<!-- omit from toc -->
# Network

- [🟢 Difficoltà: facile](#-difficoltà-facile)
  - [Verifica se lo switch è raggiungibile via SSH \[condizioni + socket\]](#verifica-se-lo-switch-è-raggiungibile-via-ssh-condizioni--socket)
    - [Esempio](#esempio)
    - [Soluzione](#soluzione)
    - [BONUS: Accetta parametri da riga di comando](#bonus-accetta-parametri-da-riga-di-comando)
      - [Esempio](#esempio-1)
      - [Soluzione](#soluzione-1)
  - [Ping checker \[subprocess + condizioni\]](#ping-checker-subprocess--condizioni)
    - [Esempio](#esempio-2)
    - [Soluzione](#soluzione-2)
  - [Verifica porte aperte \[socket + cicli\]](#verifica-porte-aperte-socket--cicli)
    - [Esempio](#esempio-3)
    - [Soluzione](#soluzione-3)
  - [Ottieni indirizzo IP da hostname \[socket + eccezioni\]](#ottieni-indirizzo-ip-da-hostname-socket--eccezioni)
    - [Esempio](#esempio-4)
    - [Soluzione](#soluzione-4)
  - [Download file da URL \[requests + file I/O\]](#download-file-da-url-requests--file-io)
    - [Esempio](#esempio-5)
    - [Soluzione](#soluzione-5)
  - [Verifica connessione internet \[requests + eccezioni\]](#verifica-connessione-internet-requests--eccezioni)
    - [Esempio](#esempio-6)
    - [Soluzione](#soluzione-6)
  - [Ottieni informazioni IP pubblico \[requests + JSON\]](#ottieni-informazioni-ip-pubblico-requests--json)
    - [Esempio](#esempio-7)
    - [Soluzione](#soluzione-7)
- [🟡 Difficoltà: medio](#-difficoltà-medio)
  - [Web scraper con sessioni \[requests + BeautifulSoup\]](#web-scraper-con-sessioni-requests--beautifulsoup)
    - [Esempio](#esempio-8)
    - [Soluzione](#soluzione-8)
- [🔴 Difficoltà: difficile](#-difficoltà-difficile)
  - [Proxy HTTP semplice \[socket + threading\]](#proxy-http-semplice-socket--threading)
    - [Esempio](#esempio-9)
    - [Soluzione](#soluzione-9)

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

</details>

## Ping checker [subprocess + condizioni]

Crea un programma che fa il ping di un host e restituisce se è raggiungibile o meno.

### Esempio

```text
Inserisci l'host da pingare: google.com
✅ google.com è raggiungibile (tempo: 15ms)

Inserisci l'host da pingare: host-inesistente.com
❌ host-inesistente.com non è raggiungibile
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import subprocess
import platform
import re

def ping_host(host, count=1):
    """
    Fa il ping di un host e restituisce il risultato.
    
    Args:
        host (str): Host da pingare
        count (int): Numero di ping da inviare
    
    Returns:
        tuple: (True/False, tempo_medio_ms)
    """
    try:
        # Determina il comando ping in base al sistema operativo
        sistema = platform.system().lower()
        if sistema == "windows":
            cmd = ["ping", "-n", str(count), host]
        else:
            cmd = ["ping", "-c", str(count), host]
        
        # Esegui il ping
        risultato = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        
        if risultato.returncode == 0:
            # Estrai il tempo di risposta dall'output
            output = risultato.stdout
            if sistema == "windows":
                # Cerca pattern come "tempo=15ms"
                match = re.search(r'tempo[=<]\s*(\d+)ms', output)
            else:
                # Cerca pattern come "time=15.3 ms"
                match = re.search(r'time=(\d+\.?\d*).*ms', output)
            
            tempo = int(float(match.group(1))) if match else None
            return True, tempo
        else:
            return False, None
            
    except subprocess.TimeoutExpired:
        return False, None
    except Exception:
        return False, None

def main():
    host = input("Inserisci l'host da pingare: ")
    
    raggiungibile, tempo = ping_host(host)
    
    if raggiungibile:
        if tempo:
            print(f"✅ {host} è raggiungibile (tempo: {tempo}ms)")
        else:
            print(f"✅ {host} è raggiungibile")
    else:
        print(f"❌ {host} non è raggiungibile")

if __name__ == "__main__":
    main()
```

</details>

## Verifica porte aperte [socket + cicli]

Dato un host, verifica quali porte sono aperte in un range specificato.

### Esempio

```text
Host: 127.0.0.1
Porta iniziale: 20
Porta finale: 25

Scansione porte su 127.0.0.1:
✅ Porta 22 aperta
❌ Porta 20 chiusa
❌ Porta 21 chiusa
❌ Porta 23 chiusa
❌ Porta 24 chiusa
❌ Porta 25 chiusa

Porte aperte trovate: 1
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import socket
from concurrent.futures import ThreadPoolExecutor
import threading

def verifica_porta(host, porta, timeout=1):
    """
    Verifica se una porta specifica è aperta.
    
    Args:
        host (str): Host da verificare
        porta (int): Porta da verificare
        timeout (int): Timeout in secondi
    
    Returns:
        bool: True se la porta è aperta
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        risultato = sock.connect_ex((host, porta))
        sock.close()
        return risultato == 0
    except:
        return False

def scansiona_porte(host, porta_inizio, porta_fine, verbose=True):
    """
    Scansiona un range di porte su un host.
    
    Args:
        host (str): Host da scansionare
        porta_inizio (int): Porta iniziale
        porta_fine (int): Porta finale
        verbose (bool): Mostra dettagli per ogni porta
    
    Returns:
        list: Lista delle porte aperte
    """
    porte_aperte = []
    
    print(f"\nScansione porte su {host}:")
    
    # Usa ThreadPoolExecutor per velocizzare la scansione
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Crea un dizionario per mappare future a porte
        future_to_port = {
            executor.submit(verifica_porta, host, porta): porta 
            for porta in range(porta_inizio, porta_fine + 1)
        }
        
        # Raccogli i risultati
        for future in future_to_port:
            porta = future_to_port[future]
            try:
                aperta = future.result()
                if aperta:
                    porte_aperte.append(porta)
                
                if verbose:
                    stato = "✅ aperta" if aperta else "❌ chiusa"
                    print(f"Porta {porta} {stato}")
                    
            except Exception as e:
                if verbose:
                    print(f"❌ Porta {porta} errore: {e}")
    
    return sorted(porte_aperte)

def main():
    host = input("Host: ")
    try:
        porta_inizio = int(input("Porta iniziale: "))
        porta_fine = int(input("Porta finale: "))
        
        if porta_inizio > porta_fine:
            print("Errore: La porta iniziale deve essere <= della porta finale")
            return
        
        porte_aperte = scansiona_porte(host, porta_inizio, porta_fine)
        
        print(f"\nPorte aperte trovate: {len(porte_aperte)}")
        if porte_aperte:
            print("Porte aperte:", ", ".join(map(str, porte_aperte)))
            
    except ValueError:
        print("Errore: Inserisci numeri validi per le porte")

if __name__ == "__main__":
    main()
```

</details>

## Ottieni indirizzo IP da hostname [socket + eccezioni]

Dato un hostname o URL, ottieni il suo indirizzo IP.

### Esempio

```text
Inserisci hostname o URL: google.com
Indirizzo IP di google.com: 142.250.180.174

Inserisci hostname o URL: https://github.com
Indirizzo IP di github.com: 140.82.121.3
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import socket
import re

def pulisci_hostname(url_o_hostname):
    """
    Estrae l'hostname da una URL o restituisce l'hostname se già pulito.
    
    Args:
        url_o_hostname (str): URL o hostname
    
    Returns:
        str: Hostname pulito
    """
    # Rimuovi protocollo se presente
    if "://" in url_o_hostname:
        url_o_hostname = url_o_hostname.split("://")[1]
    
    # Rimuovi path se presente
    if "/" in url_o_hostname:
        url_o_hostname = url_o_hostname.split("/")[0]
    
    # Rimuovi porta se presente
    if ":" in url_o_hostname:
        url_o_hostname = url_o_hostname.split(":")[0]
    
    return url_o_hostname

def ottieni_ip(hostname):
    """
    Ottiene l'indirizzo IP di un hostname.
    
    Args:
        hostname (str): Hostname da risolvere
    
    Returns:
        str: Indirizzo IP o None se non trovato
    """
    try:
        hostname_pulito = pulisci_hostname(hostname)
        ip = socket.gethostbyname(hostname_pulito)
        return ip, hostname_pulito
    except socket.gaierror:
        return None, hostname

def ottieni_tutti_ip(hostname):
    """
    Ottiene tutti gli indirizzi IP associati a un hostname.
    
    Args:
        hostname (str): Hostname da risolvere
    
    Returns:
        list: Lista di indirizzi IP
    """
    try:
        hostname_pulito = pulisci_hostname(hostname)
        _, _, ip_list = socket.gethostbyname_ex(hostname_pulito)
        return ip_list, hostname_pulito
    except socket.gaierror:
        return [], hostname

def main():
    hostname = input("Inserisci hostname o URL: ")
    
    # Ottieni IP principale
    ip, hostname_pulito = ottieni_ip(hostname)
    
    if ip:
        print(f"Indirizzo IP di {hostname_pulito}: {ip}")
        
        # Ottieni tutti gli IP
        tutti_ip, _ = ottieni_tutti_ip(hostname)
        if len(tutti_ip) > 1:
            print(f"Altri indirizzi IP: {', '.join(tutti_ip[1:])}")
    else:
        print(f"❌ Impossibile risolvere {hostname_pulito}")

if __name__ == "__main__":
    main()
```

</details>

## Download file da URL [requests + file I/O]

Scarica un file da un URL e salvalo localmente, mostrando il progresso.

### Esempio

```text
Inserisci URL del file: https://httpbin.org/bytes/1024
Nome file (invio per auto): test.bin

Scaricando test.bin...
████████████████████████████████ 100% (1024/1024 bytes)
✅ File scaricato con successo: test.bin
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import requests
import os
from urllib.parse import urlparse

def scarica_file(url, nome_file=None, mostra_progresso=True):
    """
    Scarica un file da un URL.
    
    Args:
        url (str): URL del file da scaricare
        nome_file (str): Nome del file locale (opzionale)
        mostra_progresso (bool): Mostra barra di progresso
    
    Returns:
        bool: True se il download è riuscito
    """
    try:
        # Se non è specificato un nome, usa quello dall'URL
        if not nome_file:
            parsed_url = urlparse(url)
            nome_file = os.path.basename(parsed_url.path)
            if not nome_file:
                nome_file = "download"
        
        print(f"Scaricando {nome_file}...")
        
        # Fai la richiesta con stream=True per scaricare a pezzi
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Ottieni la dimensione totale se disponibile
        dimensione_totale = int(response.headers.get('content-length', 0))
        
        with open(nome_file, 'wb') as file:
            dimensione_scaricata = 0
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    dimensione_scaricata += len(chunk)
                    
                    if mostra_progresso and dimensione_totale > 0:
                        # Calcola percentuale
                        percentuale = (dimensione_scaricata / dimensione_totale) * 100
                        
                        # Crea barra di progresso
                        barra_lunghezza = 30
                        riempimento = int(barra_lunghezza * percentuale / 100)
                        barra = "█" * riempimento + "░" * (barra_lunghezza - riempimento)
                        
                        print(f"\r{barra} {percentuale:.1f}% ({dimensione_scaricata}/{dimensione_totale} bytes)", end="")
        
        if mostra_progresso:
            print()  # Nuova linea dopo la barra di progresso
        
        print(f"✅ File scaricato con successo: {nome_file}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Errore durante il download: {e}")
        return False
    except Exception as e:
        print(f"❌ Errore imprevisto: {e}")
        return False

def main():
    url = input("Inserisci URL del file: ")
    nome_file = input("Nome file (invio per auto): ").strip()
    
    if not nome_file:
        nome_file = None
    
    scarica_file(url, nome_file)

if __name__ == "__main__":
    main()
```

</details>

## Verifica connessione internet [requests + eccezioni]

Verifica se il computer ha una connessione internet attiva.

### Esempio

```text
Verificando connessione internet...
✅ Connessione internet attiva
Velocità di risposta: 156ms
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import requests
import time

def verifica_connessione(timeout=5, url_test="https://8.8.8.8"):
    """
    Verifica se c'è una connessione internet attiva.
    
    Args:
        timeout (int): Timeout in secondi
        url_test (str): URL da testare
    
    Returns:
        tuple: (connesso, tempo_risposta_ms)
    """
    try:
        inizio = time.time()
        response = requests.get(url_test, timeout=timeout)
        fine = time.time()
        
        tempo_risposta = int((fine - inizio) * 1000)
        
        # Considera connesso se lo status code è 200
        connesso = response.status_code == 200
        return connesso, tempo_risposta
        
    except requests.exceptions.RequestException:
        return False, None
    except Exception:
        return False, None

def verifica_multipli_servizi():
    """
    Verifica la connessione usando più servizi per maggiore affidabilità.
    
    Returns:
        dict: Risultati per ogni servizio
    """
    servizi = {
        "Google DNS": "https://8.8.8.8",
        "Cloudflare": "https://1.1.1.1", 
        "Google": "https://www.google.com",
        "GitHub": "https://api.github.com"
    }
    
    risultati = {}
    
    for nome, url in servizi.items():
        connesso, tempo = verifica_connessione(url_test=url, timeout=3)
        risultati[nome] = {
            'connesso': connesso,
            'tempo': tempo
        }
    
    return risultati

def main():
    print("Verificando connessione internet...")
    
    # Test semplice
    connesso, tempo = verifica_connessione()
    
    if connesso:
        print("✅ Connessione internet attiva")
        if tempo:
            print(f"Velocità di risposta: {tempo}ms")
    else:
        print("❌ Nessuna connessione internet")
        return
    
    # Test dettagliato
    risposta = input("\nVuoi fare un test dettagliato? (s/n): ")
    if risposta.lower() == 's':
        print("\nTest dettagliato in corso...")
        risultati = verifica_multipli_servizi()
        
        print("\nRisultati per servizio:")
        for servizio, dati in risultati.items():
            if dati['connesso']:
                tempo_str = f" ({dati['tempo']}ms)" if dati['tempo'] else ""
                print(f"✅ {servizio}: OK{tempo_str}")
            else:
                print(f"❌ {servizio}: Non raggiungibile")
        
        # Statistiche
        connessi = sum(1 for r in risultati.values() if r['connesso'])
        totali = len(risultati)
        percentuale = (connessi / totali) * 100
        
        print(f"\nConnettività: {connessi}/{totali} servizi ({percentuale:.1f}%)")

if __name__ == "__main__":
    main()
```

</details>

## Ottieni informazioni IP pubblico [requests + JSON]

Ottieni informazioni dettagliate sul tuo indirizzo IP pubblico (geolocalizzazione, ISP, ecc.).

### Esempio

```text
Ottenendo informazioni IP pubblico...

=== INFORMAZIONI IP PUBBLICO ===
IP: 203.0.113.195
Paese: Italy (IT)
Regione: Lazio
Città: Rome
ISP: Example Internet Provider
Timezone: Europe/Rome
Coordinata: 41.9028, 12.4964
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import requests
import json

def ottieni_ip_pubblico():
    """
    Ottiene solo l'indirizzo IP pubblico.
    
    Returns:
        str: Indirizzo IP pubblico o None
    """
    servizi = [
        "https://api.ipify.org",
        "https://ident.me",
        "https://ipecho.net/plain",
        "https://icanhazip.com"
    ]
    
    for servizio in servizi:
        try:
            response = requests.get(servizio, timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            continue
    
    return None

def ottieni_info_dettagliate_ip(ip=None):
    """
    Ottiene informazioni dettagliate sull'IP.
    
    Args:
        ip (str): IP da analizzare (None per IP corrente)
    
    Returns:
        dict: Dizionario con le informazioni
    """
    try:
        if ip:
            url = f"http://ip-api.com/json/{ip}"
        else:
            url = "http://ip-api.com/json"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Errore nella richiesta: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Errore nel parsing della risposta JSON")
        return None

def formatta_info_ip(info):
    """
    Formatta le informazioni IP per la visualizzazione.
    
    Args:
        info (dict): Dizionario con le informazioni IP
    """
    if not info or info.get('status') != 'success':
        print("❌ Impossibile ottenere informazioni dettagliate")
        return
    
    print("\n=== INFORMAZIONI IP PUBBLICO ===")
    print(f"IP: {info.get('query', 'N/A')}")
    print(f"Paese: {info.get('country', 'N/A')} ({info.get('countryCode', 'N/A')})")
    print(f"Regione: {info.get('regionName', 'N/A')}")
    print(f"Città: {info.get('city', 'N/A')}")
    print(f"ISP: {info.get('isp', 'N/A')}")
    print(f"Organizzazione: {info.get('org', 'N/A')}")
    print(f"Timezone: {info.get('timezone', 'N/A')}")
    
    if info.get('lat') and info.get('lon'):
        print(f"Coordinate: {info['lat']}, {info['lon']}")
    
    if info.get('zip'):
        print(f"Codice postale: {info['zip']}")

def main():
    print("Ottenendo informazioni IP pubblico...")
    
    # Prima ottieni l'IP
    ip_pubblico = ottieni_ip_pubblico()
    
    if not ip_pubblico:
        print("❌ Impossibile ottenere l'IP pubblico")
        return
    
    # Poi ottieni le informazioni dettagliate
    info = ottieni_info_dettagliate_ip()
    formatta_info_ip(info)
    
    # Opzione per analizzare un altro IP
    altro_ip = input("\nVuoi analizzare un altro IP? (inserisci IP o invio per uscire): ").strip()
    if altro_ip:
        print(f"\nAnalizzando {altro_ip}...")
        info_altro = ottieni_info_dettagliate_ip(altro_ip)
        formatta_info_ip(info_altro)

if __name__ == "__main__":
    main()
```

</details>

# 🟡 Difficoltà: medio

## Web scraper con sessioni [requests + BeautifulSoup]

Crea un web scraper che mantenga sessioni e possa estrarre dati da pagine web.

### Esempio

```text
=== WEB SCRAPER ===
URL: https://quotes.toscrape.com
Selettore CSS: .quote

Estratti 10 elementi:
1. "The world as we have created it..." - Albert Einstein
2. "It is our choices, Harry..." - J.K. Rowling
3. "There are only two ways to live..." - Albert Einstein

Salvato in: quotes_data.json
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import re
from urllib.parse import urljoin, urlparse

class WebScraper:
    def __init__(self, delay=1, timeout=10):
        self.session = requests.Session()
        self.delay = delay  # Delay tra richieste
        self.timeout = timeout
        
        # User agent realistico
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_page(self, url):
        """Ottiene il contenuto di una pagina"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            # Rispetta il delay
            if self.delay > 0:
                time.sleep(self.delay)
            
            return response
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Errore nel caricamento di {url}: {e}")
            return None
    
    def estrai_elementi(self, url, selettore_css, attributo=None):
        """Estrae elementi usando selettori CSS"""
        response = self.get_page(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        elementi = soup.select(selettore_css)
        
        risultati = []
        for elemento in elementi:
            if attributo:
                valore = elemento.get(attributo)
            else:
                valore = elemento.get_text(strip=True)
            
            if valore:
                risultati.append(valore)
        
        return risultati
    
    def estrai_quotes(self, url):
        """Esempio specifico: estrazione quote da quotes.toscrape.com"""
        response = self.get_page(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = []
        
        for quote_div in soup.select('.quote'):
            testo = quote_div.select_one('.text')
            autore = quote_div.select_one('.author')
            tags = quote_div.select('.tag')
            
            if testo and autore:
                quote_data = {
                    'testo': testo.get_text(strip=True),
                    'autore': autore.get_text(strip=True),
                    'tags': [tag.get_text(strip=True) for tag in tags]
                }
                quotes.append(quote_data)
        
        return quotes
    
    def estrai_links(self, url, filtro=None):
        """Estrae tutti i link da una pagina"""
        response = self.get_page(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            # Converti link relativi in assoluti
            absolute_url = urljoin(url, href)
            
            link_data = {
                'url': absolute_url,
                'testo': link.get_text(strip=True),
                'title': link.get('title', '')
            }
            
            # Applica filtro se specificato
            if filtro:
                if filtro.lower() in absolute_url.lower() or filtro.lower() in link_data['testo'].lower():
                    links.append(link_data)
            else:
                links.append(link_data)
        
        return links
    
    def salva_dati(self, dati, nome_file, formato='json'):
        """Salva i dati estratti in diversi formati"""
        try:
            if formato == 'json':
                with open(nome_file, 'w', encoding='utf-8') as f:
                    json.dump(dati, f, indent=2, ensure_ascii=False)
            
            elif formato == 'csv':
                if not dati:
                    return False
                
                # Assume che i dati siano una lista di dizionari
                with open(nome_file, 'w', newline='', encoding='utf-8') as f:
                    if isinstance(dati[0], dict):
                        writer = csv.DictWriter(f, fieldnames=dati[0].keys())
                        writer.writeheader()
                        writer.writerows(dati)
                    else:
                        writer = csv.writer(f)
                        for item in dati:
                            writer.writerow([item])
            
            elif formato == 'txt':
                with open(nome_file, 'w', encoding='utf-8') as f:
                    for item in dati:
                        f.write(str(item) + '\n')
            
            print(f"✅ Dati salvati in: {nome_file}")
            return True
            
        except Exception as e:
            print(f"❌ Errore nel salvataggio: {e}")
            return False

def main():
    print("=== WEB SCRAPER ===")
    
    scraper = WebScraper(delay=1)
    
    while True:
        print("\n1. Estrai testo con selettore CSS")
        print("2. Estrai quotes (quotes.toscrape.com)")
        print("3. Estrai links da una pagina")
        print("4. Configura scraper")
        print("5. Esci")
        
        try:
            scelta = int(input("Scelta: "))
            
            if scelta == 5:
                break
            
            elif scelta == 1:
                url = input("URL: ")
                selettore = input("Selettore CSS: ")
                attributo = input("Attributo da estrarre (invio per testo): ").strip() or None
                
                print("Estrazione in corso...")
                risultati = scraper.estrai_elementi(url, selettore, attributo)
                
                if risultati:
                    print(f"\nEstratti {len(risultati)} elementi:")
                    for i, item in enumerate(risultati[:10], 1):
                        print(f"{i}. {item[:100]}{'...' if len(str(item)) > 100 else ''}")
                    
                    if len(risultati) > 10:
                        print(f"... e altri {len(risultati) - 10} elementi")
                    
                    # Salvataggio
                    salva = input("\nSalvare i dati? (s/n): ").lower() == 's'
                    if salva:
                        nome_file = input("Nome file: ")
                        formato = input("Formato (json/csv/txt): ").lower() or 'json'
                        scraper.salva_dati(risultati, nome_file, formato)
                else:
                    print("Nessun elemento trovato")
            
            elif scelta == 2:
                url = input("URL quotes (default: https://quotes.toscrape.com): ") or "https://quotes.toscrape.com"
                
                print("Estrazione quotes...")
                quotes = scraper.estrai_quotes(url)
                
                if quotes:
                    print(f"\nEstratte {len(quotes)} citazioni:")
                    for i, quote in enumerate(quotes[:5], 1):
                        print(f"{i}. \"{quote['testo'][:50]}...\" - {quote['autore']}")
                    
                    # Salvataggio
                    scraper.salva_dati(quotes, 'quotes_data.json', 'json')
                else:
                    print("Nessuna citazione trovata")
            
            elif scelta == 3:
                url = input("URL: ")
                filtro = input("Filtro per link (opzionale): ").strip() or None
                
                print("Estrazione links...")
                links = scraper.estrai_links(url, filtro)
                
                if links:
                    print(f"\nTrovati {len(links)} link:")
                    for i, link in enumerate(links[:10], 1):
                        print(f"{i}. {link['testo'][:30]} -> {link['url']}")
                    
                    # Salvataggio
                    salva = input("\nSalvare i link? (s/n): ").lower() == 's'
                    if salva:
                        scraper.salva_dati(links, 'links_data.json', 'json')
                else:
                    print("Nessun link trovato")
            
            elif scelta == 4:
                try:
                    delay = float(input(f"Delay tra richieste (attuale: {scraper.delay}s): ") or scraper.delay)
                    timeout = float(input(f"Timeout (attuale: {scraper.timeout}s): ") or scraper.timeout)
                    
                    scraper.delay = delay
                    scraper.timeout = timeout
                    print("Configurazione aggiornata")
                except ValueError:
                    print("Valori non validi")
            
            else:
                print("Scelta non valida")
                
        except ValueError:
            print("Inserisci un numero valido")
        except KeyboardInterrupt:
            print("\nUscita...")
            break

if __name__ == "__main__":
    main()
```

</details>

# 🔴 Difficoltà: difficile

## Proxy HTTP semplice [socket + threading]

Implementa un proxy HTTP che inoltra richieste e può loggare il traffico.

### Esempio

```text
=== PROXY HTTP ===
Proxy avviato su localhost:8888

[10:30:15] GET http://example.com/page.html - 200 OK (1.2s)
[10:30:16] POST http://api.example.com/data - 404 Not Found (0.8s)

Traffico loggato in: proxy_log.txt
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import socket
import threading
import time
from datetime import datetime
import re
import os

class HTTPProxy:
    def __init__(self, host='localhost', porta=8888, log_file='proxy_log.txt'):
        self.host = host
        self.porta = porta
        self.log_file = log_file
        self.attivo = False
        self.server_socket = None
        self.connessioni_attive = 0
        self.log_lock = threading.Lock()
    
    def log_message(self, messaggio):
        """Logga messaggio con timestamp"""
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        log_entry = f"{timestamp} {messaggio}"
        
        print(log_entry)
        
        # Salva anche su file
        with self.log_lock:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.write(log_entry + '\n')
            except:
                pass
    
    def parse_http_request(self, data):
        """Parsa richiesta HTTP per estrarre metodo, URL, host"""
        try:
            lines = data.decode('utf-8').split('\n')
            first_line = lines[0]
            
            # Estrai metodo e URL
            parts = first_line.split()
            if len(parts) >= 2:
                metodo = parts[0]
                url = parts[1]
                
                # Estrai host dall'header Host
                host = None
                porta = 80
                
                for line in lines[1:]:
                    if line.lower().startswith('host:'):
                        host_header = line.split(':', 1)[1].strip()
                        if ':' in host_header:
                            host, porta_str = host_header.split(':', 1)
                            try:
                                porta = int(porta_str)
                            except:
                                porta = 80
                        else:
                            host = host_header
                        break
                
                # Se URL è relativo, costruisci URL completo
                if not url.startswith('http'):
                    if host:
                        schema = 'https' if porta == 443 else 'http'
                        url = f"{schema}://{host}{url}"
                
                return metodo, url, host, porta
                
        except Exception as e:
            self.log_message(f"Errore parsing richiesta: {e}")
        
        return None, None, None, None
    
    def gestisci_connessione(self, client_socket, client_address):
        """Gestisce una singola connessione client"""
        self.connessioni_attive += 1
        
        try:
            # Ricevi richiesta dal client
            data = client_socket.recv(4096)
            if not data:
                return
            
            # Parsa richiesta
            metodo, url, host, porta = self.parse_http_request(data)
            
            if not host:
                self.log_message("Richiesta non valida - host mancante")
                client_socket.close()
                return
            
            start_time = time.time()
            
            # Connetti al server di destinazione
            try:
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_socket.settimeout(10)
                server_socket.connect((host, porta))
                
                # Inoltra richiesta originale
                server_socket.send(data)
                
                # Ricevi risposta dal server
                response_data = b""
                while True:
                    try:
                        chunk = server_socket.recv(4096)
                        if not chunk:
                            break
                        response_data += chunk
                        
                        # Invia chunk al client immediatamente
                        client_socket.send(chunk)
                        
                        # Se abbiamo ricevuto headers completi, controlla Content-Length
                        if b'\r\n\r\n' in response_data:
                            headers_end = response_data.find(b'\r\n\r\n')
                            headers = response_data[:headers_end].decode('utf-8', errors='ignore')
                            
                            # Cerca Content-Length
                            content_length_match = re.search(r'Content-Length:\s*(\d+)', headers, re.IGNORECASE)
                            if content_length_match:
                                content_length = int(content_length_match.group(1))
                                body_length = len(response_data) - headers_end - 4
                                
                                # Se abbiamo ricevuto tutto il contenuto, esci
                                if body_length >= content_length:
                                    break
                    
                    except socket.timeout:
                        break
                    except:
                        break
                
                server_socket.close()
                
                # Estrai status code dalla risposta
                status_code = "???"
                if response_data:
                    try:
                        status_line = response_data.split(b'\n')[0].decode('utf-8')
                        status_parts = status_line.split()
                        if len(status_parts) >= 2:
                            status_code = status_parts[1]
                    except:
                        pass
                
                end_time = time.time()
                duration = end_time - start_time
                
                self.log_message(f"{metodo} {url} - {status_code} ({duration:.1f}s)")
                
            except Exception as e:
                # Invia errore 502 al client
                error_response = (
                    "HTTP/1.1 502 Bad Gateway\r\n"
                    "Content-Type: text/html\r\n"
                    "Content-Length: 50\r\n"
                    "\r\n"
                    "<html><body>Errore proxy: server non raggiungibile</body></html>"
                ).encode('utf-8')
                
                try:
                    client_socket.send(error_response)
                except:
                    pass
                
                self.log_message(f"{metodo} {url} - 502 Bad Gateway (errore: {e})")
        
        except Exception as e:
            self.log_message(f"Errore gestione connessione: {e}")
        
        finally:
            client_socket.close()
            self.connessioni_attive -= 1
    
    def avvia(self):
        """Avvia il proxy server"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.porta))
            self.server_socket.listen(5)
            
            self.attivo = True
            self.log_message(f"Proxy HTTP avviato su {self.host}:{self.porta}")
            self.log_message(f"Log salvato in: {self.log_file}")
            
            while self.attivo:
                try:
                    client_socket, client_address = self.server_socket.accept()
                    
                    # Gestisci connessione in thread separato
                    thread = threading.Thread(
                        target=self.gestisci_connessione,
                        args=(client_socket, client_address)
                    )
                    thread.daemon = True
                    thread.start()
                    
                except socket.error:
                    if self.attivo:
                        self.log_message("Errore accettazione connessione")
                    break
        
        except Exception as e:
            self.log_message(f"Errore avvio server: {e}")
        
        finally:
            self.ferma()
    
    def ferma(self):
        """Ferma il proxy server"""
        self.attivo = False
        if self.server_socket:
            self.server_socket.close()
        self.log_message("Proxy fermato")
    
    def mostra_stato(self):
        """Mostra stato del proxy"""
        print(f"\n=== STATO PROXY ===")
        print(f"Attivo: {'Sì' if self.attivo else 'No'}")
        print(f"Indirizzo: {self.host}:{self.porta}")
        print(f"Connessioni attive: {self.connessioni_attive}")
        print(f"Log file: {self.log_file}")

def main():
    print("=== PROXY HTTP ===")
    
    # Configurazione
    try:
        porta = int(input("Porta proxy (default 8888): ") or 8888)
    except ValueError:
        porta = 8888
    
    log_file = input("File di log (default proxy_log.txt): ") or "proxy_log.txt"
    
    proxy = HTTPProxy(porta=porta, log_file=log_file)
    
    # Avvia proxy in thread separato
    proxy_thread = threading.Thread(target=proxy.avvia)
    proxy_thread.daemon = True
    proxy_thread.start()
    
    print(f"\nConfigura il tuo browser per usare il proxy:")
    print(f"  Host: localhost")
    print(f"  Porta: {porta}")
    print(f"\nComandi: 'status', 'stop'")
    
    try:
        while proxy.attivo:
            comando = input("\n> ").strip().lower()
            
            if comando == 'stop':
                break
            elif comando == 'status':
                proxy.mostra_stato()
            elif comando == 'help':
                print("Comandi disponibili:")
                print("  status - Mostra stato proxy")
                print("  stop   - Ferma il proxy")
                print("  help   - Mostra questo aiuto")
            elif comando:
                print("Comando non riconosciuto. Usa 'help' per vedere i comandi.")
    
    except KeyboardInterrupt:
        pass
    
    finally:
        proxy.ferma()

if __name__ == "__main__":
    main()
```

</details>
