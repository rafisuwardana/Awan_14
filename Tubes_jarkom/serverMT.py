from socket import *
import sys
import threading
import time

def handle_client(client_socket):
    # Menerima request dari klien
    request = client_socket.recv(1024).decode('utf-8')

    # Parsing request untuk mendapatkan nama file
    filename = request.split()[1]

    # Mencoba membuka file
    try:
        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        # Mengirim response header ke klien
        client_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        # Mengirim konten file ke klien
        for i in range(0, len(outputdata)):
            client_socket.send(outputdata[i].encode())
        client_socket.send("\r\n".encode())

    except IOError:
        # Mengirim response message jika file tidak ditemukan
        client_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        client_socket.send('404 Not Found'.encode())

    # Menutup koneksi dengan klien
    time.sleep(2)
    client_socket.close()

def main():
    # Membuat socket TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Mengikat ke alamat dan port tertentu
    serverSocket.bind(('localhost', 8080))

    # Mendengarkan koneksi masuk
    serverSocket.listen(1)

    print("Ready to serve...")

    #kode dibawah,setiap kali server menerima koneksi dari klien, ia membuat thread baru untuk menangani permintaan tersebut
    while True:
        # Menerima koneksi dari klien
        clientSocket, addr = serverSocket.accept()

        # Membuat thread baru untuk menangani permintaan klien
        client_thread = threading.Thread(target=handle_client, args=(clientSocket,))
        client_thread.start()

    # Menutup server socket
    serverSocket.close()

if __name__ == "__main__":
    main()
