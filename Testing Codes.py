import socket
from time import localtime
from time import sleep

HOST = ''
PORT = 47000



tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen()

print("Aguardando conexão!")
msg = b"TEST2022"

while True:
    conexao, endereco = tcp.accept()

    print(f'[{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}] Conexão estabelecida com:', endereco)

    while True:

        conexao.send(msg)

        print(f'[{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}] Dados enviados: {msg}')



        try:


            dados = conexao.recv(1024)

        except:

            break

        if dados == b"":
            print(f'[{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}] Conexão encerrada')
            print(20 * "--")
            print("\n")
            conexao.close()
            break

        print(f'[{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}] Dados recebido: {dados}')

        sleep(50)