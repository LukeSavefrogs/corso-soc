""" Connect to the switch via SSH and configure it. """
import logging
from pathlib import Path

import netmiko

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a console handler with a specific format and level
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)-8s - %(name)s - %(message)s'))

logger.addHandler(handler)

CONFIGURATION = r"""
!
vlan 10
 name Users
!
vlan 20
 name Voice
!
vlan 30
 name Guest
!
interface Vlan1
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
interface vlan 10
ip address 192.168.10.1 255.255.255.0
no shutdown
!
interface vlan 20
ip address 192.168.20.1 255.255.255.0
no shutdown
!
interface FastEthernet0/1
 description Uplink-to-Core
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
!
interface FastEthernet0/2
 description Access-Users
 switchport mode access
 switchport access vlan 10
!
interface FastEthernet0/3
 description Access-Voice
 switchport mode access
 switchport access vlan 20
!
interface FastEthernet0/4
 description Access-Guest
 switchport mode access
 switchport access vlan 30
!
interface FastEthernet0/5
 description Trunk-to-AP
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan all
!
interface FastEthernet0/6
 description QoS-Test
 switchport mode access
 switchport access vlan 10
 shutdown
!
interface FastEthernet0/7
 description Security-Port
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
!
interface FastEthernet0/8
 description Security-Port-Strict
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 1
 switchport port-security violation shutdown
!
interface FastEthernet0/9
 description Monitoring-Port
 switchport mode access
 switchport access vlan 30
!
interface FastEthernet0/10
 description Guest-LAN
 switchport mode access
 switchport access vlan 30
 shutdown
!
interface FastEthernet0/11
 description VoIP-Phone
 switchport mode access
 switchport voice vlan 20
 switchport access vlan 10
!
interface FastEthernet0/12
 description Backup-Link
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface FastEthernet0/13
 description Unused-Port
 shutdown
!
interface FastEthernet0/14
 description Unused-Port
 shutdown
!
interface FastEthernet0/15
 description Unused-Port
 shutdown
!
interface FastEthernet0/16
 description Test-Port
 switchport mode access
 switchport access vlan 10
!
\n\n
"""

# https://ttp.readthedocs.io/en/latest/Quick%20start.html
if __name__ == "__main__":    
    cisco_881 = {
        'device_type': 'cisco_ios',
        'host':   '127.0.0.1',
        'username': 'root',
        'password': 'root',
        'port' : 2201,
        'secret': 'root',
    }

    ttp_template = Path(__file__).parent / "show_run.ttp"
    

    with netmiko.ConnectHandler(**cisco_881) as net_connect:
        logger.info("Connected to the switch via SSH.")

        privileged = net_connect.check_enable_mode()
        logger.info("Privileged mode: %s", privileged)

        if not privileged:
            logger.debug("Prompt before enabling is '%s'", net_connect.find_prompt())
            net_connect.enable()
            logger.debug("Switched to privileged mode.")
            logger.debug("Prompt after enabling is '%s'", net_connect.find_prompt())

        # print(net_connect.send_command('show version'))
        logger.info("Using TTP template '%s'", ttp_template.resolve())
          
        config = net_connect.send_command_timing('show running-config\n\n', 
            normalize=False,
            # use_ttp=True,
            # ttp_template=str(ttp_template.resolve()),
        )

        # Send new configuration commands
        net_connect.send_config_set(CONFIGURATION, strip_prompt=False, strip_command=False, cmd_verify=False, exit_config_mode=False)
        logger.info("Configuration commands sent successfully.")

        # Exit from configuration mode
        logger.info("Exiting configuration mode...")
        net_connect.send_command_timing('exit\nexit\n\n', normalize=False)

        if net_connect.check_config_mode():
            raise Exception("Failed to exit configuration mode.")

        logger.info("Exited configuration mode successfully.")

        # Save the configuration
        net_connect.save_config()
        logger.info("Configuration saved successfully.")
