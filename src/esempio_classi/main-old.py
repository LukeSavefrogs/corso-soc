""" Autoscuola che deve gestire le prenotazioni degli esami di guida. 

- Aggiungere prenotazioni
- Rimuovere prenotazioni
- Visualizzare le prenotazioni
"""
import uuid

class Prenotazione:
    id: str = ""
    data_ora: str = ""
    cliente: str = ""
    istruttore: str = ""

    def __init__(self, data_ora, cliente, istruttore, id=None):
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.data_ora = data_ora
        self.cliente = cliente
        self.istruttore = istruttore

def aggiungi_prenotazione(registro_prenotazioni, data_ora, cliente, istruttore):
    prenotazione = Prenotazione(data_ora, cliente, istruttore)
    registro_prenotazioni.append(prenotazione)

def rimuovi_prenotazione(registro_prenotazioni, id):
    for prenotazione in registro_prenotazioni:
        if prenotazione.id == id:
            registro_prenotazioni.remove(prenotazione)
            return
        
    print("Prenotazione non trovata")

def visualizza_prenotazioni(registro_prenotazioni):
    print("Prenotazioni:")
    for prenotazione in registro_prenotazioni:
        print(f"{prenotazione.data_ora} - {prenotazione.cliente} - {prenotazione.istruttore}")
        
if __name__ == "__main__":
    registro_prenotazioni = [
        Prenotazione("2021-01-01 10:00", "Mario Rossi", "Luigi Bianchi"),
        Prenotazione("2021-01-01 10:30", "Giuseppe Verdi", "Luigi Bianchi"),
    ]
    visualizza_prenotazioni(registro_prenotazioni)

    aggiungi_prenotazione(
        registro_prenotazioni,
        "2021-01-01 11:00",
        "Paolo Neri",
        "Luigi Bianchi"
    )

    visualizza_prenotazioni(registro_prenotazioni)