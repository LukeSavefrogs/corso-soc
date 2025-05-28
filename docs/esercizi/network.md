<!-- omit from toc -->
# Network

- [🟢 Difficoltà: facile](#-difficoltà-facile)
  - [Verifica se lo switch è raggiungibile via SSH \[condizioni + socket\]](#verifica-se-lo-switch-è-raggiungibile-via-ssh-condizioni--socket)
    - [Esempio](#esempio)
    - [Soluzione](#soluzione)
    - [BONUS: Accetta parametri da riga di comando](#bonus-accetta-parametri-da-riga-di-comando)
      - [Esempio](#esempio-1)
      - [Soluzione](#soluzione-1)

# 🟢 Difficoltà: facile

## Verifica se lo switch è raggiungibile via SSH [condizioni + socket]

Dato un indirizzo IP (e opzionalmente una porta), verifica se lo switch è raggiungibile via SSH (porta XXXX). Se lo switch è raggiungibile, stampa un messaggio di successo, altrimenti stampa un messaggio di errore.

### Esempio

```text
Switch raggiungibile su porta 12345 (host: 127.0.0.1)!
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import socket

def verifica_ssh(host, porta=22, timeout=5):
    """
    Verifica se un host è raggiungibile sulla porta SSH specificata.
    
    Args:
        host (str): Indirizzo IP o hostname
        porta (int): Porta SSH (default: 22)
        timeout (int): Timeout in secondi (default: 5)
    
    Returns:
        bool: True se raggiungibile, False altrimenti
    """
    try:
        # Crea un socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Tenta la connessione
        risultato = sock.connect_ex((host, porta))
        sock.close()
        
        # Se risultato è 0, la connessione è riuscita
        return risultato == 0
        
    except socket.gaierror:
        # Errore di risoluzione del nome
        return False
    except Exception:
        # Altri errori di rete
        return False

def main():
    # Esempi di utilizzo
    host = "127.0.0.1"
    porta = 12345
    
    # Verifica raggiungibilità
    if verifica_ssh(host, porta):
        print(f"Switch raggiungibile su porta {porta} (host: {host})!")
    else:
        print(f"Switch NON raggiungibile su porta {porta} (host: {host})")

if __name__ == "__main__":
    main()
```

</details>

### BONUS: Accetta parametri da riga di comando

Puoi estendere la soluzione precedente per accettare l'indirizzo IP e la porta da riga di comando.

#### Esempio

```bash
$ python verifica_switch.py switch.internal 12345
Switch raggiungibile su porta 12345 (host: switch.internal)!
```

#### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import argparse
import socket

def verifica_ssh(host, porta=22, timeout=5):
    """
    Verifica se un host è raggiungibile sulla porta SSH specificata.
    
    Args:
        host (str): Indirizzo IP o hostname
        porta (int): Porta SSH (default: 22)
        timeout (int): Timeout in secondi (default: 5)
    
    Returns:
        bool: True se raggiungibile, False altrimenti
    """
    try:
        # Crea un socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Tenta la connessione
        risultato = sock.connect_ex((host, porta))
        sock.close()
        
        # Se risultato è 0, la connessione è riuscita
        return risultato == 0
        
    except socket.gaierror:
        # Errore di risoluzione del nome
        return False
    except Exception:
        # Altri errori di rete
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Verifica se uno switch è raggiungibile via SSH.",
        epilog="Esempio: python verifica_switch.py switch.internal 12345",
    )
    parser.add_argument("host", help="Indirizzo IP o hostname dello switch")
    parser.add_argument("porta", type=int, nargs="?", default=22, help="Porta SSH (default: 22)")

    args = parser.parse_args()

    host = args.host
    porta = args.porta  
    
    # Verifica raggiungibilità
    if verifica_ssh(host, porta):
        print(f"Switch raggiungibile su porta {porta} (host: {host})!")
    else:
        print(f"Switch NON raggiungibile su porta {porta} (host: {host})")

if __name__ == "__main__":
    main()
```
