import socket

def uppercase(message):
    return message.upper()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print('Server listening on port 12345...')

    while True:
        cl_socket, cl_address = server_socket.accept()
        print('Connected to', cl_address)

        while True:
            data = cl_socket.recv(1024).decode('utf-8')
            if not data:
                break

            uppercase_data = uppercase(data)
            cl_socket.send(uppercase_data.encode('utf-8'))
            print('Message sent:', uppercase_data)

        cl_socket.close()

start_server()