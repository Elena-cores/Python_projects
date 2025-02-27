# Echo server program
import socket

message = b"echo "



HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))    # bind Host and port to server
    s.listen(1)         # esperando al cliente
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)  
        while True:   
            data = conn.recv(1024)
            if data == b"open":
                conn.send(b"ejecuto open")
            else:
                conn.send(b"ejecuto otro cmd")
                conn.close()