import socket

#mostly taken from socket documentation and cewing's walkthru

def waitformsg():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 7539))
    server.listen(1)
    conn, addr = server.accept()
    
    data = True
    while data:
        data = conn.recv(1024)
        conn.sendall(data)
    
    conn.close()
    server.close()

if __name__ == '__main__':
    waitformsg()