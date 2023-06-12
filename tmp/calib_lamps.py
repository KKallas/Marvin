import socket

# Define the target IP address and port
target_ip = '255.255.255.255'  
target_port = 6454  # Replace with the desired port

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable socket broadcast option
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Enable socket address reuse option
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to a specific IP and port
sock.bind(('0.0.0.0', target_port))

# Set the channels to 50% intensity (values range from 0 to 255)
channels = [int(0.5 * 255)] * 5

# Build the Art-Net packet
packet_header = b'Art-Net\x00'  # Art-Net protocol header
op_code = b'\x00\x50'  # Op code for ArtDmx packet
sequence = b'\x00'  # Sequence number (can be set to zero)
physical = b'\x00'  # Physical port number (can be set to zero)
universe = b'\x00\x00'  # Universe number
length = b'\x02\x00'  # Length of data (in words)
data = bytearray(channels)  # Convert the list of channels to a bytearray

# Concatenate the packet parts
packet = packet_header + op_code + sequence + physical + universe + length + data

# Send the Art-Net packet
sock.sendto(packet, (target_ip, target_port))

# Close the socket
sock.close()