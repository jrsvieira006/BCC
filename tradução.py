port = ["como","oi","bonito","azul"]
ing = ["how","hello","beautiful","blue"]

palavra = input()
palavras = palavra.split(" ")

for palavra in palavras:
    if palavra in ing:
        x = ing.index(palavra)
        print(port[x])
