import socket

def main():
    # Server settings
    host = "127.0.0.1"
    port = 5555

    # Connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server.")

    while True:
        # Send message to server
        message = input("Enter your message: ")
        client_socket.send(message.encode("utf-8"))

        # Receive response from server
        response = client_socket.recv(1024).decode("utf-8")
        print(f"Server response: {response}")

    # Close client socket
    client_socket.close()

if __name__ == "__main__":
    main()
