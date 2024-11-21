#scrivi un programam server in linguaggio py che abbia le seguenti carattrisitche : 
#il programma usa un socket udp per realizzare un programma echo


import socket

# Definizione dell'indirizzo IP e della porta del server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Creazione di un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associazione dell'indirizzo IP e della porta al socket
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Server UDP avviato su {SERVER_IP}:{SERVER_PORT}")

while True:
    # Ricezione dei dati e dell'indirizzo del client
    data, client_address = server_socket.recvfrom(1024)
    
    # Echo dei dati ricevuti indietro al client
    server_socket.sendto(data, client_address)

    # Stampa delle informazioni ricevute
    print(f"Ricevuto messaggio da {client_address}: {data.decode('utf-8')}")

# Chiusura del socket server (in realtà non raggiungerà mai questo punto nel codice di esempio)
server_socket.close()