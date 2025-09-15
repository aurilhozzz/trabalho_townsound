musicas = []
artistas = []
generos = []
duracoes = []
playlist = []
nome_playlist = ""


def menu():
    titulo  = "Bem vindo a TownSound!"
    largura = 50
    print(titulo.center(largura))


def cadastrar_musica():
    nome_musica = input("Digite o nome da música: ")
    tempo_musica = float(input("Digite o tempo: "))
    genero = input("Digite o gênero: ")
    artista_musica = input("Digite o nome do artista: ")
    
    musicas.append(nome_musica)
    artistas.append(artista_musica)
    generos.append(genero)
    duracoes.append(tempo_musica)
    for i in range(len(musicas)):
        print(musicas[i], artistas[i], generos[i], duracoes[i])
cadastrar_musica()


def criar_playlist():
    global nome_playlist
    nome_playlist = input("Digite o nome da nova playlist: ")
    print(f"Playlist '{nome_playlist}' criada com sucesso!")
def adicionar_musica_playlist():
    if nome_playlist == "":
        print("Nenhuma playlist criada. Crie uma playlist primeiro!")
        return
    if not musicas:
        print("Nenhuma música cadastrada para adicionar.")
        return
    print("Músicas cadastradas:")
    for i in range(len(musicas)):
        print(f"{i+1} - {musicas[i]} | {artistas[i]} | {generos[i]} | {duracoes[i]}")
    try:
        indice = int(input("Digite o número da música que deseja adicionar à playlist: ")) - 1
        if 0 <= indice < len(musicas):
            playlist.append(musicas[indice])
            print(f"Música '{musicas[indice]}' adicionada na playlist '{nome_playlist}'!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")
    print("Playlist atual:", playlist)
    
    
def iniciar_playlist():
    if nome_playlist == "":
        print("Nenhuma playlist criada. Crie uma playlist primeiro!")
        return
    if not playlist:
        print("A playlist está vazia.")
        return
    print(f"Tocando playlist '{nome_playlist}':")
    for nome in playlist:
        idx = musicas.index(nome)
        print(f"Tocando '{musicas[idx]}' de {artistas[idx]} ({generos[idx]}, {duracoes[idx]} min)...")
    
    
def tocar_musica():
    if not musicas:
        print("Nenhuma música cadastrada para tocar.")
        return
    print("Músicas disponíveis:")
    for i in range(len(musicas)):
        print(f"{i+1} - {musicas[i]} | {artistas[i]} | {generos[i]} | {duracoes[i]}")
    try:
        indice = int(input("Digite o número da música que deseja tocar: ")) - 1
        if 0 <= indice < len(musicas):
            print(f"Tocando '{musicas[indice]}' de {artistas[indice]} ({generos[indice]}, {duracoes[indice]} min)...")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")


def remover_musica():
    if not musicas:
        print("Nenhuma música cadastrada para remover.")
        return
    print("Músicas cadastradas:")
    for i in range(len(musicas)):
        print(f"{i+1} - {musicas[i]} | {artistas[i]} | {generos[i]} | {duracoes[i]}")
    try:
        indice = int(input("Digite o número da música que deseja remover: ")) - 1
        if 0 <= indice < len(musicas):
            nome_remover = musicas[indice]
            musicas.pop(indice)
            artistas.pop(indice)
            generos.pop(indice)
            duracoes.pop(indice)
            print(f"Música '{nome_remover}' removida com sucesso.")
            if nome_remover in playlist:
                playlist.remove(nome_remover)
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")
        

def sair():
    print("Obrigado por usar o TownSound! Até a próxima.")
    exit()


def funcoes():
    while True:
        print("1 - Cadastrar nova música")
        print("2 - Criar playlist")
        print("3 - Adicionar música a playlist")
        print("4 - Remover música")
        print("5 - Iniciar playlist")
        print("6 - Tocar música")
        print("7 - Sair")
        escolha = int(input("Escolha o número da opção: "))
        if escolha == 1:
            cadastrar_musica()
        elif escolha == 2:
            criar_playlist()
        elif escolha == 3:
            adicionar_musica_playlist()
        elif escolha == 4:
            remover_musica()
        elif escolha == 5:
            iniciar_playlist()
        elif escolha == 6:
            tocar_musica()
        elif escolha == 7:
            sair()
        else:
            print("Opção inválida.")
menu()
funcoes()
