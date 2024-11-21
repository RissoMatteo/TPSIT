#fare 2 server che comunicano tra loro con i socket, programma server e client
#CLIENT
import socket

SERVER_ADRESS = ("127.0.0.1", 9000)  #indirizzo del server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

while True:
    string = input("->")
    binary_string = string.encode()
    s.sendto(binary_string, SERVER_ADRESS)
    if string == "EXIT":
        break


    



