#fare 2 server che comunicano tra loro con i socket, programma server e client
#SERVER
import socket

MY_ADRESS = ("192.168.1.118", 9000)  #indirizzo che identifica il processo server, indirizzo della scheda di loopback + porta (9000)
BUFFER_SIZE = 4096 #BYTE
NICKNAME = "Risso"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #istanza della classe socket
s.bind(MY_ADRESS) #lega il socket all'indirizzo


while True:
    data, sender_adress = s.recvfrom(BUFFER_SIZE) #ritorna i dati e l'indirizzo (riceve dei dati e mi dice anche chi li ha mandati)
    stringa = data.decode() #trasforma la stringa in una vera stringa
    print(f"ricevuto {data} da {sender_adress}")
    if stringa == "EXIT":
        break




