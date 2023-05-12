# https://gist.github.com/gabrielfalcao/4216897
##
import nmap

scanner = nmap.PortScanner()

host = input("Informe o Host: ")
type(host)

menu = input("""Escolha o tipo de varredura a ser feita:
        1) Varredura SYN
        2) Varredura UDP
        3) Varredura Intensa/Mais Profunda
        >   """
)
print("")

if menu == "1": # menu = string
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(host, '1-65535', '-v -sS') # IP, range de portas, parâmetros do nmap
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[host].state())
    print(scanner[host].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[host]['tcp'].keys())

elif menu == "2":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(host, '1-65535', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[host].state())
    print(scanner[host].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[host]['udp'].keys())

elif menu == "3":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(host, '1-65535', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[host].state())
    print(scanner[host].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[host]['tcp'].keys())

else:
    print("Opção Incorreta")
