import socket

def listen_udp(port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to localhost and the specified port
    server_address = ('localhost', port)
    print(f"Starting UDP server on {server_address[0]} port {server_address[1]}")
    sock.bind(server_address)
    
    while True:
        print("\nWaiting to receive message...")
        data, address = sock.recvfrom(4096)
        
        print(f"Received {len(data)} bytes from {address}")
        print(f"Data: {data.decode()}")

if __name__ == "__main__":
    PORT = 6002  # Change this to your desired port
    listen_udp(PORT)