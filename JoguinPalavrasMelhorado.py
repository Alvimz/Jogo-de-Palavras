# # Tentar adivinhar a palavra
# # Conforme a sua tentativa, ele mostra se a palavra bate
# # Se a letra tiver na palavra, porém não na sua posição correta aparecerá em amarelo
# # caso esteja na posição correta aparecerá verde
life = 3
ListC = [] #lista letra por letra da palavra digitada para comparar
WordF = "arroz"  # palavra que você quer
WordF = WordF.lower()  # deixa a palavra tudo em minúsuclo
ListF = list(WordF) #lista letra por letra

dc = {}  # dicionário que conta as letras da palavra pra acertar!
for l in ListF: #loop para adicionar ao dicionário
    dc[l] = ListF.count(l)


# criar uma função para verificar letra


def FirstLetter():
    First = ListC[0]
    if First == ListF[0]:
        a = "🟩"
        dc[First] -= 1
        return a
    else:
        if First in ListF and dc[First] != 0:
            a = "🟨"
            return a
        else:
            a = "🟥"
            return a


def SecondLetter():
    Second = ListC[1]
    if Second == ListF[1]:
        b = "🟩"
        dc[Second] -= 1
        return b
    else:
        if Second in ListF and dc[Second] != 0:
            b = "🟨"
            return b
        else:
            b = "🟥"
            return b


def ThirdLetter():
    Third = ListC[2]
    if Third == ListF[2]:
        c = "🟩"
        dc[Third] -= 1
        return c
    else:
        if Third in ListF and dc[Third] != 0:
            c = "🟨"
            return c
        else:
            c = "🟥"
            return c


def QuardLetter():
    Quard = ListC[3]
    if Quard == ListF[3]:
        d = "🟩"
        dc[Quard] -= 1
        return d
    else:
        if Quard in ListF and dc[Quard] != 0:
            d = "🟨"
            return d
        else:
            d = "🟥"
            return d

def FifLetter():
    Fif = ListC[4]
    if Fif == ListF[4]:
        d = "🟩"
        dc[Fif] -= 1
        return d
    else:
        if Fif in ListF and dc[Fif] != 0:
            d = "🟨"
            return d
        else:
            d = "🟥"
            return d

def Results():
    result = f"{FirstLetter()}{SecondLetter()}{ThirdLetter()}{QuardLetter()}{FifLetter()}"

    print(result)
    if result == "🟩🟩🟩🟩🟩":
        print("Parabéns, você acertou!")

        return True

    return False

print('--Jogo de adivinhar a palavra!--')
while life != 0:
    if life != 0:
        print(f"Vidas:{life}. Digite o que você acha que é: ")

        WordC = input("> ")

        ListC = list(WordC)

    resultado = Results()

    if resultado:
        break

    life -= 1

if life == 0:
    print(f"Você perdeu! A palavra era '{WordF}'")
