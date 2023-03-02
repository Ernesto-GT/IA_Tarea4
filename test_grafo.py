import grafo as GR


# Grafo ejemplo con listas de adyacencia
grafo = {'A': ['B', 'C', 'D'],
         'B': ['A', 'C'],
         'C': ['A', 'B', 'D'],
         'D': ['A', 'C']}

def testGrafo():
    g = GR.Graph(grafo)         # Crear el grafo con el diccionario de ejemplo

    print('Grafo')
    print(g)                    # Visualizar el grafo
    print('Iteración')
    for n in g:                 # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos
    print('Arcos:', g.edges())  # Visualizar todos los arcos
    print('Arcos desde el nodo C:', g.edges('C'))   # Arcos desde un nodo

    print('\nComprobaciones')
    print('Vacío:', g.isEmpty())                    # Comprobar si grafo vacío

if __name__ == '__main__':
    testGrafo()