import socket
from AlphaBot import AlphaBot  # Assuming the AlphaBot class is in AlphaBot.py

MY_ADDRESS = ("192.168.1.145", 9090)
BUFFER_SIZE = 4096

# Create an instance of AlphaBot
robot = AlphaBot()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    connection, client_address = s.accept()
    print(f"Client {client_address} connected")
    running = True

    while running:
        # Receive message from the client
        message = connection.recv(BUFFER_SIZE).decode()
        print(f"Received: {message}")
        
        # Control the robot based on the received command
        if message == "forward":
            robot.forward()
        elif message == "backward":
            robot.backward()
        elif message == "left":
            robot.left()
        elif message == "right":
            robot.right()
        elif message == "stop":
            robot.stop()
        else:
            connection.sendall("error|Invalid command".encode())

    connection.close()

if __name__ == '__main__':
    main()
