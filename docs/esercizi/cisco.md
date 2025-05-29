<!-- omit from toc -->
# Esercitazioni generali

Programmi di esercitazione automazione di attività su switch Cisco, suddivisi per difficoltà.

> [!IMPORTANT]
> Questi esercizi sono pensati per essere eseguiti in un ambiente di rete Cisco, come ad esempio un simulatore o un emulatore. Assicurati di avere accesso a uno switch Cisco configurato correttamente per poter eseguire gli esercizi!

Procedi con calma e cerca di risolvere gli esercizi senza guardare le soluzioni. Se hai bisogno di aiuto, puoi consultare le soluzioni fornite.

> [!NOTE]
> A differenza degli altri esercizi, questi avranno per forza bisogno di installare dipendenze esterne (paramikko, fabric, netmiko, etc.).

- [🟢 Difficoltà: facile](#-difficoltà-facile)
  - [Connessione a switch Cisco \[ssh\]](#connessione-a-switch-cisco-ssh)
    - [Esempio](#esempio)
    - [Soluzione](#soluzione)
  - [Creazione di una nuova VLAN \[ssh\]](#creazione-di-una-nuova-vlan-ssh)
    - [Esempio](#esempio-1)
    - [Soluzione](#soluzione-1)
- [🟡 Difficoltà: medio](#-difficoltà-medio)
  - [Estrattore della configurazione relativa a una interfaccia \[ssh\]](#estrattore-della-configurazione-relativa-a-una-interfaccia-ssh)
    - [Esempio](#esempio-2)
    - [Soluzione](#soluzione-2)
  - [Modifica tutte le interfacce `shutdown` in `no shutdown` \[ssh\]](#modifica-tutte-le-interfacce-shutdown-in-no-shutdown-ssh)
    - [Esempio](#esempio-3)
    - [Soluzione](#soluzione-3)

# 🟢 Difficoltà: facile

## Connessione a switch Cisco [ssh]

Connettiti in SSH a uno switch Cisco, lancia il comando `show running-config` e stampa a schermo il risultato.

### Esempio

```text
Sei connesso allo switch (switch1.internal:2201)
Ora verranno mostrati i risultati del comando `show running-config`:

Building configuration...

Current configuration : 702 bytes
version 12.1
!
hostname switch
!
!
vlan 1
!
vlan 10
 name Users
!
vlan 20
 name Servers
!
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
!
interface FastEthernet0/2
 switchport access vlan 10
 switchport mode access
!
interface FastEthernet0/3
 switchport access vlan 20
 switchport mode access
!
interface FastEthernet0/4
 switchport mode trunk
!
interface Vlan10
 ip address 192.168.10.1 255.255.255.0
!
interface Vlan20
 no ip address
!
end
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import netmiko

if __name__ == "__main__":
    # Configurazione della connessione SSH
    device = {
        'device_type': 'cisco_ios',
        'host': 'switch1.internal',
        'port': 2201,
        'username': 'root',
        'password': 'root',
        'secret': 'root',
    }

    with netmiko.ConnectHandler(**cisco_881) as net_connect:
        print(f'Sei connesso allo switch ({device["host"]}:{device["port"]})')

        # Entra in modalità privilegiata (se necessario)
        privileged = net_connect.check_enable_mode()
        if not privileged:
            net_connect.enable()

        print('Ora verranno mostrati i risultati del comando `show running-config`:\n')
        # Esegui il comando 'show running-config'
        net_connect.send_command_timing('show running-config\n\n', 
            normalize=False,
        )
```

</details>

## Creazione di una nuova VLAN [ssh]

Crea una nuova VLAN chiamata `{cognome}_{nome}` con ID `30` e assegna l'interfaccia `FastEthernet0/5` a questa VLAN.

### Esempio

```text
Sei connesso allo switch (switch1.internal:2201)

Creazione della VLAN {cognome}_{nome} con ID 30...
VLAN 30 created successfully.
Assegnazione dell'interfaccia FastEthernet0/5 alla VLAN 30...
Interfaccia FastEthernet0/5 assegnata alla VLAN 30 con successo.
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python

import netmiko

if __name__ == "__main__":
    # Configurazione della connessione SSH
    device = {
        'device_type': 'cisco_ios',
        'host': '127.0.0.1',
        'port': 2201,
        'username': 'root',
        'password': 'root',
        'secret': 'root',
    }

    with netmiko.ConnectHandler(**device) as net_connect:
        print(f'Sei connesso allo switch ({device["host"]}:{device["port"]})')

        # Entra in modalità privilegiata (se necessario)
        privileged = net_connect.check_enable_mode()
        if not privileged:
            net_connect.enable()

        vlan_name = "COGNOME_NOME"  # Sostituisci con il tuo cognome e nome


        # Crea la VLAN 30
        print(f'Creazione della VLAN {vlan_name} con ID 30...')
        net_connect.send_config_set([
            'vlan 30',
            f'name {vlan_name}',
        ], cmd_verify=False, exit_config_mode=False)
        print('VLAN 30 creata con successo.')

        # Assegna l'interfaccia FastEthernet0/5 alla VLAN 30
        print('Assegnazione dell\'interfaccia FastEthernet0/5 alla VLAN 30...')
        net_connect.send_config_set([
            'interface FastEthernet0/5',
            'switchport mode access',
            'switchport access vlan 30',
            'no shutdown',
        ], enter_config_mode=False, cmd_verify=False, exit_config_mode=False)

        print(net_connect.send_command_timing('exit\nexit\n\n', normalize=False))

        # Salva la configurazione
        net_connect.save_config()

        print(net_connect.send_command_timing('show running-config\n\n', 
            normalize=False,
        ))
```

</details>

# 🟡 Difficoltà: medio

## Estrattore della configurazione relativa a una interfaccia [ssh]

Scrivi un programma che, data una interfaccia (ad esempio `FastEthernet0/1`), estragga e stampi a schermo la configurazione relativa a quell'interfaccia.

### Esempio

```text
Inserisci il nome dell'interfaccia (ad esempio FastEthernet0/1): FastEthernet0/1

Sei connesso allo switch (switch1.internal:2201)

Configurazione dell'interfaccia FastEthernet0/1:
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import re
import netmiko

if __name__ == "__main__":
    target_interface = input('Inserisci il nome dell\'interfaccia (ad esempio FastEthernet0/1): ')

    # Configurazione della connessione SSH
    device = {
        'device_type': 'cisco_ios',
        'host': '127.0.0.1',
        'port': 2201,
        'username': 'root',
        'password': 'root',
        'secret': 'root',
    }

    with netmiko.ConnectHandler(**device) as net_connect:
        print(f'Sei connesso allo switch ({device["host"]}:{device["port"]})')

        # Entra in modalità privilegiata (se necessario)
        privileged = net_connect.check_enable_mode()
        if not privileged:
            net_connect.enable()

        # Esegui il comando 'show running-config' e filtra per l'interfaccia specificata
        print(f'Configurazione dell\'interfaccia {target_interface}:')
        output = str(net_connect.send_command_timing(f'show running-config interface {target_interface}\n\n',
            normalize=False,
        ))

        # Stampa solo il blocco indentato (tra `interface FastEthernet0/5` e `end`) dell'interfaccia
        match = re.search(rf'interface {re.escape(target_interface)}\s*\n(.*?)(?=\nend)', output, re.DOTALL)
        if match:
            print('\n'.join([line for line in match.group(1).splitlines() if line.strip()]))  # Stampa le righe non vuote
        else:
            print(f'Configurazione per l\'interfaccia {target_interface} non trovata.')
```

</details>

## Modifica tutte le interfacce `shutdown` in `no shutdown` [ssh]

Scrivi un programma che, per ogni interfaccia che ha il comando `shutdown`, esegua il comando `no shutdown`.

### Esempio

```text
Sei connesso allo switch (switch1.internal:2201)

Trovate le seguenti interfacce con il comando 'shutdown':
- FastEthernet0/3
- FastEthernet0/5

Esecuzione del comando 'no shutdown' su tutte le interfacce trovate...

> FastEthernet0/3 modificata con successo
> FastEthernet0/5 modificata con successo

Tutte le interfacce sono state modificate con successo.
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python

from logging import shutdown
import re
import netmiko

if __name__ == "__main__":
    # Configurazione della connessione SSH
    device = {
        'device_type': 'cisco_ios',
        'host': '127.0.0.1',
        'port': 2201,
        'username': 'root',
        'password': 'root',
        'secret': 'root',
    }

    with netmiko.ConnectHandler(**device) as net_connect:
        print(f'Sei connesso allo switch ({device["host"]}:{device["port"]})')

        # Entra in modalità privilegiata (se necessario)
        privileged = net_connect.check_enable_mode()
        if not privileged:
            net_connect.enable()

        # Esegui il comando 'show running-config' e filtra per l'interfaccia specificata
        output = str(net_connect.send_command_timing('show running-config\n\n',
            normalize=False,
        ))

        # Stampa solo il blocco indentato (tra `interface FastEthernet0/5` e `end`) dell'interfaccia
        interfaces = {
            el[0]: [line.strip() for line in el[1].splitlines()]
            for el in re.findall(r'interface (.*?)\s*\n(.*?)(?=\nend|!)', output, re.DOTALL)
        }

        interfaces_with_shutdown = [
            interface 
            for interface, config in interfaces.items()
            if 'shutdown' in config
        ]

        print("Trovate le seguenti interfacce con il comando 'shutdown':")
        for interface in interfaces_with_shutdown:
            print(f' - {interface}')
        
        if interfaces_with_shutdown:
            net_connect.config_mode()

        print("Esecuzione del comando 'no shutdown' su tutte le interfacce trovate...")
        for interface in interfaces_with_shutdown:
            net_connect.send_config_set([f'interface {interface}', 'no shutdown'], enter_config_mode=False, exit_config_mode=False)
            print(f"> {interface} modificata con successo")


        if interfaces_with_shutdown:
            net_connect.send_command_timing('exit\nexit\n\n', normalize=False)

        print("Tutte le interfacce sono state modificate con successo.")
```

</details>
