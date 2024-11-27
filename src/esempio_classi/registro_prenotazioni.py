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

class RegistroPrenotazioni:
    def __init__(self):
        self.prenotazioni = []

    def aggiungi_prenotazione(self, data_ora, cliente, istruttore):
        prenotazione = Prenotazione(data_ora, cliente, istruttore)
        self.prenotazioni.append(prenotazione)

    def rimuovi_prenotazione(self, id):
        self.prenotazioni = [
            prenotazione 
            for prenotazione in self.prenotazioni 
            if prenotazione.id != id
        ]
    
    def __iter__(self):
        return iter(self.prenotazioni)
    
    def __str__(self):
        return "Prenotazioni: \n" + "\n".join([
            f"\t{prenotazione.data_ora} - {prenotazione.cliente} - {prenotazione.istruttore}"
            for prenotazione in self.prenotazioni
        ])
