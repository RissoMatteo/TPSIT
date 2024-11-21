import socket
import threading
import turtle

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)

    window = turtle.Screen()
    victor = turtle.Turtle()
    movements = {"forward": victor.forward, 
                 "backward": victor.backward,
                 "left": victor.left,
                 "right": victor.right}


    while True:
        message, address = s.recvfrom(BUFFER_SIZE)
        message = message.decode()

        com, size = message.split('|')

        if com in movements:
            movements[com](int(size))#compatto i comandi con questa sintassi
            s.sendto(f"comando {com} eseguito con successo".encode(), address)
        else:
            print("comando non riconosciuto")
            s.sendto(f"comando {com} non riconosciuto".encode(), address)

        
        """
        if(com == "forward"):
            victor.forward(int(size))
            s.sendto("Comando forward eseguito".encode(), address)
        elif(com == "backward"):
            victor.backward(int(size))
            s.sendto("Comando backward eseguito".encode(), address)
        elif(com == "left"):
            victor.left(int(size))
            s.sendto("Comando left eseguito".encode(), address)
        elif(com == "right"):
            victor.right(int(size))
            s.sendto("Comando right eseguito".encode(), address)
        else:
            print("comando non riconosciuto")
            s.sendto("Comando non riuscito".encode(), address)
        """
        


if __name__ == "__main__":
    main()