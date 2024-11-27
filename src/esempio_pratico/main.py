from fabric import Connection

if __name__ == "__main__":
    username = "salvaranil" #input("Inserisci il tuo username: ")
    password = "salvaranil" #input("Inserisci la tua password: ")

    ssh_connection = Connection("192.168.0.50", user=username, port=2222, connect_kwargs={"password": password})
    result = ssh_connection.run("lsof -i", hide=True)

    print(result.stdout.strip())