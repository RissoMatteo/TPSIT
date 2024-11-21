import threading
import time

saldo = 1000

#oggetto di tipo lock, che è un blocco
blocco = threading.Lock()

class Prelievo(threading.Thread):
    def __init__(self, percentuale):
        super().__init__()
        self.percentuale = percentuale
        
    def run(self):
        global saldo #global permette di modificare saldo dal metodo run
        while True: 
            cifra = self.percentuale * (saldo / 100)
            time.sleep(1)
            
            #fa si che il primo thread che acquisisce la lock, è l'ultimo che opera, lo rilascia quando conclude l'operazione
            #BLOCCANTE
            #mutex = mutuamente esclusivo -> il codice viene eseguito solo da un thread alla volta
            
            blocco.acquire()  #acquisisce la lock7
            saldo = saldo - cifra  #area critica del codice
            blocco.release()  #rilascia la lock
            
            print(f"Il saldo aggiornato è: {saldo}")
            time.sleep(5)
            
def main():
    
    luca = Prelievo(5)  #prelievo
    mario = Prelievo(-6) #versamento
    
    #concorrono all'operazione sulla stessa varibile
    
    #la sezione critica di un thread è la porzione di codice in cui il thread opera in scrittura sulla ridorsa condivisa
    
    #race condition

    mario.start()
    luca.start()
    
    
if __name__ == "__main__":
    main()
      
#Saldo diventa un valore scritto in un file
#Ogni volta che vi opero, apro il file, leggo il valore, lo aggiorno e chiudo il file
#Dentro al Thread implementa meccanismo che impedisca al saldo di diventare negativo
#Creiamo una lista di 10 Thread, ciascuno con percentuale differente, e li eseguiamo
#Dentro la classe Thread implementiamo il metodo kill
#Il main Thread lascia eseguire i Thread per un minuto, li killa e fa la join