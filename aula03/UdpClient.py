import socket

server_address   = "127.0.0.1"
server_port      = 20001
buffer_size      = 1024

msg_from_client       = input("Forneça a mensagem: ")
bytes_to_send         = str.encode(msg_from_client)

# Cria um socket UDP
udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Envia requisição ao servidor
udp_client_socket.sendto(bytes_to_send, (server_address, server_port))

# Recebe resposta do servidor
msg_from_server = udp_client_socket.recvfrom(buffer_size)

msg = "Mensagem do servidor: {}".format(msg_from_server[0])

print(msg)