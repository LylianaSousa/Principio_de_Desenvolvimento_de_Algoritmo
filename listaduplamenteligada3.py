
        
class ListaDuplamenteLigada:
    class Node:
        
        __slots__ = 'valor', 'anterior', 'proximo'
         
        def __init__(self, valor, ante, prox):
            self.valor = valor
            self.anterior = ante
            self.proximo = prox
        
        def __str__(self):
                    
            return str(self.valor)
        
    def __init__(self):
        self.primeiro = self.Node(None, None, None)
        self.ultimo = self.Node(None, None, None)
        self.primeiro.proximo = self.ultimo
        self.ultimo.anterior = self.primeiro
        self.tamanho = 0
    
    def __len__(self):
        
        ''' retorna o tamanho da pilha.'''
        
        return self.tamanho
    
    def is_empty(self):
            
        ''' retorna True se pilha vazia'''
        
        return self.tamanho == 0
    
    def Conta(self, x):
        i = 0
        percorre = self.primeiro
        while percorre:
            if str(percorre.valor) == str(x):
                i +=1
            percorre = percorre.proximo
        return i
    
    def Remove(self, x):
        #Remove todos os elementos com info == x da lista duplamente ligada LA e retorna quantos valores forma deletados
        i = 0
        percorre = self.primeiro.proximo
        while percorre != None and percorre.valor != x:
            percorre = percorre.proximo
            if percorre.valor == x:
                i +=1 
                self.tamanho -= 1
                if percorre.anterior is not None:
                    
                    self.primeiro = percorre.proximo
                    percorre.proximo.anterior = percorre.anterior
                else:
                     
                    percorre.anterior.proximo = percorre.proximo
                    percorre.proximo.anterior = percorre.anterior
                    
            percorre = percorre.proximo
                 
        return i

    def Remove(self,x):
        n = self.Conta(x)
        i = 0
        for i in range(n):
            if self.is_empty():
                return None
            percorre = self.primeiro.proximo
            while percorre != None and percorre.valor != x:
                percorre = percorre.proximo
            if percorre ==  None:
                return None
            elif percorre.proximo == None:
                x = percorre.valor
                percorre.anterior.proximo = None
                self.ultimo = percorre.anterior
                i += 1
                del percorre
            else:
                x = percorre.valor
                percorre.proximo.anterior = percorre.anterior
                percorre.anterior.proximo = percorre.proximo
                del percorre
                
        return x

    def __str__(self):
        # Mostra os elementos da lista duplamente ligada, mostrando também o anterior e o sucessor.
        valor = 'Nó ' + ' Anterior ' + ' Informação ' + ' Posterior \n'
        n = 2 + self.tamanho
        no = list(range(1,n+1,1))
        i = 0
        if self.primeiro is not None:
            percorre = self.primeiro
           
            while percorre.proximo:
              
                percorre = percorre.proximo
                valor += '\n'
                valor += " " + str(no[i]) + "   " + str(percorre.anterior) + "       " + str(percorre.valor) + "        " + str(percorre.proximo)
                i += 1
                
           
            valor += '\n' +" " + str(no[i]) + "   " + str(percorre.valor) + "      " + str(percorre.proximo) + "        " + str(None)
                
            
        return valor
    
    def Adiciona(self, valor):
        #até agora ela ós adiciona no final 
        #comparacao = self.Busca(valor)
        #print(comparacao)
        
        #até agora ela ós adiciona no final
        if self.primeiro:
                #vou criar a função busca para ela fornecer o  aux e o ant
                aux = self.primeiro
                ant = None
                while aux.proximo:
                    ant = aux
                    aux = aux.proximo
                aux.proximo = self.Node(valor,ant, None)
                #print('entrei1')
                aux.proximo.anterior = aux
                aux.anterior = ant
                if self.ultimo:
                    self.ultimo = aux.proximo
        else:
                self.primeiro = self.Node(valor,ant, None)
                self.ultimo = self.Node(valor,ant, None)
       
        self.tamanho += 1

    def Busca(self,val):
        percorre = self.primeiro
        while percorre:
            if percorre.valor == val:
                return [str(percorre.anterior), str(percorre.proximo)]
            else:
                percorre = percorre.proximo
        return ['None', 'None']
        
if __name__ == "__main__":      
    lista = ListaDuplamenteLigada()
    print(lista)
    print("--------------------------------")
    lista.Adiciona("Antonio")
    print(lista)
    print("--------------------------------")
    lista.Adiciona("Maria")
    print(lista)
    print("--------------------------------")
    lista.Adiciona("Ana")
    print(lista)
    print("--------------------------------")
    lista.Adiciona("Antonio")
    print(lista)
    print("--------------------------------")
    print('quantas vezes aparece: Antonio ->',lista.Conta('Antonio'))
    print("--------------------------------")
    print('quantas vezes aparece: Ana ->',lista.Conta('Ana'))
    print(lista.Busca("Antonio"))
    print("--------------------------------")
    lista.Adiciona("Ana")
    print(lista)
    print("--------------------------------")
    lista.Remove("Antonio")
    print(lista)
    print("--------------------------------")
  