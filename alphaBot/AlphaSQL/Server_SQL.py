import socket as sck
import threading as thr
import time
import RPi.GPIO as GPIO  # Libreria per controllare i GPIO del Raspberry Pi
import sqlite3

# Lista per memorizzare i client connessi (non utilizzata, ma qui per estensioni future)
client_list = []

class AlphaBot:  # Classe che rappresenta il robot AlphaBot e ne controlla i movimenti
    def __init__(self, in1=13, in2=12, ena=6, in3=21, in4=20, enb=26):
        # Assegnazione dei pin di controllo per i motori
        self.IN1, self.IN2, self.ENA = in1, in2, ena
        self.IN3, self.IN4, self.ENB = in3, in4, enb

        # Impostazione delle velocità iniziali dei motori
        self.PA = 20  # Velocità motore sinistro
        self.PB = 20  # Velocità motore destro

        # Configurazione dei pin GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        
        # Configurazione PWM per controllo fine della velocità
        self.PWMA = GPIO.PWM(self.ENA, 500)
        self.PWMB = GPIO.PWM(self.ENB, 500)
        self.PWMA.start(self.PA)
        self.PWMB.start(self.PB)
        
        self.stop()  # Ferma il robot all'avvio

    # Metodo per fermare il robot
    def stop(self):
        self.PWMA.ChangeDutyCycle(0)
        self.PWMB.ChangeDutyCycle(0)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    # Metodo per avanzare
    def forward(self, speed=60):
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

    # Metodo per indietreggiare
    def backward(self, speed=60):
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

    # Metodo per girare a sinistra
    def left(self, speed=25):
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

    # Metodo per girare a destra
    def right(self, speed=25):
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

# Configurazione dell'indirizzo e porta per il server
MY_ADDRESS = ("192.168.1.145", 9000)
BUFFER_SIZE = 4096

# Comandi di base utilizzabili dal client
comandi_base = ["w", "a", "s", "d"]

def carica_comandi(cursor):
    """Funzione per caricare comandi aggiuntivi dal database."""
    global comandi_base
    query = '''SELECT tasto FROM Comandi'''
    cursor.execute(query)
    risultati = cursor.fetchall()
    comandi_db = [riga[0] for riga in risultati]
    print("Comandi caricati dal database:", comandi_db)
    comandi_base.extend(comandi_db)  # Aggiunge i comandi dal database alla lista dei comandi di base

def esegui_movimenti(robot, lista_azioni, tempo_rotazione):
    """Esegue i movimenti del robot in base alla lista di azioni."""
    for azione in lista_azioni:
        direzione = azione.get("direzione")
        durata = azione.get("distanza")
        
        # Esegue la direzione corrispondente e attende il tempo necessario
        if direzione == "F":
            print("Muovi avanti")
            robot.forward()
            time.sleep(durata)
            robot.stop()
        elif direzione == "B":
            print("Muovi indietro")
            robot.backward()
            time.sleep(durata)
            robot.stop()
        elif direzione == "L":
            print("Gira sinistra")
            robot.left()
            time.sleep(tempo_rotazione)
            robot.forward()
            time.sleep(durata)
            robot.stop()
        elif direzione == "R":
            print("Gira destra")
            robot.right()
            time.sleep(tempo_rotazione)
            robot.forward()
            time.sleep(durata)
            robot.stop()

def avvio_server():
    """Avvia il server per ricevere comandi dal client e controllare il robot."""
    # Inizializzazione del robot e arresto iniziale
    robot = AlphaBot()
    robot.stop()

    # Creazione e configurazione del socket server
    conn = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    conn.bind(MY_ADDRESS)
    conn.listen()
    
    # Accetta la connessione in entrata
    client, indirizzo_client = conn.accept()
    print(f"Client connesso da {indirizzo_client}")

    # Connessione al database
    db = sqlite3.connect("db_comandi.db")
    cursore = db.cursor()
    carica_comandi(cursore)
    print("Lista completa dei comandi:", comandi_base)

    # Ciclo principale per gestire i comandi ricevuti
    while True:
        messaggio = client.recv(BUFFER_SIZE)
        comando = messaggio.decode()

        # Verifica se il comando è nella lista dei comandi validi
        if comando in comandi_base:
            if comando == "w":
                print("Vai avanti")
                robot.forward()
            elif comando == "s":
                print("Vai indietro")
                robot.backward()
            elif comando == "a":
                print("Gira a sinistra")
                robot.left()
            elif comando == "d":
                print("Gira a destra")
                robot.right()
            elif comando in ["q", "e", "z", "c"]:
                # Per comandi speciali, recupera la sequenza di movimenti dal database
                query_movimento = f'SELECT str_mov FROM Comandi WHERE tasto = "{comando}"'
                cursore.execute(query_movimento)
                db.commit()

                # Recupera e interpreta i movimenti dal risultato del database
                risultato = cursore.fetchone()
                if risultato:
                    stringa_mov = risultato[0]
                    lista_movimenti = [{"direzione": mov[0], "distanza": 1} for mov in stringa_mov.split(";")[1:]]
                    tempo_giro = 0.5  # Tempo di rotazione per le curve
                    esegui_movimenti(robot, lista_movimenti, tempo_giro)
            elif comando.isupper():
                # Se il comando è maiuscolo, ferma il robot
                print("Stop robot")
                robot.stop()

    # Chiusura delle connessioni e pulizia dei GPIO
    client.close()
    conn.close()

# Avvia il server se il file viene eseguito direttamente
if __name__ == "__main__":
    avvio_server()
