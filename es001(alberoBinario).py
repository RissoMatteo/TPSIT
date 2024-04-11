class Node():
    def __init__(self, val):
        self.val = val
        self.sinistro = None
        self.destro = None
    def inserisci(self, val):
        if self.val is not None:
            #capire se inserire valore in figlio sinistro o destro
            if val < self.val and self.sinistro is None:
                self.sinistro = Node(val)
            elif val < self.val and self.sinistro is not None:
                self.sinistro.inserisci(val)
            elif val > self.val and self.destro is None:
                self.destro = Node(val)
            elif val > self.val and self.destro is not None:
                self.destro.inserisci(val)
        else:
            self.val = val
    def stampa(self):
        if self.val is not None:
            if self.sinistro is not None:
                self.sinistro.stampa()
            print(self.val)
            if self.destro is not None:
                self.destro.stampa()
        else:
            print("Nessun elemento")
    def find(self, val):
        if self.val is not None:
            if val == self.val:
                return True
            elif val < self.val and self.sinistro is not None:
                return self.sinistro.find(val)
            elif val > self.val and self.destro is not None:
                return self.destro.find(val)
            else:
                return False
        else:
            return False        
def main():
    n = Node(5)
    n.inserisci(6)
    n.inserisci(2)
    n.inserisci(20)
    n.inserisci(28)
    n.inserisci(16)
    n.stampa()
    if(n.find(3)):
        print("Trovato")
    else:
        print("Non trovato")
    if(n.find(2)):
        print("Trovato")
    else:
        print("Non trovato")
        
    if(n.find(16)):
        print("Trovato")
    else:
        print("Non trovato")
    
if __name__ == '__main__':
    main()