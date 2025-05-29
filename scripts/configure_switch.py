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
name Servers
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
switchport mode access
switchport access vlan 10
!
interface FastEthernet0/2
switchport mode access
switchport access vlan 10
!
interface FastEthernet0/3
switchport mode access
switchport access vlan 20
!
interface FastEthernet0/4
switchport mode trunk
!
interface FastEthernet1/1
switchport mode trunk
!
interface FastEthernet1/2
switchport mode trunk
!
interface FastEthernet1/3
switchport mode trunk
!
interface FastEthernet1/4
switchport mode trunk
!
interface FastEthernet1/5
switchport mode trunk
!
interface FastEthernet1/6
switchport mode trunk
!
interface FastEthernet1/7
switchport mode trunk
!
interface FastEthernet1/8
switchport mode trunk
!
interface FastEthernet1/9
switchport mode trunk
!
interface FastEthernet1/10
switchport mode trunk
!
interface FastEthernet1/11
switchport mode trunk
!
interface FastEthernet1/12
switchport mode trunk
!
interface FastEthernet1/13
switchport mode trunk
!
interface FastEthernet1/14
switchport mode trunk
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
          
        print(net_connect.send_command_timing('show running-config\n\n', 
            strip_prompt=False,
            strip_command=False,
            normalize=False,
            # use_ttp=True,
            # ttp_template=str(ttp_template.resolve()),
        ))

        # Send new configuration commands
        print(net_connect.send_config_set(CONFIGURATION, strip_prompt=False, strip_command=False, cmd_verify=False, exit_config_mode=False))
        logger.info("Configuration commands sent successfully.")

        logger.debug("Prompt after configuration is '%s'", net_connect.find_prompt())

        print(net_connect.send_command_timing('exit\nexit\n\n', normalize=False))
        

        if net_connect.check_config_mode():
            raise Exception("Failed to exit configuration mode.")

        logger.info("Exited configuration mode successfully.")

        logger.debug("Prompt after exiting configuration is '%s'", net_connect.find_prompt())

        # Save the configuration
        net_connect.save_config()
        logger.info("Configuration saved successfully.")


        print(net_connect.send_command_timing('show running-config\n\n', 
            strip_prompt=False,
            strip_command=False,
            normalize=False,
            # use_ttp=True,
            # ttp_template=str(ttp_template.resolve()),
        ))

