# student-fiek
from socket import *

server = '127.0.0.1'
port = 9000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((server, port))

mesazhiPerDergim = input("Mesazhi: ")


while True:
    clientSocket.send(mesazhiPerDergim.encode("UTF-8"))
    pergjigjjaNgaServeri = clientSocket.recv(128)
    print("Serveri: "+pergjigjjaNgaServeri.decode("UTF-8"))
