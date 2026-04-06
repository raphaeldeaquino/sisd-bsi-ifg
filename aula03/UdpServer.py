import socket

 
server_IP     = "127.0.0.1"
server_port   = 20001
buffer_size  = 1024

# Cria o socket UDP
udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Define o endereço IP e a porta
udp_server_socket.bind((server_IP, server_port))

print("Servidor UDP funcionando e esperando requisições")

# Espera o recebimento de datagramas
while(True):
    bytes_address_pair = udp_server_socket.recvfrom(buffer_size)
    message = bytes_address_pair[0]
    address = bytes_address_pair[1]

    client_msg = "Messagem do cliente: {}".format(message)
    client_IP  = "IP do cliente: {}".format(address)
    
    print(client_msg)
    print(client_IP)
    print('\n')
    
    # Faz o processamento da requisição
    reply_msg = message.decode("utf-8").upper()
    bytes_to_send = str.encode(reply_msg)
   

    # Enviando resposta ao cliente
    udp_server_socket.sendto(bytes_to_send, address)