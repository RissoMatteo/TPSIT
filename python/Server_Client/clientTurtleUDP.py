import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        com = input("Inserisci il comando: \n->")
        size = input ("Inserisci lo spostamento/angolo: \n->")

        mex = f"{com}|{size}" # com+"|"+size java stile

        s.sendto(mex.encode(), SERVER_ADDRESS)
        server_mex, _ = s.recvfrom(BUFFER_SIZE)

        print(server_mex.decode())

    s.close()

if __name__ == "__main__":
    main()
    