import os
import socket

PORT = 5050
SERVER = "172.31.208.1"

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ADDR))

file_name = input("File Name: ")
file_name1 = file_name.split("'")
name4 = len(file_name1)
print(name4)
if name4 > 2:
    file_name = file_name1[1]
#file_name = file_name1[1]
print(file_name)





name = file_name.split('.')
file_formet = name[-1]
name6 = len(file_formet)
name7 = len(file_name)
name8 = name7 - (name6 + 1 )
name8 = file_name[ :name8]
print(f"name8{name8}")
#print(name)
name3 = len(name)
print(name3)
#file_name1 = name[0]

print(name8)
print(file_formet)

file_name = name8 + '.' + file_formet


file = open(file_name, "rb")
file_size = os.path.getsize(file_name)
print("file open susssesfully")

file_name3 = name8.split("\\")
file_name3 = file_name3[-1]
print(file_name3)

client.send(file_name3.encode())
client.send(str(file_size).encode())
client.send(file_formet.encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()