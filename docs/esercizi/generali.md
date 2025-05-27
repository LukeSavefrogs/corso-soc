<!-- omit from toc -->
# Esercitazioni generali

- [Verifica età \[condizioni | principiante\]](#verifica-età-condizioni--principiante)
  - [Esempio](#esempio)
  - [Soluzione](#soluzione)
- [Calcolo dell'area di un triangolo \[matematica + input | principiante\]](#calcolo-dellarea-di-un-triangolo-matematica--input--principiante)
  - [Esempio](#esempio-1)
  - [Soluzione](#soluzione-1)
- [Convertitore di temperature \[matematica + formule | principiante\]](#convertitore-di-temperature-matematica--formule--principiante)
  - [Esempio](#esempio-2)
  - [Soluzione](#soluzione-2)
- [Inverti una stringa \[stringhe + slicing | principiante\]](#inverti-una-stringa-stringhe--slicing--principiante)
  - [Esempio](#esempio-3)
  - [Soluzione](#soluzione-3)
- [Palindromo \[stringhe + slicing | principiante\]](#palindromo-stringhe--slicing--principiante)
  - [Esempio](#esempio-4)
  - [Soluzione](#soluzione-4)
- [Conteggio caratteri in una stringa \[stringhe | principiante\]](#conteggio-caratteri-in-una-stringa-stringhe--principiante)
  - [Esempio](#esempio-5)
  - [Soluzione](#soluzione-5)
- [Trova il massimo in una lista \[liste | principiante\]](#trova-il-massimo-in-una-lista-liste--principiante)
  - [Esempio](#esempio-6)
  - [Soluzione](#soluzione-6)
- [Media di una lista di numeri \[liste + matematica + input parsing | principiante\]](#media-di-una-lista-di-numeri-liste--matematica--input-parsing--principiante)
  - [Esempio](#esempio-7)
  - [Soluzione](#soluzione-7)
- [Calcolo del fattoriale \[cicli + matematica | principiante\]](#calcolo-del-fattoriale-cicli--matematica--principiante)
  - [Esempio](#esempio-8)
  - [Soluzione](#soluzione-8)
  - [Bonus](#bonus)
  - [Soluzione bonus](#soluzione-bonus)
- [Tabellina di un numero \[cicli + matematica | principiante\]](#tabellina-di-un-numero-cicli--matematica--principiante)
  - [Esempio](#esempio-9)
  - [Soluzione](#soluzione-9)
- [Conta le vocali in una frase \[stringhe + cicli + condizioni | principiante\]](#conta-le-vocali-in-una-frase-stringhe--cicli--condizioni--principiante)
  - [Esempio](#esempio-10)
  - [Soluzione](#soluzione-10)
- [Trova tutti i divisori di un numero \[cicli + matematica + condizioni | intermedio\]](#trova-tutti-i-divisori-di-un-numero-cicli--matematica--condizioni--intermedio)
  - [Esempio](#esempio-11)
  - [Soluzione](#soluzione-11)
- [Generatore di password casuale \[random + stringhe + cicli | intermedio\]](#generatore-di-password-casuale-random--stringhe--cicli--intermedio)
  - [Esempio](#esempio-12)
  - [Soluzione](#soluzione-12)
- [Gioco "Indovina il numero" \[random + cicli + condizioni | intermedio\]](#gioco-indovina-il-numero-random--cicli--condizioni--intermedio)
  - [Esempio](#esempio-13)
  - [Soluzione](#soluzione-13)
- [Validatore di password \[stringhe + regex + condizioni | avanzato\]](#validatore-di-password-stringhe--regex--condizioni--avanzato)
  - [Esempio](#esempio-14)
  - [Soluzione](#soluzione-14)
- [Analizzatore di testo \[dizionari + stringhe + file I/O | avanzato\]](#analizzatore-di-testo-dizionari--stringhe--file-io--avanzato)
  - [Esempio](#esempio-15)
  - [Soluzione](#soluzione-15)
- [Sistema di gestione inventario \[classi + OOP + file JSON | avanzato\]](#sistema-di-gestione-inventario-classi--oop--file-json--avanzato)
  - [Esempio](#esempio-16)
  - [Soluzione](#soluzione-16)
- [Mini calcolatrice con cronologia \[funzioni + liste + persistenza | avanzato\]](#mini-calcolatrice-con-cronologia-funzioni--liste--persistenza--avanzato)
  - [Esempio](#esempio-17)
  - [Soluzione](#soluzione-17)
- [Cifrario di Cesare con chiave variabile \[stringhe + crittografia + ASCII | avanzato\]](#cifrario-di-cesare-con-chiave-variabile-stringhe--crittografia--ascii--avanzato)
  - [Esempio](#esempio-18)
  - [Soluzione](#soluzione-18)

## Verifica età [condizioni | principiante]

Data in ingresso l'età di un utente, stampare i seguenti valori:
- `Anziano` (età >= 70)
- `Adulto` (35 <= età < 70)
- `Ragazzo` (18 <= età < 35)
- `Adolescente` (14 <= età < 18)
- `Bambino` (4 <= età < 14)
- `Neonato` (0 <= età < 4)

### Esempio

```text
Inserisci la tua età: 26

Sei un ragazzo.
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
age = int(input("Inserisci la tua età: "))
if age >= 70:
    print("Sei un anziano.")
elif age >= 35:
    print("Sei un adulto.")
elif age >= 18:
    print("Sei un ragazzo.")
elif age >= 14:
    print("Sei un adolescente.")
elif age >= 4:
    print("Sei un bambino.")
else:
    print("Sei un neonato.")
```

</details>

## Calcolo dell'area di un triangolo [matematica + input | principiante]

Chiedi all'utente di inserire la base e l'altezza di un triangolo e calcola l'area.

### Esempio

```text
Inserisci la base del triangolo: 10
Inserisci l'altezza del triangolo: 5

L'area del triangolo è: 25.0
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
base = float(input("Inserisci la base del triangolo: "))
altezza = float(input("Inserisci l'altezza del triangolo: "))
area = (base * altezza) / 2
print(f"L'area del triangolo è: {area}")
```

</details>

## Convertitore di temperature [matematica + formule | principiante]

Chiedi all'utente di inserire una temperatura in Celsius e convertila in Fahrenheit e Kelvin.

### Esempio

```text
Inserisci la temperatura in Celsius: 25

25°C = 77.0°F
25°C = 298.15K
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
celsius = float(input("Inserisci la temperatura in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin}K")
```

</details>

## Inverti una stringa [stringhe + slicing | principiante]

Chiedi all'utente di inserire una stringa e stampa la stringa invertita.

### Esempio

```text
Inserisci una stringa: programmazione

Stringa invertita: enoizamargorp
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
stringa = input("Inserisci una stringa: ")
print("Stringa invertita:", stringa[::-1])
```

</details>

## Palindromo [stringhe + slicing | principiante]

Chiedi all’utente di inserire una parola e verifica se è palindroma.

### Esempio

```text
Inserisci una parola: radar

La parola è palindroma.
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
parola = input("Inserisci una parola: ")
if parola == parola[::-1]:
    print("La parola è palindroma.")
else:
    print("La parola NON è palindroma.")
```

</details>

## Conteggio caratteri in una stringa [stringhe | principiante]

Chiedi all'utente di inserire una stringa e conta quanti caratteri, parole e righe contiene.

### Esempio

```text
Inserisci una stringa: Ciao mondo! Come va?

Caratteri: 20
Parole: 4
Righe: 1
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
stringa = input("Inserisci una stringa: ")
caratteri = len(stringa)
parole = len(stringa.split())
righe = stringa.count('\n') + 1

print(f"Caratteri: {caratteri}")
print(f"Parole: {parole}")
print(f"Righe: {righe}")
```

</details>

## Trova il massimo in una lista [liste | principiante]

Chiedi all’utente di inserire una lista di numeri separati da spazio e stampa il massimo.

### Esempio

```text
Inserisci una lista di numeri separati da spazio: 3 7 2 9 5

Il massimo è: 9
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
numeri = list(map(int, input("Inserisci una lista di numeri separati da spazio: ").split()))
# Same as the following:
# numeri = [int(x) for x in input("Inserisci una lista di numeri separati da spazio: ").split()]
print("Il massimo è:", max(numeri))
```

</details>

## Media di una lista di numeri [liste + matematica + input parsing | principiante]

Chiedi all'utente di inserire una lista di numeri separati da spazio e calcola la media.

### Esempio

```text
Inserisci una lista di numeri separati da spazio: 10 20 30 40 50

La media è: 30.0
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
numeri = list(map(int, input("Inserisci una lista di numeri separati da spazio: ").split()))
media = sum(numeri) / len(numeri)
print(f"La media è: {media}")
```

</details>

## Calcolo del fattoriale [cicli + matematica | principiante]

Chiedi all’utente di inserire un numero intero positivo e stampa il suo fattoriale.

### Esempio

```text
Inserisci un numero: 5

Il fattoriale di 5 è: 120
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
n = int(input("Inserisci un numero: "))
fattoriale = 1
for i in range(1, n + 1):
    fattoriale *= i
print(f"Il fattoriale di {n} è: {fattoriale}")
```

</details>

### Bonus

Risolvi il problema utilizzando una funzione ricorsiva.

### Soluzione bonus

<details>
<summary>✅ Mostra soluzione bonus</summary>

```python
def fattoriale(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fattoriale(n - 1)

# [PRO TIP] Same as the following:
# fattoriale = lambda n: 1 if n in (0, 1) else n * fattoriale(n - 1)

n = int(input("Inserisci un numero: "))
print(f"Il fattoriale di {n} è: {fattoriale(n)}")
```

</details>

## Tabellina di un numero [cicli + matematica | principiante]

Chiedi all'utente di inserire un numero e stampa la sua tabellina (da 1 a 10).

### Esempio

```text
Inserisci un numero: 7

Tabellina del 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
n = int(input("Inserisci un numero: "))
print(f"Tabellina del {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

</details>

## Conta le vocali in una frase [stringhe + cicli + condizioni | principiante]

Chiedi all’utente di inserire una frase e conta quante vocali contiene.

### Esempio

```text
Inserisci una frase: Ciao come va?

La frase contiene 6 vocali.
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
frase = input("Inserisci una frase: ").lower()
vocali = "aeiou"
conteggio = sum(1 for char in frase if char in vocali)
print(f"La frase contiene {conteggio} vocali.")
```

</details>

## Trova tutti i divisori di un numero [cicli + matematica + condizioni | intermedio]

Chiedi all’utente di inserire un numero e stampa tutti i suoi divisori.

### Esempio

```text
Inserisci un numero: 12

I divisori di 12 sono: 1 2 3 4 6 12
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
n = int(input("Inserisci un numero: "))
divisori = [i for i in range(1, n + 1) if n % i == 0]
print(f"I divisori di {n} sono: " + ' '.join(divisori))
```

</details>

## Generatore di password casuale [random + stringhe + cicli | intermedio]

Chiedi all'utente di inserire la lunghezza desiderata e genera una password casuale con lettere, numeri e simboli.

### Esempio

```text
Inserisci la lunghezza della password: 8

Password generata: aB3$kL9m
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import random
import string

lunghezza = int(input("Inserisci la lunghezza della password: "))
caratteri = string.ascii_letters + string.digits + "!@#$%^&*"
password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
print(f"Password generata: {password}")
```

</details>

## Gioco "Indovina il numero" [random + cicli + condizioni | intermedio]

Il computer sceglie un numero casuale tra 1 e 100. L'utente deve indovinarlo, ricevendo suggerimenti "troppo alto" o "troppo basso".

### Esempio

```text
Ho pensato un numero tra 1 e 100. Indovina!

Inserisci il tuo numero: 50
Troppo alto! Prova ancora.

Inserisci il tuo numero: 25
Troppo basso! Prova ancora.

Inserisci il tuo numero: 37
Bravo! Hai indovinato in 3 tentativi.
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import random

numero_segreto = random.randint(1, 100)
tentativi = 0

print("Ho pensato un numero tra 1 e 100. Indovina!")

while True:
    tentativo = int(input("\nInserisci il tuo numero: "))
    tentativi += 1
    
    if tentativo == numero_segreto:
        print(f"Bravo! Hai indovinato in {tentativi} tentativi.")
        break
    elif tentativo > numero_segreto:
        print("Troppo alto! Prova ancora.")
    else:
        print("Troppo basso! Prova ancora.")
```

</details>

## Validatore di password [stringhe + regex + condizioni | avanzato]

Crea un validatore di password che verifichi se una password rispetta i seguenti criteri:
- Almeno 8 caratteri
- Contiene almeno una lettera maiuscola
- Contiene almeno una lettera minuscola
- Contiene almeno un numero
- Contiene almeno un simbolo speciale (!@#$%^&*)
- Non contiene spazi

### Esempio

```text
Inserisci una password: Test123!

✅ Password valida!

Inserisci una password: test123

❌ Password non valida:
- Manca almeno una lettera maiuscola
- Manca almeno un simbolo speciale
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import re

def valida_password(password):
    errori = []
    
    if len(password) < 8:
        errori.append("Deve contenere almeno 8 caratteri")
    
    if not re.search(r'[A-Z]', password):
        errori.append("Manca almeno una lettera maiuscola")
    
    if not re.search(r'[a-z]', password):
        errori.append("Manca almeno una lettera minuscola")
    
    if not re.search(r'\d', password):
        errori.append("Manca almeno un numero")
    
    if not re.search(r'[!@#$%^&*]', password):
        errori.append("Manca almeno un simbolo speciale")
    
    if ' ' in password:
        errori.append("Non deve contenere spazi")
    
    return errori

password = input("Inserisci una password: ")
errori = valida_password(password)

if not errori:
    print("✅ Password valida!")
else:
    print("❌ Password non valida:")
    for errore in errori:
        print(f"- {errore}")
```

</details>

## Analizzatore di testo [dizionari + stringhe + file I/O | avanzato]

Crea un programma che analizzi un file di testo e fornisca statistiche dettagliate: parole più frequenti, lunghezza media delle parole, distribuzione delle lunghezze, ecc.

### Esempio

```text
Inserisci il nome del file: testo.txt

=== ANALISI DEL TESTO ===
Caratteri totali: 1250
Parole totali: 245
Righe totali: 15
Lunghezza media parole: 5.1

Top 5 parole più frequenti:
1. "the" (23 occorrenze)
2. "and" (18 occorrenze)
3. "of" (12 occorrenze)
4. "in" (10 occorrenze)
5. "to" (9 occorrenze)

Distribuzione lunghezza parole:
2 caratteri: ████████ (8.2%)
3 caratteri: ████████████ (12.2%)
4 caratteri: ████████████████ (16.3%)
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import re
from collections import Counter

def analizza_testo(nome_file):
    try:
        with open(nome_file, 'r', encoding='utf-8') as file:
            contenuto = file.read()
    except FileNotFoundError:
        print(f"File '{nome_file}' non trovato.")
        return
    
    # Statistiche base
    caratteri_totali = len(contenuto)
    righe_totali = contenuto.count('\n') + 1 if contenuto else 0
    
    # Estrai parole (solo lettere)
    parole = re.findall(r'\b[a-zA-Z]+\b', contenuto.lower())
    parole_totali = len(parole)
    
    if parole_totali == 0:
        print("Nessuna parola trovata nel file.")
        return
    
    lunghezza_media = sum(len(parola) for parola in parole) / parole_totali
    
    # Parole più frequenti
    contatore_parole = Counter(parole)
    top_parole = contatore_parole.most_common(5)
    
    # Distribuzione lunghezze
    lunghezze = [len(parola) for parola in parole]
    distribuzione = Counter(lunghezze)
    
    # Stampa risultati
    print(f"\n=== ANALISI DEL TESTO ===")
    print(f"Caratteri totali: {caratteri_totali}")
    print(f"Parole totali: {parole_totali}")
    print(f"Righe totali: {righe_totali}")
    print(f"Lunghezza media parole: {lunghezza_media:.1f}")
    
    print(f"\nTop 5 parole più frequenti:")
    for i, (parola, freq) in enumerate(top_parole, 1):
        print(f'{i}. "{parola}" ({freq} occorrenze)')
    
    print(f"\nDistribuzione lunghezza parole:")
    for lunghezza in sorted(distribuzione.keys()):
        freq = distribuzione[lunghezza]
        percentuale = (freq / parole_totali) * 100
        barre = '█' * int(percentuale // 2)
        print(f"{lunghezza} caratteri: {barre} ({percentuale:.1f}%)")

nome_file = input("Inserisci il nome del file: ")
analizza_testo(nome_file)
```

</details>

## Sistema di gestione inventario [classi + OOP + file JSON | avanzato]

Crea un sistema per gestire l'inventario di un negozio con persistenza dei dati in formato JSON.

### Esempio

```text
=== SISTEMA INVENTARIO ===
1. Aggiungi prodotto
2. Visualizza inventario
3. Cerca prodotto
4. Aggiorna quantità
5. Rimuovi prodotto
6. Salva ed esci
Scelta: 1

Nome prodotto: Laptop
Prezzo: 999.99
Quantità: 10
Categoria: Elettronica

Prodotto aggiunto con successo! (ID: 1)
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import json
import os
from datetime import datetime

class Prodotto:
    def __init__(self, id_prodotto, nome, prezzo, quantita, categoria):
        self.id = id_prodotto
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        self.categoria = categoria
        self.data_aggiunta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'prezzo': self.prezzo,
            'quantita': self.quantita,
            'categoria': self.categoria,
            'data_aggiunta': self.data_aggiunta
        }
    
    @classmethod
    def from_dict(cls, data):
        prodotto = cls(data['id'], data['nome'], data['prezzo'], 
                      data['quantita'], data['categoria'])
        prodotto.data_aggiunta = data['data_aggiunta']
        return prodotto

class Inventario:
    def __init__(self, file_path="inventario.json"):
        self.file_path = file_path
        self.prodotti = {}
        self.prossimo_id = 1
        self.carica_dati()
    
    def carica_dati(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    dati = json.load(file)
                    for id_str, prod_data in dati['prodotti'].items():
                        prodotto = Prodotto.from_dict(prod_data)
                        self.prodotti[int(id_str)] = prodotto
                    self.prossimo_id = dati.get('prossimo_id', 1)
            except (json.JSONDecodeError, KeyError):
                print("Errore nel caricamento del file. Creato nuovo inventario.")
    
    def salva_dati(self):
        dati = {
            'prodotti': {str(id_prod): prod.to_dict() 
                        for id_prod, prod in self.prodotti.items()},
            'prossimo_id': self.prossimo_id
        }
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(dati, file, indent=2, ensure_ascii=False)
    
    def aggiungi_prodotto(self, nome, prezzo, quantita, categoria):
        prodotto = Prodotto(self.prossimo_id, nome, prezzo, quantita, categoria)
        self.prodotti[self.prossimo_id] = prodotto
        self.prossimo_id += 1
        return prodotto.id
    
    def visualizza_inventario(self):
        if not self.prodotti:
            print("Inventario vuoto.")
            return
        
        print(f"{'ID':<4} {'Nome':<20} {'Prezzo':<10} {'Qtà':<5} {'Categoria':<15}")
        print("-" * 60)
        for prodotto in self.prodotti.values():
            print(f"{prodotto.id:<4} {prodotto.nome:<20} "
                  f"€{prodotto.prezzo:<9.2f} {prodotto.quantita:<5} "
                  f"{prodotto.categoria:<15}")
    
    def cerca_prodotto(self, termine):
        risultati = []
        for prodotto in self.prodotti.values():
            if (termine.lower() in prodotto.nome.lower() or 
                termine.lower() in prodotto.categoria.lower()):
                risultati.append(prodotto)
        return risultati

def main():
    inventario = Inventario()
    
    while True:
        print("\n=== SISTEMA INVENTARIO ===")
        print("1. Aggiungi prodotto")
        print("2. Visualizza inventario")
        print("3. Cerca prodotto")
        print("4. Aggiorna quantità")
        print("5. Rimuovi prodotto")
        print("6. Salva ed esci")
        
        scelta = input("Scelta: ")
        
        if scelta == "1":
            nome = input("Nome prodotto: ")
            prezzo = float(input("Prezzo: "))
            quantita = int(input("Quantità: "))
            categoria = input("Categoria: ")
            
            id_prodotto = inventario.aggiungi_prodotto(nome, prezzo, quantita, categoria)
            print(f"Prodotto aggiunto con successo! (ID: {id_prodotto})")
        
        elif scelta == "2":
            inventario.visualizza_inventario()
        
        elif scelta == "3":
            termine = input("Termine di ricerca: ")
            risultati = inventario.cerca_prodotto(termine)
            if risultati:
                for prodotto in risultati:
                    print(f"ID: {prodotto.id}, Nome: {prodotto.nome}, "
                          f"Prezzo: €{prodotto.prezzo:.2f}")
            else:
                print("Nessun risultato trovato.")
        
        elif scelta == "6":
            inventario.salva_dati()
            print("Dati salvati. Arrivederci!")
            break

if __name__ == "__main__":
    main()
```

</details>

## Mini calcolatrice con cronologia [funzioni + liste + persistenza | avanzato]

Crea una calcolatrice che supporti operazioni base, mantenga una cronologia delle operazioni e possa salvare/caricare la cronologia da file.

### Esempio

```text
=== CALCOLATRICE AVANZATA ===
1. Addizione
2. Sottrazione
3. Moltiplicazione
4. Divisione
5. Potenza
6. Mostra cronologia
7. Salva cronologia
8. Carica cronologia
9. Cancella cronologia
0. Esci
Scelta: 1

Primo numero: 15
Secondo numero: 7
Risultato: 15 + 7 = 22

Scelta: 6
=== CRONOLOGIA ===
1. 15 + 7 = 22
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
import json
import os
from datetime import datetime

class Calcolatrice:
    def __init__(self):
        self.cronologia = []
        self.operazioni = {
            1: ('+', self.addizione),
            2: ('-', self.sottrazione),
            3: ('×', self.moltiplicazione),
            4: ('÷', self.divisione),
            5: ('^', self.potenza)
        }
    
    def addizione(self, a, b):
        return a + b
    
    def sottrazione(self, a, b):
        return a - b
    
    def moltiplicazione(self, a, b):
        return a * b
    
    def divisione(self, a, b):
        if b == 0:
            raise ValueError("Divisione per zero non permessa")
        return a / b
    
    def potenza(self, a, b):
        return a ** b
    
    def esegui_operazione(self, tipo_op):
        try:
            a = float(input("Primo numero: "))
            b = float(input("Secondo numero: "))
            
            simbolo, funzione = self.operazioni[tipo_op]
            risultato = funzione(a, b)
            
            # Formatta i numeri per rimuovere .0 se interi
            a_str = str(int(a)) if a.is_integer() else str(a)
            b_str = str(int(b)) if b.is_integer() else str(b)
            ris_str = str(int(risultato)) if isinstance(risultato, float) and risultato.is_integer() else str(risultato)
            
            operazione = f"{a_str} {simbolo} {b_str} = {ris_str}"
            self.cronologia.append({
                'operazione': operazione,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            print(f"Risultato: {operazione}")
            
        except ValueError as e:
            print(f"Errore: {e}")
        except Exception as e:
            print(f"Errore imprevisto: {e}")
    
    def mostra_cronologia(self):
        if not self.cronologia:
            print("Cronologia vuota.")
            return
        
        print("\n=== CRONOLOGIA ===")
        for i, entry in enumerate(self.cronologia, 1):
            print(f"{i}. {entry['operazione']} ({entry['timestamp']})")
    
    def salva_cronologia(self):
        nome_file = input("Nome file (default: cronologia.json): ").strip()
        if not nome_file:
            nome_file = "cronologia.json"
        
        try:
            with open(nome_file, 'w', encoding='utf-8') as file:
                json.dump(self.cronologia, file, indent=2, ensure_ascii=False)
            print(f"Cronologia salvata in {nome_file}")
        except Exception as e:
            print(f"Errore nel salvataggio: {e}")
    
    def carica_cronologia(self):
        nome_file = input("Nome file da caricare: ").strip()
        
        try:
            with open(nome_file, 'r', encoding='utf-8') as file:
                self.cronologia = json.load(file)
            print(f"Cronologia caricata da {nome_file}")
        except FileNotFoundError:
            print("File non trovato.")
        except Exception as e:
            print(f"Errore nel caricamento: {e}")
    
    def cancella_cronologia(self):
        conferma = input("Sei sicuro di voler cancellare la cronologia? (s/n): ")
        if conferma.lower() == 's':
            self.cronologia.clear()
            print("Cronologia cancellata.")

def main():
    calc = Calcolatrice()
    
    while True:
        print("\n=== CALCOLATRICE AVANZATA ===")
        print("1. Addizione")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("5. Potenza")
        print("6. Mostra cronologia")
        print("7. Salva cronologia")
        print("8. Carica cronologia")
        print("9. Cancella cronologia")
        print("0. Esci")
        
        try:
            scelta = int(input("Scelta: "))
            
            if scelta == 0:
                print("Arrivederci!")
                break
            elif 1 <= scelta <= 5:
                calc.esegui_operazione(scelta)
            elif scelta == 6:
                calc.mostra_cronologia()
            elif scelta == 7:
                calc.salva_cronologia()
            elif scelta == 8:
                calc.carica_cronologia()
            elif scelta == 9:
                calc.cancella_cronologia()
            else:
                print("Scelta non valida.")
                
        except ValueError:
            print("Inserisci un numero valido.")

if __name__ == "__main__":
    main()
```

</details>

## Cifrario di Cesare con chiave variabile [stringhe + crittografia + ASCII | avanzato]

Implementa un cifrario di Cesare che può cifrare/decifrare testo con diversi spostamenti e supporta caratteri speciali.

### Esempio

```text
=== CIFRARIO DI CESARE ===
1. Cifra testo
2. Decifra testo
3. Forza bruta (prova tutte le chiavi)
4. Esci
Scelta: 1

Testo da cifrare: Ciao Mondo!
Chiave (spostamento): 3
Includi caratteri speciali? (s/n): s

Testo cifrato: Fldр Prqgr!

Scelta: 3
Testo da decifrare: Fldр Prqgr!

=== FORZA BRUTA ===
Chiave  0: Fldр Prqgr!
Chiave  1: Ekcp Oqpfq!
Chiave  2: Djbo Npoep!
Chiave  3: Ciao Mondo!  ← Possibile match!
```

### Soluzione

<details>
<summary>✅ Mostra soluzione</summary>

```python
class CifrarioCesare:
    def __init__(self):
        # Alfabeti per diversi set di caratteri
        self.alfabeto_base = 'abcdefghijklmnopqrstuvwxyz'
        self.alfabeto_completo = (
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789 .,!?;:-_()[]{}@#$%^&*+=<>/\\|`~"\''
        )
    
    def cifra_carattere(self, char, chiave, alfabeto):
        if char not in alfabeto:
            return char
        
        indice_originale = alfabeto.index(char)
        nuovo_indice = (indice_originale + chiave) % len(alfabeto)
        return alfabeto[nuovo_indice]
    
    def decifra_carattere(self, char, chiave, alfabeto):
        return self.cifra_carattere(char, -chiave, alfabeto)
    
    def cifra_testo(self, testo, chiave, includi_speciali=False):
        alfabeto = self.alfabeto_completo if includi_speciali else self.alfabeto_base
        
        risultato = []
        for char in testo:
            if not includi_speciali and char.isupper():
                # Mantieni maiuscole separate
                char_lower = char.lower()
                if char_lower in self.alfabeto_base:
                    cifrato = self.cifra_carattere(char_lower, chiave, self.alfabeto_base)
                    risultato.append(cifrato.upper())
                else:
                    risultato.append(char)
            else:
                risultato.append(self.cifra_carattere(char, chiave, alfabeto))
        
        return ''.join(risultato)
    
    def decifra_testo(self, testo, chiave, includi_speciali=False):
        return self.cifra_testo(testo, -chiave, includi_speciali)
    
    def forza_bruta(self, testo, includi_speciali=False):
        alfabeto = self.alfabeto_completo if includi_speciali else self.alfabeto_base
        risultati = []
        
        for chiave in range(len(alfabeto)):
            decifrato = self.decifra_testo(testo, chiave, includi_speciali)
            
            # Euristica semplice per identificare testo italiano
            parole_comuni = ['il', 'di', 'che', 'e', 'la', 'il', 'un', 'a', 'per', 'non', 'una', 'in', 'con', 'è', 'da', 'su', 'del', 'al', 'le']
            score = sum(1 for parola in parole_comuni if parola in decifrato.lower())
            
            risultati.append((chiave, decifrato, score))
        
        return risultati
    
    def analizza_frequenze(self, testo):
        """Analizza la frequenza dei caratteri per aiutare nella decrittazione"""
        from collections import Counter
        
        # Frequenze tipiche in italiano (lettere più comuni)
        # Source: https://it.wikipedia.org/wiki/Analisi_delle_frequenze?oldformat=true
        freq_italiane = {
            a: 11.74,
            b: 0.92,
            c: 4.50,
            d: 3.73,
            e: 11.79,
            f: 0.95,
            g: 1.64,
            h: 1.54,
            i: 11.28,
            l: 6.51,
            m: 2.51,
            n: 6.88,
            o: 9.83,
            p: 3.05,
            q: 0.51,
            r: 6.37,
            s: 4.98,
            t: 5.62,
            u: 3.01,
            v: 2.10,
            z: 0.49,
        }
        
        conteggio = Counter(char.lower() for char in testo if char.isalpha())
        lunghezza = sum(conteggio.values())
        
        if lunghezza == 0:
            return {}
        
        freq_testo = {char: (count / lunghezza) * 100 for char, count in conteggio.items()}
        return freq_testo

def main():
    cifrario = CifrarioCesare()
    
    while True:
        print("\n=== CIFRARIO DI CESARE ===")
        print("1. Cifra testo")
        print("2. Decifra testo")
        print("3. Forza bruta (prova tutte le chiavi)")
        print("4. Analizza frequenze")
        print("5. Esci")
        
        try:
            scelta = int(input("Scelta: "))
            
            if scelta == 5:
                print("Arrivederci!")
                break
            
            elif scelta == 1:
                testo = input("\nTesto da cifrare: ")
                chiave = int(input("Chiave (spostamento): "))
                speciali = input("Includi caratteri speciali? (s/n): ").lower() == 's'
                
                risultato = cifrario.cifra_testo(testo, chiave, speciali)
                print(f"\nTesto cifrato: {risultato}")
            
            elif scelta == 2:
                testo = input("\nTesto da decifrare: ")
                chiave = int(input("Chiave (spostamento): "))
                speciali = input("Includi caratteri speciali? (s/n): ").lower() == 's'
                
                risultato = cifrario.decifra_testo(testo, chiave, speciali)
                print(f"\nTesto decifrato: {risultato}")
            
            elif scelta == 3:
                testo = input("\nTesto da decifrare: ")
                speciali = input("Includi caratteri speciali? (s/n): ").lower() == 's'
                
                risultati = cifrario.forza_bruta(testo, speciali)
                
                print("\n=== FORZA BRUTA ===")
                for chiave, decifrato, score in risultati[:26]:  # Mostra solo prime 26
                    marker = "  ← Possibile match!" if score >= 2 else ""
                    print(f"Chiave {chiave:2d}: {decifrato[:50]}{'...' if len(decifrato) > 50 else ''}{marker}")
            
            elif scelta == 4:
                testo = input("\nTesto da analizzare: ")
                frequenze = cifrario.analizza_frequenze(testo)
                
                print("\n=== ANALISI FREQUENZE ===")
                for char, freq in sorted(frequenze.items(), key=lambda x: x[1], reverse=True)[:10]:
                    print(f"'{char}': {freq:.2f}%")
            
            else:
                print("Scelta non valida.")
                
        except ValueError:
            print("Inserisci un numero valido.")
        except Exception as e:
            print(f"Errore: {e}")

if __name__ == "__main__":
    main()
```

</details>
