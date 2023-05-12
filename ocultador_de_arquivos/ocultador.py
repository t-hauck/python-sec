import os, platform, ctypes

def hide_file_windows(filename):
    # Define a flag para ocultar o arquivo
    file_attribute_hidden = 0x02

    # Define a função SetFileAttributes da biblioteca kernel32 do Windows para configurar o atributo de arquivo oculto
    set_file_attributes = ctypes.windll.kernel32.SetFileAttributesW

    # Chama a função SetFileAttributes para ocultar o arquivo
    retorno = set_file_attributes(filename, file_attribute_hidden)
    if retorno:
        print("\n", f"{filename} ocultado com sucesso", "\n\n")
    else:
        print("\n", f"Erro ao ocultar {filename}", "\n\n")

def unhide_file_windows(filename):
    file_attribute_normal = 0x80

    # Define a função SetFileAttributes da biblioteca kernel32 do Windows para remover o atributo de arquivo oculto
    set_file_attributes = ctypes.windll.kernel32.SetFileAttributesW

    # Chama a função SetFileAttributes para remover o atributo de arquivo oculto
    retorno = set_file_attributes(filename, file_attribute_normal)
    if retorno:
        print(f"{filename} tornou-se visível com sucesso")
    else:
        print("\n", f"Erro ao tornar {filename} visível", "\n\n")

def hide_file_unix(filename):
    hidden_filename = f".{filename}" # adiciona . no nome
    os.rename(filename, hidden_filename)
    print("\n", f"{filename} ocultado com sucesso", "\n\n")

def unhide_file_unix(filename):
    # Cria uma nova variável com o nome do arquivo original sem o ponto no início
    unhidden_filename = filename.lstrip(".")
    os.rename(filename, unhidden_filename)
    print("\n", f"{filename} tornou-se visível com sucesso", "\n\n")



filename = input("Nome do arquivo ou pasta: ")
action = int(input("""O que deseja fazer:
        1) Ocultar
        2) Tornar Vísivel
        escolha:  """
))

if platform.system() == "Windows":
    if action == 1:
        hide_file_windows(filename)
    elif action == 2:
        unhide_file_windows(filename)

elif platform.system() in ["Linux", "Darwin"]:
    if action == 1:
        hide_file_unix(filename)
    elif action == 2:
        unhide_file_unix(filename)
else:
    print("Sistema operacional Não Suportado")
