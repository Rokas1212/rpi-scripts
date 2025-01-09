import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DC_MSG = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


def receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            if msg and msg != DC_MSG:
                print(f"\n{msg}")
        except:
            print("[ERROR] Disconnected from server.")
            break
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

while True:
    msg = input("")
    if(msg == ""):
        send(DC_MSG)
        print("Disconnected.")
        break
    send(msg)

