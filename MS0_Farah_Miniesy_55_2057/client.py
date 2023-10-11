import socket

def start_client():
    cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl_socket.connect(('localhost', 12345))

    while True:
        message = input('Enter your message (or enter "close socket" to exit): ')

        if message.lower() == 'close socket':
            break

        cl_socket.send(message.encode('utf-8'))
        received_data = cl_socket.recv(1024).decode('utf-8')
        print('Received:', received_data)

    cl_socket.close()

start_client()


