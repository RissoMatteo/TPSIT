import socket
import threading

# Configurazione del server
HOST = '127.0.0.1'  # Indirizzo IP del server (localhost)
PORTA = 65432       # Porta su cui il server ascolta

# Creazione del socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((HOST, PORTA))  # Associa l'indirizzo IP e la porta
socket_server.listen()  # Inizia ad ascoltare le connessioni
print(f"Server in ascolto su {HOST}:{PORTA}...")

# Funzione per gestire un singolo client
def gestisci_client(conn, addr):
    print(f"[NUOVA CONNESSIONE] {addr} connesso.")
    while True:
        data = conn.recv(1024)  # Riceve dati dal client
        if not data:
            break  # Interrompe la connessione se il client chiude
        print(f"[MESSAGGIO da {addr}] {data.decode()}")
        conn.sendall(data)  # Invia indietro i dati ricevuti (echo)
    
    conn.close()  # Chiude la connessione
    print(f"[CONNESSIONE CHIUSA] {addr} disconnesso.")

# Loop principale del server
while True:
    conn, addr = socket_server.accept()  # Accetta una nuova connessione
    # Creazione di un thread per gestire il client
    thread_client = threading.Thread(gestisci_client, (conn, addr))
    thread_client.start()

# Chiusura del server (non verrà mai raggiunto in questo esempio)
socket_server.close()
