import sys
from algorithms import bfs, ids, ucs, greedy, astar


TERRAIN_COSTS = {
    '.': 1.0,  # Grama
    ';': 1.5,  # Grama alta
    '+': 2.5,  # Água
    'x': 6.0,  # Fogo
    '@': float('inf')  # Parede
}

def parse_map(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    dimensions = lines[0].split()
    w, h = int(dimensions[0]), int(dimensions[1])

    grid = []
    for line in lines[1:h + 1]: grid.append([TERRAIN_COSTS[char] for char in line.strip()])
    
    return grid


def main():
    if len(sys.argv) != 7:
        print("Uso: python main.py [arquivo_mapa] [algoritmo] xi yi xf yf")
        sys.exit(1)

    file_path = sys.argv[1]
    algorithm = sys.argv[2].lower()
    xi, yi, xf, yf = map(int, sys.argv[3:])

    # Carrega o mapa
    grid = parse_map(file_path)

    # Seleciona o algoritmo
    algorithms = {
        "bfs": bfs.search,
        "ids": ids.search,
        "ucs": ucs.search,
        "greedy": greedy.search,
        "astar": astar.search,
    }

    if algorithm not in algorithms:
        print("Algoritmo inválido. Escolha entre: bfs, ids, ucs, greedy, astar.")
        sys.exit(1)

    # Executa a busca
    path, cost = algorithms[algorithm](grid, (xi, yi), (xf, yf))
    print(cost, path)

if __name__ == "__main__":
    main()
