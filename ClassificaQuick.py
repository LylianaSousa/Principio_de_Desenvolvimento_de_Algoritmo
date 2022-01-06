
import time 
#Teste pra classificar pela método Quick não recursivo

class PilhaLista:
    
    # Construtor da classe PilhaLista
    def __init__(self):
        self.pilha = []
    
    def __len__(self):
        return len(self.pilha)
    
    # retorna True se pilha vazia
    def vazia(self):
        return len(self.pilha) == 0
    
    # empilha novo elemento elem
    def push(self, elem):
            self.pilha.append(elem)           

    # retorna o elemento no tomo da lista
    def topo(self):
        if self.vazia():
            raise ValueError('Pilha vazia')

        return self.pilha[-1]

    # desempilha elemento, com uma exceção se pilha for vazia
    def pop(self):
        if self.vazia():
            raise ValueError('Pilha vazia')

        return self.pilha.pop()
 
    # imprime a pilha
    def __str__(self):
        
        return str(self.pilha)

def criandoTAB(nome):
    lines = []
    with open(nome) as f:
       lines = f.readlines()
    TAB = []

    for line in lines:
        TAB += [line.split(',')] 
        
    return TAB

def particiona(TAB, inicio, fim, ordem):
    n = len(TAB)
    i, j = inicio, fim
    pivo = TAB[fim]
    primeiro = int(ordem[0]) - 1
    segundo = int(ordem[1]) - 1
    terceiro = int(ordem[2]) - 1
    
    for i in range(n):
        if primeiro == 2:
            # aumentado i
            while i < j and TAB[i][primeiro][2] <= pivo[primeiro][2]:
                i = i + 1
            if i < j:
                TAB[i], TAB[j] = pivo, TAB[i]
            else:
                break
            # diminuindo j
            while i < j and TAB[j][primeiro][2]  >= pivo[primeiro][2]: 
                j = j - 1
            if i < j: 
                TAB[i], TAB[j] = TAB[j], pivo
            else: 
                break
        else:
            # aumentado i
            while i < j and TAB[i][primeiro] <= pivo[primeiro]:
                i = i + 1
            if i < j:
                TAB[i], TAB[j] = pivo, TAB[i]
            else:
                break
            # diminuindo j
            while i < j and TAB[j][primeiro]  >= pivo[primeiro]: 
                j = j - 1
            if i < j: 
                TAB[i], TAB[j] = TAB[j], pivo
            else: 
                break
        
    for i in range(n):
        if TAB[i][primeiro] == pivo[primeiro]:
            if segundo == 2:
                while i < j and TAB[i][segundo][2] <= pivo[segundo][2]:
                    i = i + 1
                if i < j:
                    TAB[i], TAB[j] = pivo, TAB[i]
                else:
                    break
                # diminuindo j
                while i < j and TAB[j][segundo][2]  >= pivo[segundo][2]: 
                    j = j - 1
                if i < j: 
                    TAB[i], TAB[j] = TAB[j], pivo
                else: 
                    break
            else:
                while i < j and TAB[i][segundo] <= pivo[segundo]:
                    i = i + 1
                if i < j:
                    TAB[i], TAB[j] = pivo, TAB[i]
                else:
                    break
                # diminuindo j
                while i < j and TAB[j][segundo]  >= pivo[segundo]: 
                    j = j - 1
                if i < j: 
                    TAB[i], TAB[j] = TAB[j], pivo
                else: 
                    break
  
    for i in range(n):
        if TAB[i][primeiro] == pivo[primeiro]:
            if TAB[i][segundo] == pivo[segundo]:
                if terceiro == 2:
                    while i < j and TAB[i][terceiro][2] <= pivo[terceiro][2]:
                        i = i + 1
                    if i < j:
                        TAB[i], TAB[j] = pivo, TAB[i]
                    else:
                        break
                    # diminuindo j
                    while i < j and TAB[j][terceiro][2]  >= pivo[terceiro][2]: 
                        j = j - 1
                    if i < j: 
                        TAB[i], TAB[j] = TAB[j], pivo
                    else: 
                        break
                else:
                    while i < j and TAB[i][terceiro] <= pivo[terceiro]:
                        i = i + 1
                    if i < j:
                        TAB[i], TAB[j] = pivo, TAB[i]
                    else:
                        break
                    # diminuindo j
                    while i < j and TAB[j][terceiro]  >= pivo[terceiro]: 
                        j = j - 1
                    if i < j: 
                        TAB[i], TAB[j] = TAB[j], pivo
                    else: 
                        break
    return i

def ClassificaQuick(TAB, ordem):
    t1 = time.time()
    # Cria a pilha de sub-listas e inicia com lista completa
    Pilha = PilhaLista()
    Pilha.push((0, len(TAB) - 1))
    # Repete até que a pilha de sub-listas esteja vazia
    
    #nesse primeiro for, inverterei a data em uma lista, para conseguir classificar pela ano
    for i in range(len(TAB)):
                s =TAB[i][2] 
                TAB[i][2] =  s.split('/')
    while not Pilha.vazia():
            inicio, fim = Pilha.pop()
            # Só particiona se há mais de 1 elemento
            if fim - inicio > 0:
                k = particiona(TAB, inicio, fim, ordem)
                # Empilhe as sub-listas resultantes
                Pilha.push((inicio, k - 1))
                Pilha.push((k + 1, fim))
    
    TABnovo = TAB[:]
    for i in range(len(TAB)):
                s =TAB[i][2] 
                TABnovo[i][2] = '/'. join(s)
   
    t2 = time.time()       
    print('Tempo de classificação Quick =', t2 - t1)        
    return TABnovo

if __name__ == '__main__':
 
        nome = 'testes1.txt'
        TAB = criandoTAB(nome)
        ordem = list('213')
        print(ClassificaQuick(TAB, ordem))