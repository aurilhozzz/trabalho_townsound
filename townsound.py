musicas = []
artistas = []
generos = []
duracoes = []
playlist = []

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

def iniciar_playlist():
    if nome_playlist == "":
        print("Nenhuma playlist criada. Crie uma playlist primeiro!")
        return
    if not musicas:
        print("Nenhuma música cadastrada para adicionar.")
        return
    print("Músicas cadastradas:")
    for i in range(len(musicas)):
        print(f"{i+1} - {musicas[i]} | {artistas[i]} | {generos[i]} | {duracoes[i]}")
    nome_escolhido = input("Digite o nome da música que deseja adicionar à playlist: ")
    if nome_escolhido in musicas:
        playlist.append(nome_escolhido)
        print(f"Música '{nome_escolhido}' adicionada na playlist '{nome_playlist}'!")
    else:
        print("Música não encontrada.")
    print("Playlist atual:", playlist)

def remover_musica():
    nome_remover = input("Digite o nome da música que deseja remover: ")
    if nome_remover in musicas:
        index = musicas.index(nome_remover)
        musicas.pop(index)
        artistas.pop(index)
        generos.pop(index)
        duracoes.pop(index)
        print(f"Música '{nome_remover}' removida com sucesso.")
        if nome_remover in playlist:
            playlist.remove(nome_remover)
    else:
        print(f"Música '{nome_remover}' não encontrada.")

def sair():
    print("Obrigado por usar o TownSound! Até a próxima.")
    exit()

def criar_playlist():
    nome_playlist = input("Digite o nome da nova playlist: ")
    print(f"Playlist '{nome_playlist}' criada com sucesso!")

def tocar_musica():
    if not musicas:
        print("Nenhuma música cadastrada para tocar.")
        return
    print("Músicas disponíveis:")
    for i in range(len(musicas)):
        print(f"{i+1} - {musicas[i]} | {artistas[i]} | {generos[i]} | {duracoes[i]}")
    nome_escolhido = input("Digite o nome da música que deseja tocar: ")
    if nome_escolhido in musicas:
        idx = musicas.index(nome_escolhido)
        print(f"Tocando '{musicas[idx]}' de {artistas[idx]} ({generos[idx]}, {duracoes[idx]} min)...")
    else:
        print("Música não encontrada.")

def adicionar_playlist():
    print("Músicas disponíveis para adicionar:")
    for i in range(len(musicas)):
        print(f"{i+1} - {musicas[i]} | {artistas[i]} | {generos[i]} | {duracoes[i]}")
    musica_adicionar = input("Digite o nome da música para adicionar: ")
    if musica_adicionar in musicas:
        playlist.append(musica_adicionar)
        print(f"Música {musica_adicionar} adicionada a playlist {nome_playlist}")
    else:
        print("Música inválida.")
        
def funcoes():
    while True:
        print("1 - Cadastrar nova música")
        print("2 - Criar playlist")
        print("3 - Remover música")
        print("4 - Iniciar playlist")
        print("5 - Tocar música")
        print("6 - Sair")
        escolha = int(input("Escolha o número da opção: "))
        if escolha == 1:
            cadastrar_musica()
        elif escolha == 2:
            criar_playlist()
        elif escolha == 3:
            remover_musica()
        elif escolha == 4:
            iniciar_playlist()
        elif escolha == 5:
            tocar_musica()
        elif escolha == 6:
            sair()
        else:
            print("Opção inválida.")
menu()
funcoes()
