import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

print(socket.gethostbyname(socket.gethostname()))

client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = int(client.recv(1024).decode())
print(file_size)

file_formet = client.recv(1024).decode()
print(file_formet)

print("file Transfaring.......")

file = client.recv(file_size)
name_of_file = file_name
name_of_file = name_of_file + '.' + file_formet

binary_file = open(name_of_file, "wb")
binary_file.write(file)

binary_file.close()

print("file Trensferd susssesfully")
