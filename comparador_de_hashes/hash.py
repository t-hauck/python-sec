import hashlib

print("- Mova dois arquivos para o mesmo local deste script para serem comparados \n")
arquivo1 = input("Arquivo 1: ")
arquivo2 = input("Arquivo 2: ")

hash1 = hashlib.new("ripemd160")
hash1.update( open(arquivo1, "rb").read() )

hash2 = hashlib.new("ripemd160")
hash2.update( open(arquivo2, "rb").read() )


if hash1.digest() != hash2.digest():
    print(f"\n\nOs arquivos são diferentes: {arquivo1} {arquivo2}")
    print("Hash ", arquivo1, "\n    ", hash1.hexdigest(), "\n")
    print("Hash ", arquivo2, "\n    ", hash2.hexdigest(), "\n")
else:
    print(f"\n\nO arquivo {arquivo1} é igual ao arquivo {arquivo2}")
    print("Hash: \n     ", hash1.hexdigest(), "\n")