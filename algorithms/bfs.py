# algorithms/bfs.py
from collections import deque

def search(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) # Grid bounds
    queue = deque([(start, [start])])  # (current_position, path)
    visited = set() # Visited positions

    # Loop until there are no nodes to explore
    while queue:
        # Dequeue current node and its path
        (x, y), path = queue.popleft()

        # If the goal is reached, return the path and its total cost
        if (x, y) == goal: return path, sum(grid[px][py] for px, py in path)

        # Mark current position as visited
        visited.add((x, y))

        # Explore all valid neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # Get observed neighbor's coordinates
            nx, ny = x + dx, y + dy
            
            # Check if neighbor is within bounds and traversable (not `inf` cost)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != float('inf'):
                # Add neighbors that have not been visited to queue
                if (nx, ny) not in visited: queue.append(((nx, ny), path + [(nx, ny)]))

    # Return None if no path is found
    return None, float('inf')
