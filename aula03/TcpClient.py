import socket

server_address   = "3.93.168.169"
server_port      = 20001
buffer_size      = 1024

msg_from_client       = input("Forneça a mensagem: ")
bytes_to_send         = str.encode(msg_from_client)

# Cria um socket TCP
tcp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Conecta ao servidor
tcp_client_socket.connect((server_address, server_port))

# Envia requisição ao servidor
tcp_client_socket.sendall(bytes_to_send)

# Recebe resposta do servidor
msg_from_server = tcp_client_socket.recv(buffer_size)

msg = "Mensagem do servidor: {}".format(msg_from_server)

print(msg)