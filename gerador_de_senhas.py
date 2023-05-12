import random, string

tamanho = input("Tamanho da Senha: ") ## tamanho = 20
size = int(tamanho);

quantidade = input("Quantidade de Senhas: ")
amount = int(quantidade);


chars = string.ascii_letters + string.digits + '!@#$%¨&*()_-=`~^]}[{]};:.><,/\|' ## ascii_lowercase
rnd = random.SystemRandom()

print ("\n")
for qtd in range (amount):
    print(''.join(rnd.choice(chars) for i in range(size)))

print ("\n\n")
