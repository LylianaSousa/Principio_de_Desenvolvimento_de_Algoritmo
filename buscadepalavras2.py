import time

#Criarei uma função para ler o arquivo e montar a lista com todas as palavras removendo as pontuações
def criandoTAB(nome):
    lines = []
    with open(nome, "r",  encoding="latin-1") as f:
        lines = f.readlines()
    TAB = []
    characters = "._!,?!;:"
    for line in lines:
        a = line.rstrip("\n")
        for character in characters:
            a = a.replace(character, "")
        b = a.split(' ')
        TAB += b
    return TAB

#Função que usará a função Intrínseca da python Count
def pycount(palavra, TAB):
    t1 = time.time()
    contador = TAB.count(palavra)
    t2 = time.time()
    t = t2 - t1
    print(f'count: Encontrada {contador} vezes em {t} segundos')
    
    
if __name__ == '__main__':
     #while True:
        nome ="machado.txt" #input("Entre com o nome do arquivo de texto:")
        TAB = criandoTAB(nome)
        pycount("lembrança", TAB)