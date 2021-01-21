import socket

def server():
	#get the hostname
	HOST = socket.gethostname()
	PORT = 5050

	s_socket = socket.socket()
	s_socket.bind((HOST, PORT))
	s_socket.listen(2)
	conn, addr = s_socket.accept()
	print("Connection from: " + str(addr))
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print("from connectet user: " + str(data))
		conn.send(data.encode())
	conn.close()

if __name__ == '__main__':
	server()