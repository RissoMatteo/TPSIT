from tkinter import CENTER
import pygame
import sys
import random

class Snake():
    def __init__(self, screen, snake, snake_direction, snake_size):
        self.screen = screen
        self.snake = snake
        self.snake_direction = snake_direction
        self.snake_size = snake_size

    def drawSnake(self):
        for segment in self.snake: 
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0], segment[1], self.snake_size, self.snake_size)) 
    
    def updateNew_head(self):
        #calcola le nuove cordinate x e y della testa del serprente
        #snake[0][0] prende solamente il valore di x [0][1] prende il valore y
        return (self.snake[0][0] + self.snake_direction[0] * self.snake_size, self.snake[0][1] + self.snake_direction[1] * self.snake_size)
    
    def snakePosition(self, new_head):
        return [new_head] + self.snake[:-1]

class Apple: 
    def __init__(self, screen, apple):
        self.screen = screen
        self.apple = apple

    def drawAppleRandom(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.apple[0], self.apple[1], 20, 20))

    def randomApple(self, size):
        return (random.randint(180 // size, 620 // size) * size,
                random.randint(100 // size, 540 // size) * size)

class PlayGround: 
    def __init__(self, screen): 
        self.screen = screen

    def buildPlayGround(self):
        pygame.draw.rect(self.screen, (0, 0, 255), (170, 90, 480, 10)) 
        pygame.draw.rect(self.screen, (0, 0, 255), (170, 100, 10, 480))
        pygame.draw.rect(self.screen, (0, 0, 255), (170, 580, 480, 10))
        pygame.draw.rect(self.screen, (0, 0, 255), (640, 100, 10, 480))
        title = pygame.image.load("titolo1.png")
        self.screen.blit(title, (340, 10))

    def finalPage(self, font, punt):
        self.screen.fill((255, 255, 255)) 
        text = font.render(f"Punteggio finale: {punt}", True, (0, 0, 0))
        text1 = font.render("Premi [Esc] per uscire", True, (0, 0, 0))
        text2 = font.render("GAME OVER", True, (255, 0, 0))
        text3 = font.render("Premi [R] per ricominciare una nuova partita", True, (0, 0, 0))
        text_pos = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        text_pos1 = text.get_rect(center=(self.screen.get_width() // 2 - 15, self.screen.get_height() // 2 + 30))
        text_pos2 = text.get_rect(center=(self.screen.get_width() // 2 + 30, self.screen.get_height() // 2 - 30))
        text_pos3 = text.get_rect(center=(self.screen.get_width() // 2 - 140, self.screen.get_height() // 2 + 60))
        self.screen.blit(text, text_pos)
        self.screen.blit(text1, text_pos1)
        self.screen.blit(text2, text_pos2)
        self.screen.blit(text3, text_pos3)
        pygame.display.flip()

        #gestione uscita con esc e restart partita con r
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        return True
    
class Player:
    def __init__(self, snake_direction):
        self.snake_direction = snake_direction

    def closingPage(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: #gestione chiusura di finestra di gioco 
                    pygame.quit()
                    sys.exit()

    def movementPlayer(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.snake_direction[1] == 0:
            self.snake_direction = (0, -1)
        elif keys[pygame.K_DOWN] and self.snake_direction[1] == 0:
            self.snake_direction = (0, 1)
        elif keys[pygame.K_LEFT] and self.snake_direction[0] == 0:
            self.snake_direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and self.snake_direction[0] == 0:
            self.snake_direction = (1, 0)
        return self.snake_direction

class Game: 
    def __init__(self, screen_width, screen_height, fps, white):
        self.screen_width = screen_width #larghezza
        self.screen_height = screen_height #altezza
        self.fps = fps #fps game
        self.white = white #color screen

    def play(self):
        #creazione finestra di gioco 
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("SNAKE")
        font = pygame.font.Font(None, 36)

        #inizializzazione dimensione serpente
        snake_direction = (1, 0)
        snake = [(200, 100)]
        snake_size = 20
        punt = 0

        #inizializzazione dimensione mela causale
        apple = (200, 200)

        clock = pygame.time.Clock()
        while True:

            #creazione degli oggetti serprente, mela, campo e giocatore
            snakeObject = Snake(screen, snake, snake_direction, snake_size)
            appleObject = Apple(screen, apple)
            playGround = PlayGround(screen)
            player = Player(snake_direction)

            player.closingPage()
            snake_direction = player.movementPlayer()
            
            new_head = snakeObject.updateNew_head()
            snake = snakeObject.snakePosition(new_head)

            #verifica collisioni con la mela
            if new_head == apple:
                apple = appleObject.randomApple(snake_size)
                snake.append(snake[-1]) #aggiunge alla coda del serprente
                punt += 1

            # Verifica collisione con i confini
            if not (160 <= new_head[0] < 650 and 80 <= new_head[1] < 600): #160-650 80-600
                if playGround.finalPage(font, punt):
                    Game.play(self)
                else:
                    pygame.quit()
                    sys.exit()

            # Verifica collisione con il corpo del serpente
            if new_head in snake[2:]: 
                if playGround.finalPage(font, punt):
                    Game.play(self)
                else:
                    pygame.quit()
                    sys.exit()

            screen.fill(self.white)

            textScore = font.render(f"Punteggio: {punt}", True, (250, 0, 0))
            screen.blit(textScore, (10, 15)) 
            #creazione campo da gioco ed elementi interni
            snakeObject.drawSnake()
            appleObject.drawAppleRandom()
            playGround.buildPlayGround()
            
            #Aggiornamento dello schermo
            pygame.display.flip()
            #Impostazione del frame rate
            clock.tick(self.fps)
        
def main():
    pygame.init()
    game = Game(800, 600, 10, (255, 255, 255))
    game.play()

if __name__ == "__main__":
    main()