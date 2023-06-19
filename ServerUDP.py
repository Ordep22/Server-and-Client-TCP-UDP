import socket
from time import localtime, sleep
# 177.207.193.146
# 187.32.79.169
# 127.0.0.1

localIP = '192.168.0.6'
#localIP = 'localhost'

localPort = 47001

bufferSize = 1024

messagetosend = b"LUPA2022"

# Create a datagram socket

UDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDP.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

while (True):

    bytesAddressPair = UDP.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    print(f'[{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}] Conexão estabelecida com:',address)

    print(f'[{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}] Mensagem recebida do cliente:',message)


    while True:

        UDP.sendto(messagetosend, address)

        print(f'[{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}] Mensagem enviada ao cliente: ',messagetosend)
        sleep(35)

        bytesAddressPair = UDP.recvfrom(bufferSize)

        message = bytesAddressPair[0]

        print(f'[{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}] Mensagem recebida do cliente: ',message)











