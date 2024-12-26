import threading
from clientForTest import run_client  # Pastikan untuk mengimpor fungsi run_client dari client.py

def make_request(server_host, server_port, filename):
    run_client(server_host, server_port, filename)

if __name__ == "__main__":
    server_host = 'localhost'
    server_port = 8080
    filename = 'HelloWorld.html'
    
    threads = []
    for _ in range(10):  # Mengirim 10 permintaan simultan
        t = threading.Thread(target=make_request, args=(server_host, server_port, filename))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
