<!-- omit from toc -->
# Esercitazioni generali

- [Verifica età](#verifica-età)
  - [Esempio](#esempio)
  - [Soluzione](#soluzione)
- [Elenco dei primi N numeri pari](#elenco-dei-primi-n-numeri-pari)
  - [Esempio](#esempio-1)
  - [Soluzione](#soluzione-1)
  - [BONUS 1](#bonus-1)
    - [Esempio](#esempio-2)
  - [BONUS 2](#bonus-2)
    - [Esempio](#esempio-3)

## Verifica età

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
<summary>Mostra soluzione</summary>

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

## Elenco dei primi N numeri pari

Dato in ingresso un numero N, stampare i primi N numeri pari.

### Esempio

```text
Inserisci un numero: 5

I primi 5 numeri pari sono:
0
2
4
6
8
```

### Soluzione

<details>
<summary>Mostra soluzione</summary>

```python
n = int(input("Inserisci un numero: "))
print(f"I primi {n} numeri pari sono:")

def is_even(num):
    return num % 2 == 0

even_numbers = [i for i in range(n * 2) if is_even(i)]
for number in even_numbers[:n]:
    print(number)
```

</details>

### BONUS 1

Chiedi se si vuole stampare i numeri pari o dispari e stampa i primi N numeri di quel tipo.

#### Esempio

```text
Inserisci un numero: 5

Vuoi stampare i numeri pari o dispari? pari

I primi 5 numeri pari sono:
0
2
4
6
8
```

### BONUS 2

Se l'utente inserisce un valore invalido (es. un numero negativo o non numerico, oppure nel caso della seconda domanda un valore diverso da "pari" o "dispari"), il programma deve chiedere nuovamente l'input fino a quando non viene inserito un valore valido.

#### Esempio

```text
Inserisci un numero: -3

VALORE INVALIDO: Riprovare.
Inserisci un numero: 5

Vuoi stampare i numeri pari o dispari? sbagliato

VALORE INVALIDO: Riprovare.
Vuoi stampare i numeri pari o dispari? pari

I primi 5 numeri pari sono:
0
2
4
6
8
```
