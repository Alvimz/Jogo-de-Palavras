import random


class Main:
    def __init__(self):
        self.WordF = self.gerarPalavraFinal()  # Palavra aleatória final!
        self.ListF = list(self.WordF)  # Lista de letras da palavra
        self.dcFinal = self.tratamentofinal()  # Dicionário de contagem de letras
        self.ListC = []  # Lista de letras da tentativa do usuário

    def gerarPalavraFinal(self):
        ListaPalavraSortida = []  # Lista de palavras

        with open("palavras.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()
            for palavra in conteudo.split(","):
                ListaPalavraSortida.append(
                    palavra.strip().lower()
                )  # Remove espaços e minúsculas

        numero = random.randint(0, len(ListaPalavraSortida) - 1)
        WordF = ListaPalavraSortida[numero]  # Palavra selecionada
        return WordF

    def tratamentofinal(self):
        dcFinal = {}  # Dicionário que conta as letras
        for letra in self.ListF:
            dcFinal[letra] = self.ListF.count(letra)
        return dcFinal

    def tentativa(self, WordC):
        self.ListC = list(WordC.lower())  # Atualiza a lista com a tentativa

    def verificar_letra(self, posicao):
        letra = self.ListC[posicao]
        if letra == self.ListF[posicao]:
            resultado = "🟩"
            self.dcFinal[letra] -= 1
        elif letra in self.ListF and self.dcFinal[letra] > 0:
            resultado = "🟨"
        else:
            resultado = "🟥"
        return resultado

    def Results(self):
        if len(self.ListC) != 5:
            print("Insira uma palavra com 5 letras!")
            return False

        result = "".join([self.verificar_letra(i) for i in range(5)])
        print(result)
        if result == "🟩🟩🟩🟩🟩":
            print("Parabéns, você acertou!")
            return True
        return False


print("--Jogo de adivinhar a palavra!--")
life = 4
pessoa = Main()

while life > 0:
    print(f"Vidas: {life}. Digite o que você acha que é: ")
    tentativa = input("> ")
    pessoa.tentativa(tentativa)

    if pessoa.Results():
        break

    life -= 1

if life == 0:
    print(f"Você perdeu! A palavra era '{pessoa.WordF}'")
