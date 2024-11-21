#fare 2 server che comunicano tra loro con i socket, programma server e client

import socket

SERVER_ADRESS = ("127.0.0.1", 9000)  #indirizzo del server
BUFFER_SIZE = 4096 #BYTE

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

while True:
    string = input("->")
    binary_string = string.encode()
    s.sendto(binary_string, SERVER_ADRESS)
    data, sender_adress = s.recvfrom(BUFFER_SIZE)
    string = data.decode()
    print(f"ricevuto {data} da {sender_adress}")
    
    if string == "EXIT":
        break


    



