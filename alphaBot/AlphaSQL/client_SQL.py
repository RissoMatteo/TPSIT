import socket
import time
from pynput import keyboard

# Configurazione del server (indirizzo IP e porta)
INDIRIZZO_SERVER = ("192.168.1.145", 9000)
DIM_BUFFER = 4096

# Creazione del socket per la comunicazione con il server
connessione = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connessione.connect(INDIRIZZO_SERVER)  # Connessione al server

# Variabile per tenere traccia dell'ultimo tasto inviato
comando_precedente = None

def gestione_pressione(tasto):
    """Gestisce la pressione dei tasti inviando il comando in minuscolo"""

    global comando_precedente

    # Invia il carattere solo se è diverso dal precedente
    try:
        if tasto.char != comando_precedente:
            connessione.sendall(tasto.char.lower().encode())
            comando_precedente = tasto.char
            time.sleep(0.05)  # Breve pausa per limitare l'invio eccessivo di comandi
    except AttributeError:
        pass  # Ignora tasti speciali che non hanno attributo 'char'

def gestione_rilascio(tasto):
    """Gestisce il rilascio dei tasti inviando il comando in maiuscolo"""

    global comando_precedente

    # Reset del comando precedente e invio in maiuscolo
    try:
        comando_precedente = None
        connessione.sendall(tasto.char.upper().encode())
        time.sleep(0.05)
    except AttributeError:
        pass  # Ignora tasti speciali che non hanno attributo 'char'

def avvia_ascolto():
    """Inizia il listener per monitorare pressione e rilascio dei tasti"""

    with keyboard.Listener(on_press=gestione_pressione, on_release=gestione_rilascio) as ascoltatore:
        ascoltatore.join()

def avvio_principale():
    """Avvia il listener e gestisce la chiusura del socket in caso di errore"""

    try:
        avvia_ascolto()
    except KeyError:
        connessione.close()

if __name__ == "__main__":
    avvio_principale()
