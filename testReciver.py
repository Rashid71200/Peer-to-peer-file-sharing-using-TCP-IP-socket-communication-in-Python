import socket

# Set up server socket






PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(f"IP Adress: {SERVER}")
print(socket.gethostbyname(socket.gethostname()))
print(f"IP Adress: {SERVER}")

ADDR = (SERVER, PORT)
print(ADDR)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

print(socket.gethostbyname(socket.gethostname()))

client, addr = server.accept()

File = client.recv(1024).decode()
print(f"File: --- {File}")
File = File.split("*")

file_name = File[0]
print(file_name)

file_size = File[1]
print(file_size)
file_size = int(file_size)
print(file_size)

file_format = File[2]
print(file_format)

output_file_name = f"{file_name}.{file_format}"
print(f"Writing to file: {output_file_name}")


print("file Transfaring.......")





'''
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

# Wait for client connection
print("Waiting for connection...")
client, addr = server.accept()
print(f"Connection from {addr}")

# Receive file name, size, and format
file_name = client.recv(1024).decode()
print(f"Received file name: {file_name}")
file_size = int.from_bytes(client.recv(1024), byteorder='big')
print(f"Received file size: {file_size}")
#file_format = client.recv(1024).decode()
file_format = client.recv(1024).decode()
print(f"Received file format: {file_format}")

# Open output file for writing
output_file_name = f"{file_name}.{file_format}"
print(f"Writing to file: {output_file_name}") */ '''



with open(output_file_name, "wb") as output_file:
    # Read and write file data in chunks
    bytes_read = 0
    while bytes_read < file_size:
        chunk_size = min(10102400, file_size - bytes_read)  # Read up to 1024 bytes or remaining bytes, whichever is smaller
        chunk = client.recv(chunk_size)  # Read a chunk of data from the client
        output_file.write(chunk)  # Write the chunk to the output file
        bytes_read += len(chunk)  # Update the number of bytes read so far
        print(f'Transfered {(bytes_read / 1000000)} MB out of {(file_size / 1000000)}MB....')

# Close the connection and server socket
client.close()
server.close()
print("File transfer complete.")
