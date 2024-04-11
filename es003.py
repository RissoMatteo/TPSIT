class Node():
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

    def inserisci(self, valore):
        if self.valore is not None:
            #capire se inserire valore in figlio sinistro o destro
            if self.valore > valore:
                if self.sinistro == None:
                    self.sinistro = Node(valore)
                else:
                    self.sinistro.inserisci(valore)

            elif self.valore < valore:
                if self.destro == None:
                    self.destro = Node(valore)
                else:
                    self.destro.inserisci(valore)

        else: self.valore = valore
    
    def print_tree(self):
        #stampa solo i valori
        print(self.valore)
        
        if(self.sinistro != None):
            self.sinistro.print_tree()
            
        if(self.destro != None):
            self.destro.print_tree()

    def cercaValore(self, valore):
        #restituisce true o false
        if self.valore is not None:
            if valore == self.valore:
                return True
            elif(valore < self.valore):
                    if(self.sinistro != None):
                        return self.sinistro.cercaValore(valore)

            elif(valore > self.valore):
                if (self.destro != None):
                    return self.destro.cercaValore(valore)

            else:
                return False   
        else: 
            return False
        
    
    def isBilanciato(self):
        #ritorna se il numero è bilanciato
        #fase 1: dato un albero contare i nodi
        #fase 2: trovare l'altezza(calcolare il massimo c'è la funzione max)

        pass


def alberoBilanciato(lista,n):
    centro = len(lista)//2
    #print(lista)
    n.inserisci(lista[centro])
    if centro != 0:
        listaSx = lista[0 : centro]
        listaDx = lista[centro+1 :]
        if len(listaSx) > 0:
            alberoBilanciato(listaSx, n)
        if len(listaDx) > 0:
            alberoBilanciato(listaDx, n)
    else:
        return None

def main():
    """n = Node(5)
    n.inserisci(6)
    n.inserisci(2)
    n.inserisci(10)
    n.inserisci(28)
    n.inserisci(16)
    n.inserisci(4)
    n.print_tree()
    if (n.cercaValore(7)):
        print("Trovato")
    else:
        print("Non trovato")

    if (n.cercaValore(3)):
        print("Trovato")
    else:
        print("Non trovato")
"""
    n1 = Node(None)
    lista = [5, 6, 2, 20, 28, 16]
    lista.sort()
    alberoBilanciato(lista, n1)
    n1.print_tree()

if __name__ == '_main_':
    main()