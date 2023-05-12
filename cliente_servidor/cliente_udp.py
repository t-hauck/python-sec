import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "127.0.0.1"
port = "22"
msg = "msg"

try:
    print("Cliente: " + msg)
    s.sendto(msg.encode(), (host, 5432)) # porta do servidor

    dados, servidor = s.recvfrom(4096) # 4096 Bytes
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print("Cliente: conexão fechada")
    s.close()
