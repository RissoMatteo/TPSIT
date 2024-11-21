import socket
import threading
import random

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

blocco = threading.Lock()
partita = True
password_segreta = "abc"
print(f"La password segreta è: {password_segreta}")  # Per debug

class ClientHandler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.isRunning = True

    def run(self):
        while self.isRunning:
            global partita
            data = self.connection.recv(BUFFER_SIZE).decode()
            password_client = data.strip()
            
            blocco.acquire()
            if partita:
                if password_client == password_segreta:
                    self.connection.sendall("PASSWORD INDOVINATA!\n".encode())
                    partita = False
                    self.isRunning = False
                else:
                    self.connection.sendall("PASSWORD ERRATA!\n".encode())
            else:
                self.isRunning = False
                self.connection.sendall("PASSWORD GIA' INDOVINATA!\n".encode())
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