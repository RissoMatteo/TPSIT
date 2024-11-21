import pygame
from pygame.locals import *
import sys

def calc_pav():
    mat = [] 
    with open("percorso.csv", "r") as f:
        for riga in f.readlines():
            riga = riga.split(",")
            mat.append([int(c) for c in riga])
    return mat

def sceltaNodo(nonVisitati, label):
    minLabel = sys.maxsize
    minNodo = None
    for nodo in nonVisitati:
        labelNodo = label[nodo]
        if labelNodo < minLabel:
            minLabel = labelNodo
            minNodo = nodo
    return minNodo

def djkstra(node_sorgente, matrice):
    n_nodi = len(matrice)
    predecessori = {}
    nonVisitati = set([i for i in range(0, n_nodi)])
    label = {i : sys.maxsize for i in range(0, n_nodi)}
    label[node_sorgente] = 0
    while len(nonVisitati) > 0:
        nodo_corrente = sceltaNodo(nonVisitati, label)
        if nodo_corrente is None:
            break
        nonVisitati.remove(nodo_corrente)
        for nodoVicino, peso in enumerate(matrice[nodo_corrente]):
            if peso > 0:
                nuovaLabel = label[nodo_corrente] + peso
                if nuovaLabel < label[nodoVicino]:
                    predecessori[nodoVicino] = nodo_corrente  # Aggiorna il predecessore corrente
                    label[nodoVicino] = nuovaLabel
    print(f"prede {predecessori}")
    return label, predecessori


def main():
    lato_x = 100
    lato_y = 100
    
    # Load the map from a file
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)]
    k = 0

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x, n_y * lato_y))
    muro = pygame.image.load("muro1.png")
    strada = pygame.image.load("strada1.png")
    robot = pygame.image.load("robot.png")
    font = pygame.font.Font(None, 36) 

    # Build adjacency information
    diz = {}
    cont = 0
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonne, casella in enumerate(riga): #trova celle libere
            if casella == 0:
                cont = cont + 1
                matrice[indice_riga][indice_colonne] = cont
    
    for indice_riga, riga in enumerate(matrice):
        for indice_colonna, casella in enumerate(riga):
            if casella != -1:
                adiacenti = []
                if indice_colonna + 1 < len(riga) and matrice[indice_riga][indice_colonna + 1] != -1: #destra
                    adiacenti.append(matrice[indice_riga][indice_colonna + 1])
                if indice_colonna - 1 >= 0 and matrice[indice_riga][indice_colonna - 1] != -1: #sinistra
                    adiacenti.append(matrice[indice_riga][indice_colonna - 1])
                if indice_riga - 1 >= 0 and matrice[indice_riga - 1][indice_colonna] != -1: #sopra
                    adiacenti.append(matrice[indice_riga - 1][indice_colonna])
                if indice_riga + 1 < len(matrice) and matrice[indice_riga + 1][indice_colonna] != -1: #sotto
                    adiacenti.append(matrice[indice_riga + 1][indice_colonna])
                diz[casella] = adiacenti

    # Construct the matrix of weights based on adjacency information
    #matricePesi = [[0 if casella == -1 else (1 if casella in diz[casella] else 0) for casella in riga] for riga in matrice]
    numCelleLibere=max(diz.keys())
    matricePesi= [[0]*numCelleLibere for _ in range(numCelleLibere)]
    for i in range(numCelleLibere):
        for j in range(numCelleLibere):
            if j+1 in diz[i+1]:
                matricePesi[i][j]=1
            


    print(f"matricePesi: {matricePesi}")    
    print(f"matriceIniziale: {matrice}")
    print(f"dizionario: {diz}")

    # Run Dijkstra's algorithm
    start = 0
    end = 24
    label, predecessori = djkstra(start, matricePesi)
    print(f"predecessori: {predecessori}")
    print(f"label:{label}")

    # Calculate the shortest path
    shortest_path = []
    node = end
    if node in predecessori or node == start:  # Verifica se il nodo finale è raggiungibile o se è già il nodo di partenza
        while node != start:
            shortest_path.append(node)
            node = predecessori.get(node)  # Use .get() to handle KeyError
            if node is None:
                break
        if node is not None:
            shortest_path.append(node)
            shortest_path.reverse()
            print("Shortest Path:", shortest_path)
        else:
            print("No path found from start to end.")
    else:
        print("eppa No path found from start to end.")


    # Uncomment this block for Pygame event handling
# Display the map
    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            if k in shortest_path:
                text = font.render(f"{k}", True, (0, 255, 0))
            else:
                text = font.render(f"{k}", True, (0, 0, 0))
            if casella == 1:
                surf1.blit(muro, (0, 0))
                screen.blit(surf1, (lato_x - 100, lato_y - 100))  
            else:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x - 50, lato_y - 50))  
                screen.blit(surf1, (lato_x - 100, lato_y - 100))  
                screen.blit(text, text_pos)
                k += 1
            
            pygame.display.flip()
            lato_x += 100
            
        lato_x = 100
        lato_y += 100
        screen.blit(robot, (10, 10))
    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()


if __name__ == "__main__":
    main()