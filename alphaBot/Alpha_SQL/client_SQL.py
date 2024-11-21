import socket
import time
from pynput import keyboard

# Indirizzo IP e porta dell'Alphabot a cui ci connettiamo
SERVER_ADDRESS = ("192.168.1.145", 9000)
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Creazione del socket TCP per la comunicazione con il server
s.connect(SERVER_ADDRESS)   # Connessione al server

ultimo_comando = None # Variabile globale per tenere traccia dell'ultimo comando inviato

def on_press(key):  #gestisce la pressione di un tasto
    global ultimo_comando
    if key.char != ultimo_comando:  # Controlla se il tasto corrente è diverso dall'ultimo comando inviato e fa parte dei comandi
        s.sendall(key.char.lower().encode())   # Invia il tasto in minuscolo al server per indicare la pressione
        ultimo_comando = key.char   # Aggiorna l'ultimo comando inviato
        time.sleep(0.05)     # Pausa per evitare di sovraccaricare la rete con troppi comandi consecutivi

def on_release(key): #gestisce il rilascio di un tasto
    global ultimo_comando     
    ultimo_comando = None   # Resetta l'ultimo comando inviato
    s.sendall(key.char.upper().encode())     # Invia il tasto in maiuscolo al server per indicare il rilascio  
    time.sleep(0.05)

def start_listener(): #avvia l' ascolto della tastiera
    # listener per monitorare la pressione e il rilascio dei tasti
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def main():
    start_listener()    # Avvia il listener della tastiera
    if KeyError:     # Se si verifica un'eccezione KeyError (non gestito), chiude il socket
        s.close()

if __name__ == "__main__":
    main()
