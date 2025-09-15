"""Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket
import sys
def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    
    if len(sys.argv) != 3:
        print("Usage: python3 tcp_client.py <server-ip> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    # TODO: Get user input and send it to the server using your TCP socket
    message = input("Enter a message: ")
    client_socket.sendall(message.encode())

    # TODO: Receive a response from the server and close the TCP connection
    response = client_socket.recv(1024)
    print("Received from server:", response.decode())
    client_socket.close()


if __name__ == '__main__':
    main()
