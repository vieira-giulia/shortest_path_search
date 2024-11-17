# algorithms/greedy.py
import heapq

# Manhattan distance: |x1 - x2| + |y1 - y2|
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 


def search(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) # Grid bounds
    priority_queue = [(heuristic(start, goal), start, [start])]  # (heuristic_value, current_position, path)
    visited = set() # Visited positions

    while priority_queue:
        # Dequeue node with the smallest heuristic value, and its path
        _, (x, y), path = heapq.heappop(priority_queue)

        # If the goal is reached, return the path and its total cost
        if (x, y) == goal: return path, sum(grid[px][py] for px, py in path)

        # Skip nodes that have already been visited
        if (x, y) in visited: continue

        # Mark current position as visited
        visited.add((x, y))

        # Explore all valid neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # Get observed neighbor's coordinates
            nx, ny = x + dx, y + dy
            
            # Check if neighbor is within bounds and traversable (not `inf` cost)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != float('inf'):
                # Add valid neighbor to the queue
                heapq.heappush(priority_queue, (heuristic((nx, ny), goal), (nx, ny), path + [(nx, ny)]))

    # Return None if no path is found
    return None, float('inf')
