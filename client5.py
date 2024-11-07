import socket

def run_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('localhost', 65432)  # Use the same IP and port as the server
    print(f"Connecting to server at {server_address}...")
    client_socket.connect(server_address)

    try:
        # Send a greeting message to the server
        client_message = "Hello, Server!"
        client_socket.sendall(client_message.encode())
        print(f"Sent to server: {client_message}")

        # Receive the server's response
        server_message = client_socket.recv(1024).decode()
        print(f"Server says: {server_message}")

    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    run_client()







'''
Connection-Oriented Protocol: TCP establishes a connection between sender and receiver before data is transmitted, using a three-way handshake (SYN, SYN-ACK, ACK) to ensure both ends are ready for data transfer.

Reliable Data Transfer: TCP ensures that data packets are delivered in sequence and without errors. If any packet is lost or damaged, TCP will retransmit it.

Flow Control: TCP manages the rate at which data is sent between sender and receiver, preventing network congestion and ensuring the receiver is not overwhelmed.

Error Checking and Recovery: TCP uses checksums to verify data integrity and requests retransmission if errors are detected.
'''
