import sys
from algorithms import bfs, ids, ucs, greedy, astar

ALGORITHMS = {
    "bfs": bfs.search,
    "ids": ids.search,
    "ucs": ucs.search,
    "greedy": greedy.search,
    "astar": astar.search,
}

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

    # Selecionar buscador
    search = ALGORITHMS[algorithm]

    # Executa a busca
    path, cost = search(grid, (xi, yi), (xf, yf))
    print(cost, path)

if __name__ == "__main__":
    main()
