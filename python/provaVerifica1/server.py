import socket
import threading
import sqlite3

def handle_client(client_socket):
    conn = sqlite3.connect('file.db')
    cursor = conn.cursor()
    
    while True:
        request = client_socket.recv(1024).decode('utf-8')
        if not request:
            break

        # Parse the request
        parts = request.split(':')
        command = parts[0]

        if command == 'SEARCH_FILE':
            nome_file = parts[1]
            cursor.execute("SELECT 1 FROM files WHERE nome = ?", (nome_file,))
            result = cursor.fetchone()
            response = f"FILE_FOUND:{nome_file}:{bool(result)}"
        
        elif command == 'GET_FRAGMENT_COUNT':
            nome_file = parts[1]
            cursor.execute("SELECT tot_frammenti FROM files WHERE nome = ?", (nome_file,))
            result = cursor.fetchone()
            if result:
                tot_frammenti = result[0]
                response = f"FRAGMENT_COUNT:{nome_file}:{tot_frammenti}"
            else:
                response = f"FRAGMENT_COUNT:{nome_file}:NOT_FOUND"

        elif command == 'GET_FRAGMENT_HOST':
            nome_file, n_frammento = parts[1], int(parts[2])
            cursor.execute("""
                SELECT f.host FROM frammenti f
                JOIN files ON f.id_file = files.id_file
                WHERE files.nome = ? AND f.n_frammento = ?
            """, (nome_file, n_frammento))
            result = cursor.fetchone()
            if result:
                response = f"FRAGMENT_HOST:{nome_file}:{n_frammento}:{result[0]}"
            else:
                response = f"FRAGMENT_HOST:{nome_file}:{n_frammento}:NOT_FOUND"

        elif command == 'GET_ALL_FRAGMENT_HOSTS':
            nome_file = parts[1]
            cursor.execute("""
                SELECT f.host FROM frammenti f
                JOIN files ON f.id_file = files.id_file
                WHERE files.nome = ?
            """, (nome_file,))
            hosts = [row[0] for row in cursor.fetchall()]
            response = f"ALL_FRAGMENT_HOSTS:{nome_file}:{','.join(hosts)}" if hosts else f"ALL_FRAGMENT_HOSTS:{nome_file}:NOT_FOUND"
        
        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Server in ascolto sulla porta 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connessione accettata da {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

start_server()
