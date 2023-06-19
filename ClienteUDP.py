import socket

# Endereço IP e porta do servidor
server_address = ("127.0.0.1",47001)

# Cria um socket UDP
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#client_socket.close()

# Mensagem a ser enviada ao servidor
message = b'LUPA'

try:
    # Envia a mensagem para o servidor
    client_socket.sendto(message, server_address)

    # Recebe a resposta do servidor
    data, server = client_socket.recvfrom(1024)
    print(data)

except:
    print("Erro ao enviar a mensagem")


# Fecha o socket
socket.socket.close(client_socket)



