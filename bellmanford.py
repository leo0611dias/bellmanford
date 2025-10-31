class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def bellman_ford(self, src):
        # Inicialização das distâncias
        dist = {vertex: float('inf') for vertex in self.V}
        dist[src] = 0
        
        # Relaxamento das arestas |V| - 1 vezes
        for _ in range(len(self.V) - 1):
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # Verificação de ciclos de peso negativo
        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("O grafo contém ciclo de peso negativo")
                return None
        
        return dist
    
    def print_solution(self, dist, src):
        print(f"\nCaminhos mais curtos a partir do vértice {src}:")
        print("-" * 40)
        for vertex in self.V:
            if dist[vertex] == float('inf'):
                print(f"{src} → {vertex}: \tNão alcançável")
            else:
                print(f"{src} → {vertex}: \t{dist[vertex]}")

# Criando o grafo baseado na imagem
vertices = ['A', 'B', 'C', 'D']
g = Graph(vertices)

# Adicionando arestas conforme o diagrama
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 6)
g.add_edge('B', 'C', 8)
g.add_edge('B', 'D', 9)
g.add_edge('C', 'D', 2)
g.add_edge('D', 'B', 5)  # Aresta de D para B

# Executando o algoritmo Bellman-Ford
source = 'A'
distances = g.bellman_ford(source)

if distances:
    g.print_solution(distances, source)

# Demonstração passo a passo
print("\n" + "="*50)
print("EXECUÇÃO PASSO A PASSO DO ALGORITMO")
print("="*50)

def bellman_ford_step_by_step(graph, src):
    dist = {vertex: float('inf') for vertex in graph.V}
    dist[src] = 0
    
    print(f"\nInicialização:")
    for v in dist:
        print(f"  dist[{v}] = {dist[v]}")
    
    # Relaxamento |V| - 1 vezes
    for i in range(len(graph.V) - 1):
        print(f"\n--- Iteração {i+1} ---")
        updated = False
        
        for u, v, w in graph.graph:
            old_dist = dist[v]
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                print(f"  Relaxando {u}→{v}: dist[{v}] = min({old_dist}, {dist[u]} + {w}) = {dist[v]}")
                updated = True
            else:
                print(f"  {u}→{v}: sem atualização (dist[{v}] = {old_dist})")
        
        if not updated:
            print("  Nenhuma atualização - convergiu!")
            break
    
    # Verificação de ciclos negativos
    print(f"\n--- Verificação de ciclos negativos ---")
    has_negative_cycle = False
    for u, v, w in graph.graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print(f"  CICLO NEGATIVO DETECTADO: {u}→{v}")
            has_negative_cycle = True
    
    if not has_negative_cycle:
        print("  Nenhum ciclo negativo detectado")
    
    return dist if not has_negative_cycle else None

# Executando passo a passo
step_distances = bellman_ford_step_by_step(g, 'A')
if step_distances:
    print(f"\nRESULTADO FINAL:")
    for vertex in g.V:
        print(f"  dist[{vertex}] = {step_distances[vertex]}")
