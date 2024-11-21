import socket
from pynput import keyboard

# Server address
SERVER_ADDRESS = ("192.168.1.145", 9090)
BUFFER_SIZE = 4096

# Create a socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(SERVER_ADDRESS)

# Key to command mapping
key_comandi = {"w": "forward", "s": "backward", "a": "left", "d": "right", "f": "stop"}
statoKey = {"w": False, "s": False, "a": False, "d": False, "f": False}

# Function to handle key presses
def on_press(key):
    try:
        if key.char in key_comandi and not statoKey[key.char]:
            statoKey[key.char] = True
            # Send the corresponding movement command to the server
            s.sendall(f"{key_comandi[key.char]}".encode())
            print(f"Command sent: {key_comandi[key.char]}")
    except AttributeError:
        pass

# Function to handle key releases
def on_release(key):
    try:
        if key.char in key_comandi:
            statoKey[key.char] = False
            # Send the stop command when the key is released
            s.sendall("stop".encode())
            print("Command sent: stop")
    except AttributeError:
        pass

# Start listening for key presses and releases
def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def main():
    start_listener()

if __name__ == '__main__':
    main()
