'''
Progettare in python 
- un server TCP che quando viene eseguito sorteggia un numero intero casuale tra 1 e 100
- al server si connettono almeno due client
- gli utenti tramite i client inviano al server un nuemro tentando di indovinare il nuemro casuale scelto dal server
-il server risponde ai client nei modi seguenti:
    * "HAI VINTO" se il client ha indovinato
    * "TROPPO BASSO" se il numero del client è minore
    * "TROPPO ALTRO" se il nuemro del client è maggiore
- quando un client vince viene comunqicato a gli altri con "HAI PERSO"

Usare una lock nel punto critico: controllo del numero
'''
# Server
import socket
import random
import threading

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

blocco = threading.Lock()
numero_casuale = random.randint(1,100)
partita = True

class ClientHandler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.isRunning = True
        
    def run(self):  
        while self.isRunning:
            global partita
            data = self.connection.recv(BUFFER_SIZE).decode()
            numero_client = int(data)
            
            blocco.acquire()
            if partita:
                if numero_client == numero_casuale:
                    self.connection.sendall("HAI VINTO\n".encode())
                    partita = False
                    self.isRunning = False
                elif numero_client < numero_casuale:
                    self.connection.sendall("TROPPO BASSO\n".encode())
                else:
                    self.connection.sendall("TROPPO ALTO\n".encode())
            else:
                self.isRunning = False
                self.connection.sendall("HAI PERSO\n".encode())
            blocco.release()
            
        self.connection.close()
                   
def main(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, _ = s.accept()
        thread = ClientHandler(connection)
        thread.start()
 
if __name__ == "__main__":
    main()