#CLIENT
import socket
import time
import datetime

HOST_SERVER = "127.0.0.1"
PORTA_SERVER = 9090

#configurazione stazione
ID_STAZIONE = 2
FIUME = "Gesso"
LOCALITA = "Bandito"
LIVELLO_GUARDIA = 2.9

#connessione al server
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((HOST_SERVER, PORTA_SERVER))
print(f"Connesso al server {HOST_SERVER} : {PORTA_SERVER}")

#funzione per inviare i dati al server
def invia_dati(livello):
    data_ora = datetime.datetime.now()
    messaggio = f"{ID_STAZIONE},{FIUME},{LOCALITA},{livello},{data_ora}"
    socket_client.sendall(messaggio.encode())
    
    #riceve risposta dal server
    risposta = socket_client.recv(1024).decode()
    print(f"risposta dal server:{risposta}")

#inviare dati ogni 15 secondi
def invia_in_loop():
    while True:
        livello = float(input("inserire livello acqua in metri: "))
        invia_dati(livello)
        time.sleep(15)  # Attende 15 secondi prima di inviare i dati successivi

invia_in_loop()

#chiusura connessione
socket_client.close()

