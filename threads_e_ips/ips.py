import ipaddress
#
# ip = "192.168.0.1"
# endereco = ipaddress.ip_address(ip)
# print(endereco + 666)

ip = "192.168.0.0/8"

rede = ipaddress.ip_network(ip, strict=False) # strict = desativar erros
print(rede)

for ip in rede:
    print(ip)