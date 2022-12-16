import socket

# echo-server.py

import socket

HOST = "127.0.0.1"
PORT = 6666
BUFFER_SIZE = 1024*128
SEPARATOR = "<sep>"

server = socket.socket()
server.bind((HOST, PORT))
server.listen()
print('server listenning')
conn, addr = server.accept()
print(f"Connected by {addr}")
cwd = conn.recv(BUFFER_SIZE)

while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    command = b'dir'
    server.send(command)
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = server.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    # print output
    print(results)

server.close()