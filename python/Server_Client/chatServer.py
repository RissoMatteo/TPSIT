import csv
import socket

MY_ADDRESS = ("0.0.0.0", 9000)
BUFFER_SIZE = 4096

def leggi_rubrica(file):
    rubrica = {}
    with open(file, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                nickname, ip_address = row
                rubrica[nickname] = ip_address
    return rubrica

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    rubrica = leggi_rubrica("rubrica.csv")

    while True:
        data, sender_address = s.recvfrom(BUFFER_SIZE)
        print("Messaggio ricevuto da:", sender_address)
        elementMessage = data.decode().split("|")
        
        if len(elementMessage) == 3:
            message, destinatario_nickname, porta_destinatario = elementMessage
            if destinatario_nickname in rubrica:
                destinatario_address = rubrica[destinatario_nickname]
                try:
                    s.sendto(message.encode(), (destinatario_address, int(porta_destinatario)))
                    print(f"Mando a {destinatario_nickname} ({destinatario_address}:{porta_destinatario}) il messaggio: {message} da parte di {sender_address}")
                except:
                    print(f"Errore durante l'invio a {destinatario_nickname}")
            else:
                print(f"Destinatario {destinatario_nickname} non trovato nella rubrica")
        else:
            print("Errore: formato del messaggio non valido")
            print(data.decode())

if __name__ == "__main__":
    main()
