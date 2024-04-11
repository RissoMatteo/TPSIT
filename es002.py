import networkx as nx
import matplotlib.pyplot as plt

def stampaGrafoAlbero(albero):
    G = nx.Graph()

    def aggiungi_nodo_e_archi(nodo, parent=None):
        if nodo:
            G.add_node(nodo.valore)
            if parent:
                G.add_edge(parent.valore, nodo.valore)
            aggiungi_nodo_e_archi(nodo.sinistro, nodo)
            aggiungi_nodo_e_archi(nodo.destro, nodo)

    aggiungi_nodo_e_archi(albero)

    pos = nx.spring_layout(G)  # Posizioni dei nodi nel grafico
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title("Albero bilanciato")
    plt.show()

class NodoAlbero:
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

def AlberoBilanciato(lista):
    if not lista:
        return None
    
    lista.sort()  # Ordina la lista [2, 5, 6, 16, 20, 28]
    centro = len(lista) // 2
    radice = NodoAlbero(lista[centro])
    
    radice.sinistro = AlberoBilanciato(lista[:centro])
    radice.destro = AlberoBilanciato(lista[centro + 1:])
    
    return radice

def StampaAlberoInOrdine(nodo):
    if nodo:
        StampaAlberoInOrdine(nodo.sinistro)
        print(nodo.valore, end=' ')
        StampaAlberoInOrdine(nodo.destro)

def main():
    lista = [5, 6, 2, 20, 28, 16]
    albero = AlberoBilanciato(lista)
    print("Albero bilanciato in ordine:")
    StampaAlberoInOrdine(albero)
    stampaGrafoAlbero(albero)

if __name__ == '__main__':
    main()