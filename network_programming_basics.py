import socket
import threading
import time

def udp_server():
   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   
    server_address = ('127.0.0.1', 12345)
    server_socket.bind(server_address)

    print(f"UDP server listening on {server_address}")

    while True:
        data, client_address = server_socket.recvfrom(1024) # Receiving data from the client
        print(f"Received from {client_address}: {data.decode()}")

       
        response = "Message received!"
        server_socket.sendto(response.encode(), client_address)

def udp_client():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   
    server_address = ('127.0.0.1', 12345)

  
    message = "Hello, server!"
    client_socket.sendto(message.encode(), server_address)

  
    response, server_address = client_socket.recvfrom(1024)
    print(f"Response from the server: {response.decode()}")

 
    client_socket.close()

if __name__ == "__main__":
  
    server_thread = threading.Thread(target=udp_server)
    server_thread.start()

    time.sleep(1)

    udp_client()