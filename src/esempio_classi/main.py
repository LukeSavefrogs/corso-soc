""" Autoscuola che deve gestire le prenotazioni degli esami di guida. 

- Aggiungere prenotazioni
- Rimuovere prenotazioni
- Visualizzare le prenotazioni
"""
import registro_prenotazioni

if __name__ == "__main__":
    registro_prenotazioni = registro_prenotazioni.RegistroPrenotazioni()
    registro_prenotazioni.aggiungi_prenotazione("2021-01-01 10:00", "Pippo Rossi", "Pippo Bianchi")
    registro_prenotazioni.aggiungi_prenotazione("2021-01-01 10:30", "Pippo Verdi", "Pippo Bianchi")

    print(registro_prenotazioni)

    registro_prenotazioni.aggiungi_prenotazione(
        "2021-01-01 11:00",
        "Pippo Neri",
        "Pippo Bianchi"
    )

    print(registro_prenotazioni)