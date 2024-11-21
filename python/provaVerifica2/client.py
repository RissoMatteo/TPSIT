import socket
import sqlite3

# Configurazione rete da scansionare
RIP = "192.168.0."
INIZIO_IP = 0
FINE_IP = 31
PORTE_COMUNI = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389]  # Porte comuni

# Configurazione client-server
HOST_SERVER = '127.0.0.1'
PORTA_SERVER = 65432

# Connessione al server
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((HOST_SERVER, PORTA_SERVER))
print(f"Connesso al server {HOST_SERVER}:{PORTA_SERVER}")

# Creazione del database locale
conn_db = sqlite3.connect('ip_lista.db')  # Crea o apre il database
cur = conn_db.cursor()

# Creazione della tabella
cur.execute('''
CREATE TABLE IF NOT EXISTS scansione_ip (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_host TEXT,
    nome_host TEXT,
    lista_porte TEXT
)
''')
conn_db.commit()

# Funzione per scansionare un host
def scansiona_host(ip):
    porte_aperte = []
    nome_host = socket.gethostbyaddr(ip)[0]  # Ottieni il nome dell'host

    for porta in PORTE_COMUNI:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        risultato = sock.connect_ex((ip, porta))
        if risultato == 0:  # Porta aperta
            porte_aperte.append(porta)
        sock.close()

    # Salva nel database
    cur.execute('INSERT INTO scansione_ip (ip_host, nome_host, lista_porte) VALUES (?, ?, ?)', 
                (ip, nome_host, ', '.join(map(str, porte_aperte))))
    conn_db.commit()
    
    return ip, nome_host, porte_aperte

# Funzione per visualizzare i risultati dal database
def mostra_risultati():
    query = "SELECT * FROM scansione_ip;"
    cur.execute(query)
    risultati = cur.fetchall()
    print(f"Risultati salvati nel database:")
    for riga in risultati:
        print(riga)

# Funzione per inviare i risultati al server
def invia_risultati_server():
    query = "SELECT * FROM scansione_ip;"
    cur.execute(query)
    risultati = cur.fetchall()
    messaggio = f"Risultati della scansione:\n{risultati}"
    socket_client.sendall(messaggio.encode())

    # Ricezione della risposta dal server
    risposta = socket_client.recv(1024).decode()
    print(f"Risposta dal server: {risposta}")

# Funzione per scansionare la rete
def scansiona_rete():
    print("Inizio scansione della rete...")
    for i in range(INIZIO_IP, FINE_IP + 1):
        ip_address = f"{RIP}{i}"
        print(f"Scansione di {ip_address}...")
        ip, nome_host, porte = scansiona_host(ip_address)
        print(f"Host: {ip}, Nome: {nome_host}, Porte Aperte: {porte}")
    print("Scansione completata. Risultati salvati nel database.")

# Funzione per il menu
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Scansiona la rete")
        print("2. Mostra i risultati salvati nel database")
        print("3. Invia i risultati al server")
        print("4. Esci")
        
        scelta = input("Scegli un'opzione (1-4): ")
        
        if scelta == '1':
            scansiona_rete()
        elif scelta == '2':
            mostra_risultati()
        elif scelta == '3':
            invia_risultati_server()
        elif scelta == '4':
            print("Uscita in corso...")
            break

# Avvio del menu
menu()

# Chiusura delle connessioni
socket_client.close()
conn_db.close()
print("Connessione chiusa.")
