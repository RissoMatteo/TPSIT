import socket

def send_request(request):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    client.send(request.encode('utf-8'))
    response = client.recv(4096).decode('utf-8')
    client.close()
    return response

# Interfaccia per l'invio delle richieste
def client_interface():
    while True:
        print("\nScegli un'opzione:")
        print("1. Cerca file per nome")
        print("2. Numero di frammenti di un file")
        print("3. IP host di un frammento specifico")
        print("4. Tutti gli IP host per i frammenti di un file")
        print("5. Esci")
        choice = input("Scelta: ")

        if choice == '1':
            nome_file = input("Inserisci il nome del file: ")
            response = send_request(f"SEARCH_FILE:{nome_file}")
            print("Risposta:", response)

        elif choice == '2':
            nome_file = input("Inserisci il nome del file: ")
            response = send_request(f"GET_FRAGMENT_COUNT:{nome_file}")
            print("Risposta:", response)

        elif choice == '3':
            nome_file = input("Inserisci il nome del file: ")
            n_frammento = input("Inserisci il numero del frammento: ")
            response = send_request(f"GET_FRAGMENT_HOST:{nome_file}:{n_frammento}")
            print("Risposta:", response)

        elif choice == '4':
            nome_file = input("Inserisci il nome del file: ")
            response = send_request(f"GET_ALL_FRAGMENT_HOSTS:{nome_file}")
            print("Risposta:", response)

        elif choice == '5':
            print("Chiusura del client.")
            break

        else:
            print("Scelta non valida. Riprova.")

client_interface()
