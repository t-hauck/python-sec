import hashlib, bcrypt

string = input("Digite o texto para geração do hash: ")
menu = input("""Escolha o tipo de HASH para ser gerado:
        1) MD5
        2) SHA1
        3) SHA256
        4) SHA512
        5) BCRYPT
        hash:  """
)


if menu == 1:
    resultado = hashlib.md5(b"string para Hash")
    print("\nhash MD5: ", resultado.hexdigest(), "\n")
elif menu == 2:
    resultado = hashlib.sha1(b"string para Hash")
    print("\nhash SHA1: ", resultado.hexdigest(), "\n")
elif menu == 3:
    resultado = hashlib.sha256(b"string para Hash")
    print("\nhash SHA256: ", resultado.hexdigest(), "\n")
elif menu == 4:
    resultado = hashlib.sha512(b"string para Hash")
    print("\nhash SHA512: ", resultado.hexdigest(), "\n")
elif menu == 5:
    bytes = string.encode('utf-8')
    salt = bcrypt.gensalt()
    print( bcrypt.hashpw(bytes, salt) )
else:
    print("\n\nOpção Incorreta\n")