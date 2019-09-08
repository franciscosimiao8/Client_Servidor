from socket import *

serverName = '192.168.100.6'
serverPort = 12000
clientSocket = socket(family=AF_INET, type=SOCK_DGRAM)
message = raw_input('Escreva sua mensagem:')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()