import socket, re

pattern = re.compile(r"^(\w+)(,\s*\w+)*$")
def check_port(input_string):
    if pattern.match(input_string) == None:
        return False # string Valida com virgula
    else:
        return True


host = input("Informe o Host: \n    ")
port = input("Informe uma ou mais Portas separadas por virgula: \n    ")
print("------------------------- \n\n")

if check_port(port):
    ports = port.split(",")

    for p in ports:
        ports = int(p)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4
        client.settimeout(0.05)
        code  = client.connect_ex((host, ports))

        if code == 0:
            print(" + ", str(ports), "> Porta Aberta")
        else:
            print(" - ", str(ports), "> Porta Fechada")
    print("\nScan Finalizado\nHost: {}".format(host), "\n")
else:
    print("ERRO: Endereço do Host ou Porta Inválida")

