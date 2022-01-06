# Exercício Programa I - MAC 122 - PDA
#Nome: Lyliana Myllena Santos de Sousa
#NUSP:11223740

#EXERCÍCIO ENTREGUE PARA CORREÇÃO

import re

# Criando a classe Pilha
class Pilha:
    
    # Construtor da classe PilhaLista
    def __init__(self, tamanho):
        self.pilha = []
        self.tamanho = tamanho
    
    # empilha novo elemento elem
    def push(self, elem):
        if len(self.pilha) < self.tamanho:
            self.pilha.append(elem)           

    # desempilha elemento, com uma exceção se pilha for vazia
    def pop(self):
        resultado = -1

        if self.pilha != []:
            resultado = self.pilha.pop()

        return resultado
    
    # retorna True se pilha vazia
    def vazia(self):
        return self.pilha == []
    
    # retorna o elemento no tomo da lista
    def topo(self):
        resultado = -1

        if self.pilha != []:
            resultado = self.pilha[len(self.pilha) - 1]

        return resultado
    
    # imprime a pilha
    def __str__(self):
        strPilha = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", self.pilha)       
        return str(strPilha)



"""  definirei algumas funções que nos ajudaram ao longo do exercício"""



# confere se o elemento analisado é um "número", para ser mais precisa um string referente a um número
def numero(c):
    return c >= '0' and c <= '9'

#Lista dos operadores que usaremos, indo do com prioridade menor para prioridade maior
operadores = ['+','-','*','/','**']

# confere se o elemento analisado é um operador
def operador(c):
    return c in operadores

# função que decide a prioridade dos operadores
def precedente(c):
    resultado = 0

    for i in operadores:
        resultado += 1

        if i == c:
            if c in '-/':
                resultado -= 1
            break
       
    return resultado

 
# função que traduz a nossa expressão para pos fixa
def TraduzPosFixa(exp):
    resultado = ""

    pilha = Pilha(15000)
    j = 0
    for i in exp:
           
        if numero(i):
            resultado += i 
       
        elif operador(i):
                     
            while True:
                topo = pilha.topo()
                resultado += chr(32)
                if i == '*' and exp[j +1] == '*':
                        pilha.push(i)
                        break
                if i == '*' and exp[j -1] == '*':
                        pilha.push(i)
                        break
                if pilha.vazia() or topo == '(':
                    pilha.push(i)
                    break
                
                  
                else:
                   
                    pC = precedente(i)
                    pTC = precedente(topo)

                    if pC > pTC:
                        pilha.push(i)
                        break
                    else:
                        resultado += pilha.pop()

        elif i == '(':
            pilha.push(i)
        elif i == ')':
            cpop = pilha.pop()

            while cpop != '(':
                resultado += cpop
                cpop = pilha.pop()
        j += 1
        
    while not pilha.vazia():
        cpop = pilha.pop()
        resultado += cpop

    res =  re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", resultado)       
    return str(res)

# Vou definir uma classe chamada de operação para realizar os calculos na notação pos fixa
      
def operacao(op, opnd1, opnd2):
    if op == "+":
        return opnd1 + opnd2
    elif op == "-":
        return opnd1 - opnd2
    elif op == "*":
        return opnd1 * opnd2
    elif op == "/":
        return opnd1 / opnd2
    elif op == "**":
        return opnd1 ** opnd2
    else:
        return False 

   
# função que calcula a partir da pos fixa
# infelizmente, eu tive dois problemas nessa etapa que eu não consegui resolver: 
    #1°: eu não consegui resolver um bug para operações com números exponenciais
    #2°: eu não consegui fazer com que as operação fossem realizadas por meio de frações ordinárias 
#Eu vou deixar anexado junto o contido com o erro, ele também não resolver operações exponencias,
#não consegue resolver várias operações simulatenas, porém devolvia o resultado em fração ordinária

def CalcPosFixa(listaexp):
    p = Pilha(15000)
    lista =  re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", listaexp)
     
    for i in range(len(lista)):
       
        c = lista[i]
        if c >= '0' and c <= '9999999999':
            p.push(c)
         
        else:
            opnd2 = p.pop()
            opnd1 = p.pop()

            valor = operacao(c,float(opnd1), float(opnd2))

            if valor:                                       # Verifica se o operando é válido   
                p.push(valor)
            else:
                #"Operador invalido" 
                return lista
    
    resultado = p.pop()
    res = resultado.as_integer_ratio()

    if p.vazia():                 # Verifica se ao final a pilha está vazia
        return str(resultado) + " ou a fração " + str(res[0]) + "/" + str(res[1])
    
    else:
        return "Expressao invalida"
           

if __name__ == '__main__':
    # Loop para o programa continuar funcionando ate você digitar fim
    s = input(">>> ")    
    while s != "fim":
        list = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", s)
        posf = TraduzPosFixa(s)
        res_posf = CalcPosFixa(posf)
        print(f' {list} -> TraduzPosFixa: {posf} -> CalcPosFixa: {res_posf}')
        s = input(">>> ")

