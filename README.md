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

## Connessione al server

1. Installa le estensioni consigliate, in particolare:
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
   - [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
   - [Tabstop Whitespace Converter](https://marketplace.visualstudio.com/items?itemName=johnnywong.vscode-ts-whitespace-converter)

2. Installa un client OpenSSH:
   - [Git for Windows](https://git-scm.com/downloads/win)
   - [Windows OpenSSH Client](https://learn.microsoft.com/it-it/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui&pivots=windows-server-2019#install-openssh-for-windows-server)

3. Aggiungi il server alla lista di host:
   1. Apri il "Riquadro Comandi" (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd> o <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> a seconda dei binding)
   2. Digita "Remote-SSH: Add new SSH Host" e dai <kbd>Invio</kbd>
   3. Quando richiesto inserisci la seguente stringa sostituendo a `SERVER_USERNAME` e `SERVER_IP` i valori corretti:
      ```shell
      ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no {SERVER_USERNAME}@{SERVER_IP} -p 2222
      ```
   4. Seleziona il file di configurazione nella tua home:
      ![alt text](./docs/images/ssh-config-file.png)

4. Connettiti all'host remoto:
   1. Apri il "Riquadro Comandi" (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd> o <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> a seconda dei binding)
   2. Digita "Remote-SSH: Connetti la finestra corrente all'host..." e dai <kbd>Invio</kbd>
   3. Seleziona l'host creato al punto 3 (con il nome corrispondente a `SERVER_IP`)
   4. Inserisci la password

5. Installa nell'host remoto le estensioni locali:
   1. Clicca sul tasto "Estensioni" dalla barra laterale sinistra
   2. Clicca al pulsante download alla destra della sezione "SSH - {ip_address} - INSTALLATE"
   ![alt text](./docs/images/download-estensioni-remote.png)

6. Seleziona l'interprete Python remoto:
   1. Apri il "Riquadro Comandi" (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd> o <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> a seconda dei binding)
   2. Digita "Python: Select Interpreter" e dai <kbd>Invio</kbd>
   3. Seleziona "Python 3.12.3" come da immagine:
   ![alt text](./docs/images/selezione-interprete.png)

7. Sei pronto!