# grafo no dirigido
# admite lazos 
#grafo ejemplo
'''grafo = {'A': [('B', 1), ('C', 2), ('D', 3)],
         'B': [('A', 1), ('C', 4)],
         'C': [('A', 2), ('B', 4), ('D', 5)],
         'D': [('A', 3), ('C', 5)]}'''

class Graph():
    # Constructor, por defecto crea un diccionario vacío
    # El grafo se presenta como un diccionario de la forma
    # {nodo: [arcos]}
    # arcos es una lista de los nodos adyacentes 
    def __init__(self, graph={}):
        self.graph = graph

    # Devuelve una representación formal del contenido del grafo
    def __repr__(self):
        nodes = ''
        for node, edges in self.graph.items():
            nodes += f'{node}: {edges}\n'
        return nodes

    # Iterador para recorrer todos los nodos del grafo
    def __iter__(self):
        self.iter_obj = iter(self.graph)
        return self.iter_obj

    # Devuelve los nodos del grafo como una lista
    def nodes(self):
        return list(self.graph.keys())

    # Devuelve los arcos del grafo como una lista de tuplas
    # (nodo_origen, nodo_destino)
    def edges(self, node=None):
        if node:
            if self.existNode(node):
                return [(node, e) for e in self.graph[node]]
            else:
                return []
        else:
            return [(n, e) for n in self.graph.keys() for e in self.graph[n]]

    # Devuelve una lista de los nodos aislados
    def isolatedNodes(self):
        return [node for node in self.graph if not self.graph[node]]
    '''  
    # Recorrido en profundidad (Depth First Search)
    # comienza en un nodo del grafo y
    # comprueba a todo lo largo de cada arco antes de retroceder
    def DFS(self, node):
        visited = [node]                    # lista de visitados
        stack = [node]                      # pila a tratar
        while stack:                        # mientras haya nodos en la pila
            current = stack.pop()           # sacar nodo de la pila
            if current not in visited:      # si no ha sido visitado
                visited.append(current)     # añadir a visitados
            for e in self.graph[current]:   # para cada nodo adyacente
                if e not in visited:        # si no ha sido visitado
                    stack.append(e)         # añadir a la pila
        return visited                      # devolver el recorrido
    ''' 
    
    # Consulta si el grafo está vacío
    def isEmpty(self):
        return self.graph == {}

    # Consulta si el nodo existe en el grafo
    def existNode(self, node):
        return node in self.graph.keys()
