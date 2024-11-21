import socket
import threading

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

blocco = threading.Lock()

rubrica_telefonica = {
    "Mario Rossi": "123-456-7890",
    "Luca Bianchi": "234-567-8901",
    "Giulia Verdi": "345-678-9012",
    "Elena Neri": "456-789-0123",
    "Roberto Russo": "567-890-1234"
}

class ClientHandler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.isRunning = True
        
    def run(self):  
        global rubrica_telefonica
        while self.isRunning:
            data = self.connection.recv(BUFFER_SIZE).decode()
            comando, param = data.split('|')
                
            if comando == "Cerca-numero":
                if nome in rubrica_telefonica:
                    numero_telefono = rubrica_telefonica[nome]
                    self.connection.sendall(f"Il numero associato a {nome} è {numero_telefono}\n".encode())
                else:
                    self.connection.sendall("Nome non trovato\n".encode())
                    
            elif comando == "Cerca-nome":
                nome = (k for k, v in rubrica_telefonica if v == numero)
                if nome:
                    self.connection.sendall(f"Il nome associato al numero {numero} è {nome}\n".encode())
                else:
                    self.connection.sendall("Numero di telefono non trovato\n".encode())
            
            elif comando == "Aggiungi-contatto":
                nome, numero = param.split(';')
                rubrica_telefonica[nome.strip()] = numero.strip()
                self.connection.sendall("Ok".encode())
            else:
                self.connection.sendall("Comando sconosciuto\n".encode())
        
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
