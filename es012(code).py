class Coda():
    def __init_(self):
        self.lista = []
    
    def is_empty(self):
        if(len(self.lista) == 0):
            return True
        else:
            return False
        
    def enqueue(self, x):
        self.lista.append(x)
        
    def dequeue(self):
        if(self.is_empty()):
            print("Lista vuota, impossibile rimnuovere!")
            return None
        else:
            return self.lista.pop(0)
    
    def print(self):
        print(self.lista)

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 
    text: 
    """
    coda = Coda()
    coda.dequeue()
    coda.enqueue(10)
    coda.enqueue(5)
    coda.print()
    print(f"elemento rimosso: {coda.dequeue()}")
    print(f"elemento rimosso: {coda.dequeue()}")
    print(f"elemento rimosso: {coda.dequeue()}")
    coda.enqueue(39)
    coda.print()
    
if __name__ == '__main__':
    main()