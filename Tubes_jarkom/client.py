from socket import *
import sys

def main():
    # Membaca argumen baris perintah
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        return

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # Membuat socket TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Menghubungkan ke server
    clientSocket.connect((server_host, server_port))

    # Mengirim request HTTP ke server
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
    clientSocket.send(request.encode())

    # Menerima response dari server
    response = clientSocket.recv(1024)
    while response:
        print(response.decode(), end='')
        response = clientSocket.recv(1024)

    # Menutup koneksi dengan server
    clientSocket.close()

if __name__ == "__main__":
    main()
