import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 5432

print("Socket criado")

s.bind((host, port))
msg = "mensagem"

while True:
    dados, end = s.recvfrom(4096) # 4096 Bytes

    if (dados):
        print("servidor enviando mensagem")
        s.sendto(dados + (msg.encode()), end) # porta do servidor
