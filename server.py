import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    while True:
        # Receive data from the client
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            print(f"Connection from {client_address} closed.")
            break
        print(f"Received message from {client_address}: {message}")

        # Send response back to the client
        response = input("Enter your response: ")
        client_socket.send(response.encode("utf-8"))

    # Close client socket
    client_socket.close()

# Main function
def main():
    # Server settings
    host = "127.0.0.1"
    port = 5555

    # Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
