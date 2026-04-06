import socket
from threading import Thread

 
server_IP     = "127.0.0.1"
server_port   = 20001
buffer_size   = 1024

def task(client_socket, address):
	message = client_socket.recv(buffer_size)
	
	client_msg = "Messagem do cliente: {}".format(message)
	client_IP  = "IP do cliente: {}".format(address)
	
	# Faz o processamento da requisição
	reply_msg = message.decode("utf-8").upper()
	bytes_to_send = str.encode(reply_msg)
	
	# Enviando resposta ao cliente
	client_socket.send(bytes_to_send)


if __name__ == "__main__":
	# Cria o socket TCP
	tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

	# Define o endereço IP e a porta
	tcp_server_socket.bind((server_IP, server_port))

	print("Servidor TCP funcionando e esperando conexões")

	# Espera o recebimento de solicitações de conexão
	while(True):
		# Espera requisição de conexão
		tcp_server_socket.listen() 
	
		# Aceita requisição de conexão
		client_socket, address = tcp_server_socket.accept() 
		
		thread = Thread(target=task, args=(client_socket, address,))
		
		thread.start()

	
		
	
		
	
		
	
		