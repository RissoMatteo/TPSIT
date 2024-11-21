import socket
import random

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

n = 3

def main():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    trovata = False
    while True:
        if(trovata == False):
            lettere = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
            parola_casuale = ''.join(random.choice(lettere) for _ in range(n))
            s.sendall(parola_casuale.encode())
            message=s.recv(BUFFER_SIZE)
            print(f"ricevuto dal server: {message.decode()}")
        
    s.close()

if __name__ == "__main__":
    main()