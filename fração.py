#Nome: Lyliana Myllena Santos de Sousa
#NUSP:11223740
# Exercícios 1

#Antes de iniciar a nosssa class, definirei algumas funções que nos ajudaram ao longo do exercício

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
     
'''Definindo a classe Fração Ordinária'''
     
class Fração:
   
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
        return Fração(xnum // xmdc, xden // xmdc)
        
    #Operação subtração de duas frações
    def __sub__(self, other):
        #Montarei a fração resultante pelo método da borboleta
        xnum = self.num * other.den - self.den * other.num
        xden = self.den * other.den
        xmdc = mdc(xnum, xden)
        return Fração(xnum // xmdc, xden // xmdc)
        
    #Operação multiplicação de duas frações
    def __mul__(self, other):
        #A multiplicação será feita pelo produto dos "semelhantes"
        xnum = self.num * other.num 
        xden = self.den * other.den
        xmdc = mdc(xnum, xden)
        return Fração(xnum // xmdc, xden // xmdc) 
        
   #Operação divisão de duas frações
    def __truediv__(self, other):
        #A multiplicação será feita pelo produto dos "opostos"
        xnum = self.num * other.den 
        xden = self.den * other.num
        xmdc = mdc(xnum, xden)
        return Fração(xnum // xmdc, xden // xmdc) 
        
    #Operação potenciação de duas frações
    def __pow__(self, n): 
        #Usarei um if para desconsiderar os casos dos números não inteiros
        if inteiro_ou_decimal(n) == 0:
            return str("Expoente não é inteiro")
        xnum = self.num ** n
        xden = self.den ** n
        xmdc = mdc(xnum, xden)
        return Fração(xnum // xmdc, xden // xmdc)
    #Iniciarei as operações de comparação
    
    #Operação de comparação se duas frações são iguais
    def __eq__(self, other):
        pri_fator = self.num * other.den
        seg_fator = self.den * other.num
        return pri_fator == seg_fator
    
    #Operação de comparação se a < b (menor)
    def __lt__(self, other):
        pri_fator = self.num * other.den
        seg_fator = self.den * other.num
        return pri_fator < seg_fator
    
     #Operação de comparação se a <= b (menos igual)
    def __le__(self, other):
        pri_fator = self.num * other.den
        seg_fator = self.den * other.num
        return pri_fator <= seg_fator
    
    #Operação de comparação se a > b (maior)
    def __gt__(self, other):
        pri_fator = self.num * other.den
        seg_fator = self.den * other.num
        return pri_fator > seg_fator
    
    #Operação de comparação se a >= b (maior igual)
    def __ge__(self, other):
        pri_fator = self.num * other.den
        seg_fator = self.den * other.num
        return pri_fator >= seg_fator
    
    #Operação de comparação se a != b (difernete)
    def __ne__(self, other):
        pri_fator = self.num * other.den
        seg_fator = self.den * other.num
        return pri_fator != seg_fator
    
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
        
#Testando 

if __name__ == '__main__':
    
    # Programa principal de teste da classe Fração
    x = Fração(-2)
    y = Fração(1, -2)
    z = x + y
    w = Fração(15)
    print(w)
    print(z)
    print (x < y or x < z)
    print (y - z * x)
    print (x ** 3)
    print (x * y + z)