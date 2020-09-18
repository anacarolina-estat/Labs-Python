# Clique em "RUN" e e divirta-se na tela preta

cenas_forca = [
    """+++++
    |   |
    |
    |
    |
    +_______""",

    """+++++
    |   |
    |   O
    |
    |
    +_______""",

    """+++++
    |   |
    |   O
    |   |
    |
    +_______""",
    """+++++
    |   |
    |   O
    |  /|
    |
    +_______""",

    """+++++
    |   |
    |   O
    |  /|\\
    |
    +_______""",

    """+++++
    |   |
    |   O
    |  /|\\
    |  /
    +_______""",

    """+++++
    |   |
    |   O
    |  /|\\
    |  / \\
    +_______"""

]

palavras = ["perfeitamente", "liberdade", "enfermidade", "significado", "outono", "chuva", "ilha", "infinito",
            "solidariedade", "ameixa", "felicidade", "arte", "paternidade", "criatividade", "virtude", "guerra",
            "democracia", "teatro", "saudade", "adeus", "paz", "honestidade", "horizonte", "sabedoria", "sossego",
            "maternidade", "esperteza", "primavera", "coragem", "igualdade", "navio", "montanha", "queijo", "gentileza",
            "tempestade", "joalheria", "paralelogramo", "melancolia", "trem", "inverno", "amizade", "atriz",
            "computador", "borboleta", "aeroporto", "nascimento", "uva", "oceano", "orquestra", "melancia"]

num = int(input("Escolha um numero entre 0 e 49: "))

if num in range(50):
    contErro = 0
    contCerto = 0
    incLetras = []
    palavra = palavras[num]
    tamPalavra = ["_" for i in range(len(palavra))]
    erradas = []
    letras = []

    while contErro < 7 and contCerto != (len(palavra) + 1):

        auxpalavra = palavra
        print()
        print(cenas_forca[contErro])
        print("Palavra: ", end="")
        aux2 = 0
        while aux2 < len(tamPalavra):
            if aux2 != 0:
                print("  ", end="")
            print(tamPalavra[aux2], end="")
            aux2 += 1
        print()

        pos = []
        remov = 0

        aux3 = 0
        if len(erradas) > 0:
            print("Tentativa(s) incorreta(s):", end="")
            for i in erradas:
                print(" " + i, end="")
            print()

        if contCerto != len(palavra) and contErro < 6:
            proxLetra = input("Proxima letra: ")

        if proxLetra in letras:
            print("Voce jah escolheu esta letra.")

        else:

            while proxLetra in auxpalavra:
                aux = auxpalavra.find(proxLetra)
                pos.append(aux + remov)
                auxpalavra = auxpalavra[(aux + 1):]
                remov = remov + aux + 1

                for i in pos:
                    del tamPalavra[i]
                    tamPalavra.insert(i, proxLetra)

                contCerto += 1

            if not proxLetra in palavra:
                erradas.append(proxLetra)
                contErro += 1

        if contCerto != len(palavra) and contErro < 6:
            letras.append(proxLetra)

    if contCerto == (len(palavra) + 1):
        print("Palavra encontrada!")

    elif contErro == 7:
        print("Palavra oculta:", palavra)

else:
    print("Numero invalido.")