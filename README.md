# shortest_path_search

python main.c MAP_FILE_PATH ALGORITHM start_x start_y goal_x goal_y

pathfinder/
│
├── main.py               # Arquivo principal para execução do programa.
├── algorithms/           # Pasta para os algoritmos de busca.
│   ├── bfs.py
│   ├── ids.py
│   ├── ucs.py
│   ├── greedy.py
│   └── astar.py
├── README.md             # Instruções para executar o programa.
├── mapas/                # Diretório com mapas teste
└── docs/                 # Documentação.
    └── report.pdf


Here’s a detailed explanation of how each algorithm works, focusing on their mechanics, how they navigate the grid, and their specific strategies for finding the path.

---

### 1. **Breadth-First Search (BFS)**

#### How It Works
- **Mechanism**: BFS explores all nodes at the current "depth" (distance from the start) before moving to nodes at the next depth level.
- **Data Structure**: A **queue** (FIFO) ensures nodes are explored in the correct order.
- **Key Properties**:
  - Explores all possible paths of equal cost before increasing the cost.
  - Guarantees the shortest path in terms of **number of steps** (not cumulative terrain cost).

#### BFS in Action
1. Start at the initial position and enqueue it, marking it as visited.
2. Dequeue the current node and explore its neighbors (up, down, left, right).
3. Add unvisited, valid neighbors to the queue with the updated path.
4. If the goal is reached, return the path and compute the cost.
5. If the queue is empty and the goal is not reached, no solution exists.

#### Strengths and Weaknesses
- **Strengths**: Simple and guarantees the shortest path in terms of steps if terrain costs are uniform.
- **Weaknesses**: Does not account for varying terrain costs and can explore unnecessary nodes.

---

### 2. **Iterative Deepening Search (IDS)**

#### How It Works
- **Mechanism**: IDS is a combination of depth-first search (DFS) and breadth-first search. It performs DFS up to a certain depth, then increases the depth iteratively.
- **Data Structure**: A **stack** is used for DFS traversal.
- **Key Properties**:
  - Avoids high memory usage by limiting the depth of recursion.
  - Guarantees finding the shortest path in terms of **number of steps** (not cumulative terrain cost).

#### IDS in Action
1. Start with a depth limit of 0 and increment it iteratively.
2. Perform DFS from the starting node up to the current depth limit.
3. Explore neighbors recursively, backtracking if the depth limit is exceeded.
4. If the goal is reached within the depth, return the path and compute the cost.
5. If no solution is found at any depth, increase the limit and try again.

#### Strengths and Weaknesses
- **Strengths**: Memory-efficient and guarantees shortest paths in terms of steps for uniform terrains.
- **Weaknesses**: Inefficient for large grids or deep solutions, especially if terrain costs vary.

---

### 3. **Uniform Cost Search (UCS)**

#### How It Works
- **Mechanism**: UCS expands the node with the lowest total path cost (not heuristic). It prioritizes paths with the smallest cumulative cost, considering terrain costs.
- **Data Structure**: A **priority queue** ensures the cheapest node is always expanded first.
- **Key Properties**:
  - Guarantees the optimal path based on terrain costs.
  - Similar to BFS but accounts for variable terrain costs.

#### UCS in Action
1. Start at the initial position with a cumulative cost of 0.
2. Add the starting position to the priority queue.
3. Expand the node with the lowest cost from the queue.
4. For each neighbor:
   - Compute the new cumulative cost (current cost + terrain cost).
   - Add the neighbor to the priority queue if it hasn’t been visited with a lower cost.
5. If the goal is reached, return the path and its cost.

#### Strengths and Weaknesses
- **Strengths**: Guarantees the optimal solution based on terrain costs.
- **Weaknesses**: Can explore unnecessary nodes if the goal is far away.

---

### 4. **Greedy Best-First Search**

#### How It Works
- **Mechanism**: Greedy search expands the node that appears closest to the goal based on a heuristic (e.g., Manhattan distance).
- **Data Structure**: A **priority queue** prioritizes nodes based on the heuristic value.
- **Key Properties**:
  - Does not guarantee the optimal path.
  - Focuses only on getting closer to the goal without considering cumulative costs.

#### Greedy Search in Action
1. Start at the initial position with the heuristic value computed from the goal.
2. Add the starting position to the priority queue.
3. Expand the node with the lowest heuristic value.
4. For each neighbor:
   - Compute the heuristic for the neighbor.
   - Add the neighbor to the priority queue if it hasn’t been visited.
5. If the goal is reached, return the path and compute the cost.

#### Strengths and Weaknesses
- **Strengths**: Fast in practice for finding a path, especially in large grids.
- **Weaknesses**: Can take suboptimal paths or even fail to find a solution if it gets stuck.

---

### 5. **A* Search**

#### How It Works
- **Mechanism**: A* combines UCS and Greedy search by balancing the cumulative cost (from UCS) and the heuristic (from Greedy search).
- **Data Structure**: A **priority queue** prioritizes nodes based on their `f(n)` value:
  - \( f(n) = g(n) + h(n) \)
  - \( g(n) \): Cumulative cost from start to the current node.
  - \( h(n) \): Heuristic estimate from the current node to the goal.
- **Key Properties**:
  - Guarantees the optimal path if the heuristic is **admissible** (never overestimates the true cost).

#### A* in Action
1. Start at the initial position with `f = g + h` (where \( g = 0 \), \( h = heuristic(start, goal) \)).
2. Add the starting position to the priority queue.
3. Expand the node with the lowest `f(n)` value.
4. For each neighbor:
   - Compute the cumulative cost \( g(n) \) and heuristic \( h(n) \).
   - Compute the total cost \( f(n) = g(n) + h(n) \).
   - Add the neighbor to the priority queue if it hasn’t been visited with a lower cost.
5. If the goal is reached, return the path and its cost.

#### Strengths and Weaknesses
- **Strengths**: Efficient and guarantees the optimal solution when the heuristic is admissible.
- **Weaknesses**: Requires a well-designed heuristic; otherwise, performance can degrade.

---

### Comparison of Algorithms

| **Algorithm**        | **Optimal Solution** | **Considers Terrain Costs** | **Heuristic**     | **Performance**                     |
|-----------------------|----------------------|-----------------------------|-------------------|-------------------------------------|
| BFS                  | No (shortest steps)  | No                          | None              | Explores unnecessary nodes.         |
| IDS                  | No (shortest steps)  | No                          | None              | Inefficient for large/deep grids.   |
| UCS                  | Yes                  | Yes                         | None              | Guaranteed optimal but slow.        |
| Greedy Search        | No                  | No                          | Yes (goal-focused)| Fast but not optimal.               |
| A*                   | Yes                  | Yes                         | Yes               | Most efficient with good heuristic. |

Each algorithm has its strengths and is suited to specific types of problems. For grid-based pathfinding with variable terrain costs, **A*** is generally the best choice.

