from socket import *

serverPort = 12000
serverSocket = socket(family=AF_INET, type=SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print"O servidor esta pronto para receber"
while 1:
    print"Recebendo Mensagem:"
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    print('-='*20)
    print('\033[32m{}\033[m' .format(message))
    print('-='*20)
    serverSocket.sendto(modifiedMessage, clientAddress)