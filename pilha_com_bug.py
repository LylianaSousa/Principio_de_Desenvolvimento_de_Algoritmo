# Exercício Programa I - MAC 122 - PDA
#Nome: Lyliana Myllena Santos de Sousa
#NUSP:11223740

#EXERCÍCIO ERRADO, QUE FOI CITADO NOS COMENTÁRIOS DO EXERCÍCIO PARA CORREÇÃO

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

#Função para simplificar o valor da fração obtida
def mdc(n,m):
    resto = n % m 
    while resto != 0:
        n = m 
        m = resto
        resto = n % m
    return m

#Função para testar se o número é inteiro
def inteiro_ou_decimal(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
 
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
class operação:
    # vou considerar que todo numero é uma fraçao, onde para os numero inteiros o seu denominador será sempre 1
    
    #Construtor da classe
    def __init__(self, numerador = 0, denominador = 1):
        #Usarei um if para contornar uma divergência matemática, que aparece quando dividimos por zero
        if denominador == 0:
            raise ValueError("Denominador igual a zero")
        self.num = numerador 
        self.den =  denominador
     
    #Operação soma de duas frações
    def __add__(self, other):
        #Montarei a fração resultante pelo método da borboleta
        xnum = self.num * other.den + self.den * other.num
        xden = self.den * other.den
        xmdc = mdc(xnum, xden)
        return operação(xnum // xmdc, xden // xmdc)
        
    #Operação subtração de duas frações
    def __sub__(self, other):
        #Montarei a fração resultante pelo método da borboleta
        xnum = self.num * other.den - self.den * other.num
        xden = self.den * other.den
        xmdc = mdc(xnum, xden)
        return operação(xnum // xmdc, xden // xmdc)
        
    #Operação multiplicação de duas frações
    def __mul__(self, other):
        #A multiplicação será feita pelo produto dos "semelhantes"
        xnum = self.num * other.num 
        xden = self.den * other.den
        xmdc = mdc(xnum, xden)
        return operação(xnum // xmdc, xden // xmdc) 
        
   #Operação divisão de duas frações
    def __truediv__(self, other):
        #A multiplicação será feita pelo produto dos "opostos"
        xnum = self.num * other.den 
        xden = self.den * other.num
        xmdc = mdc(xnum, xden)
        return operação(xnum // xmdc, xden // xmdc) 
        
    #Operação potenciação de duas frações
    def __pow__(self, n): 
        #Usarei um if para desconsiderar os casos dos números não inteiros
        if inteiro_ou_decimal(n) == 0:
            return str("Expoente não é inteiro")
        xnum = self.num ** n
        xden = self.den ** n
        xmdc = mdc(xnum, xden)
        return operação(xnum // xmdc, xden // xmdc)
    
    
    #Por fim, printarei os resultados
    def __str__(self):
        # Usarei um if para imprimir frações com o denominador 1 como números inteiros
        if self.den == 1:
            return str(self.num)
        if self.num == 0:
            return str(self.num)
         # Usarei um if para imprimir frações com o sinal de negativo aparecer somente uma vez e na frente do numerador
        if self.den < 0:
            return str(((-1)*self.num)) + "/" + str(((-1)*self.den))
        return str(self.num) + "/" + str(self.den)
        
def operacao(op,x_class, y_class):
    opnd1 = x_class.split("/")
    opnd2 = y_class.split("/")

    if len(opnd1) == 1 and len(opnd2) == 1:
        x = int(x_class)
        y = int(y_class)
        if op == "+":
            res = operação(x) + operação(y)
            return res
        
        elif op == "-":
            res = operação(x) - operação(y)
            return res
        
        elif op == "*":
            res = operação(x) * operação(y)
            return res
        
        elif op == "/":
            res = operação(x) / operação(y)
            return res
        
        elif op == "**":
            res = operação(x) ** operação(y)
            return res
        else:
            return False

    elif len(opnd1) == 1 and len(opnd2) == 2:
        x = int(x_class)
        y1 = int(opnd2[0])
        y2 = int(opnd2[1])
        if op == "+":
            res = operação(x) + operação(y1,y2)
            return res
        
        elif op == "-":
            res = operação(x) - operação(y1,y2)
            return res
        
        elif op == "*":
            res = operação(x) * operação(y1,y2)
            return res
        
        elif op == "/":
            res = operação(x) / operação(y1,y2)
            return res
        
        elif op == "**":
            res = operação(x) ** operação(y1,y2)
            return res
        else:
            return False
   
    elif len(opnd1) == 2 and len(opnd2) == 1:
        x1 = int(opnd1[0])
        x2 = int(opnd1[1])
        y = int(y_class)
        if op == "+":
            res = operação(x1,x2) + operação(y)
            return res
        
        elif op == "-":
            res = operação(x1,x2) - operação(y)
            return res
        
        elif op == "*":
            res = operação(x1,x2) * operação(y)
            return res
        
        elif op == "/":
            res = operação(x1,x2) / operação(y)
            return res
        
        elif op == "**":
            res = operação(x1,x2) ** operação(y)
            return res
        else:
            return False
        
    elif len(opnd1) == 2 and len(opnd2) == 2:
        x1 = int(opnd1[0])
        x2 = int(opnd1[1])
        y1 = int(opnd2[0])
        y2 = int(opnd2[1])
        if op == "+":
            res = operação(x1,x2) + operação(y1,y2)
            return res
        
        elif op == "-":
            res = operação(x1,x2) - operação(y1,y2)
            return res
        
        elif op == "*":
            res = operação(x1,x2) * operação(y1,y2)
            return res
        
        elif op == "/":
            res = operação(x1,x2) / operação(y1,y2)
            return res
        
        elif op == "**":
            res = operação(x1,x2) ** operação(y1,y2)
            return res
        else:
            return False 
# função que calcula a partir da pos fixa
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

            valor = operacao(c,opnd1, opnd2)

            if valor:                                       # Verifica se o operando é válido   
                p.push(valor)
            else:
                #"Operador invalido" 
                return lista
    resultado = p.pop()

    if p.vazia():                 # Verifica se ao final a pilha está vazia
        return resultado
    else:
        return "Expressao invalida"
    

if __name__ == '__main__':
    # teste ['(2 +52)* (3 - 51/31)']
    s = input(">>> ")    
    while s != "fim":
        list = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", s)
        posf = TraduzPosFixa(s)
        res_posf = CalcPosFixa(posf)
        print(f' {list} -> TraduzPosFixa: {posf} -> CalcPosFixa: {res_posf}')
        s = input(">>> ")
    

         
