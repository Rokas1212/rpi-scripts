import socket
import threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DC_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
CONNS = []


def broadcast(message, sender):
    for connection in CONNS:
        if connection != sender:
            try:
                connection.send(message.encode(FORMAT))
            except:
                CONNS.remove(connection)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    CONNS.append(conn)
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DC_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            broadcast(f"[{addr}]: {msg}", conn)
    CONNS.remove(conn)
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")



print("[STARTING] server is starting...")
start()

