# Echo client program
import socket

message = b""

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"open")
    data = s.recv(1024)
    print(data)
    s.send(b"cmd")
    data = s.recv(1024)
    print(data)