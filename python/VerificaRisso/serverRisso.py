#SERVER
import socket
import threading
import sqlite3

IP = "127.0.0.1"
PORTA = 9090

#creazione socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((IP, PORTA))
socket_server.listen()
print(f"Server in ascolto su {IP}:  {PORTA}")

#connessione database
conn_db = sqlite3.connect("fiumi.db")
cur = conn_db.cursor()

#gestistione client
def gestisci_client(conn, addr):
    print(addr)
    while True:
        data = conn.recv(1024) #riceve
        if not data:
            break
        messaggio = data.decode()
        id_stazione, fiume, localita, livello, data_ora = messaggio.split(',')
        livello = float(livello)
        
        #salvataggio dei dati nel database
        cur.execute('''
        INSERT INTO livelli (id_stazione, fiume, localita, livello) 
        VALUES (?, ?, ?, ?)
        ''', (id_stazione, fiume, localita, livello))
        conn_db.commit()
        
        #controllo livello e invio risposta
        risposta = ""
        if livello >= 0.7 * 3.0:
            risposta = "attivare sirena luminosa"
            print(f"pericolo{fiume},{localita},{data_ora} Livello:{livello}")
        elif livello >= 0.3 * 3.0:
            risposta = "pericolo imminente"
            print(f"avviso{fiume},{localita},{data_ora} Livello:{livello}")

        conn.sendall(risposta.encode()) 
    conn.close()
    print("connessione chiusa")

while True:
    conn, addr = socket_server.accept()
    thread_client = threading.Thread(target=gestisci_client,args=(conn, addr))
    thread_client.start()




