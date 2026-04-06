import socket
from concurrent.futures import ThreadPoolExecutor
import time

server_address   = "3.93.168.169"
server_port      = 20001
buffer_size      = 1024
num_client		 = 2000
num_msg			 = 100


def task(client_id):
	# Cria um socket UDP
	udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	for m in range(1, num_msg):
		msg_from_client = "Mensagem #{} do cliente #{}".format(m, client_id)
		bytes_to_send = str.encode(msg_from_client)
		
		# Envia requisição ao servidor
		udp_client_socket.sendto(bytes_to_send, (server_address, server_port))
		
		# Recebe resposta do servidor
		msg_from_server = udp_client_socket.recvfrom(buffer_size)

		msg = "Mensagem do servidor: {}".format(msg_from_server[0])
		
		if client_id == 1:
			print(msg)
		
		time.sleep(1)
		
		
		
if __name__ == '__main__':
	# cria um pool de threads com a quantidade de threads
	pool = ThreadPoolExecutor(max_workers=num_client)
	pool.map(task, range(1, num_client))