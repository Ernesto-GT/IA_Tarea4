import grafo_ponderado as GRP
import instance_generator as ig
#import No_informado as ni
import time as tiempo

# Hola Grafo ejemplo con listas de adyacencia y pesos asociados
'''grafo = {'A': [('B', 1), ('C', 2), ('D', 3)],
         'B': [('A', 1), ('C', 4)],
         'C': [('A', 2), ('B', 4), ('D', 5)],
         'D': [('A', 3), ('C', 5)]} '''

'''grafo = {'1': [('2', 4), ('3', 3)],
         '2': [('5', 8)],
         '3': [('4', 12), ('6', 4)],
         '4': [('6', 2), ('7', 20), ('8', 15)],
         '5': [('7', 17)],
         '6': [('8', 22)],
         '7': [('8', 9)],
         '8': [('1', 1)]} '''
#Modifique el grafo de ejemplo para probar mejor Dijkstra, pero el inicial lo guarde en la pestaña "grafo.py"

def testGrafo():
    
    grafo = ig.create_instance(5)
    g = GRP.WeightedGraph(grafo)    # Crear el grafo con el diccionario de ejemplo
    while (len(g.isolatedNodes())>0):
        grafo = ig.create_instance(50);
        g = GRP.WeightedGraph(grafo); 

    print('Grafo')
    print(g)                    # Visualizar el grafo
    """
    print('Iteración')
    for n in g:                 # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    #print('Nodos:', g.nodes())  # Visualizar todos los nodos
    #print('Arcos:', g.edges())  # Visualizar todos los arcos
    #print('Arcos desde el nodo C:', g.edges('C'))   # Arcos desde un nodo
    """
    print('\nComprobaciones')
    print('Vacío:', g.isEmpty())                    # Comprobar si grafo vacío
    
        
     # Obtener el camino más corto entre dos nodos
    tiempo_inicio = tiempo.time()
    path, weight = g.shortestPath('1', '5')
    print("DFS('10'):", g.DFS('1')) 
    tiempo_final = tiempo.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicio
    print('Tiempo de ejecución: ', tiempo_ejecucion)
    print(f'Dijkstra: {path} peso:{weight}')

if __name__ == '__main__':
    testGrafo()