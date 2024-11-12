# Beginner Python for SOC crash course

Questo repository contiene il materiale utilizzato per il corso accelerato di Python SOC il 14/11/2024.

> [!WARNING]
> Questo non deve in alcun modo essere preso come un approccio serio alla CyberSecurity, ma piuttosto come un'*introduzione per principianti* al **potenziale** rappresentato dal conoscere Python in un contesto SOC.

## Obbiettivi

1. Analizza e genera un report per le seguenti vulnerabilità:
   - porte aperte (`lsof -i`)
   - troppi tentativi di accesso (`lastb --fullnames --time-format iso --dns`)
   - utenze bloccate/scadute
2. Lettura di un file CSV contenente una lista di hostname/porta e controllare che siano aperte
