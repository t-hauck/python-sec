import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Falha na Conexão")
        print("Erro: {}".format(e))
        sys.exit() #print("Socket criado com sucesso!")

    HostAlvo = input("Insira o endereço do host para conexão: ")
    PortaAlvo = input("Insira a porta do host remoto: ")
    try:
        s.connect((HostAlvo, int(PortaAlvo)) )
        print("\nSucesso na conexão TCP ao host " + HostAlvo + " na porta " + PortaAlvo + "\n\n")
        s.shutdown(2) # 2 Segundos

    except socket.error as e:
        print("\nNão foi possível conectar via TCP ao host " + HostAlvo + " na porta " + PortaAlvo)
        print("Erro: {}".format(e) + "\n\n")
        sys.exit()


if __name__ == "__main__":
    main()