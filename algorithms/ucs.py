# algorithms/ucs.py
import heapq

def search(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) # Grid bounds
    priority_queue = [(0, start, [start])]  # (cost, current_position, path)
    visited = set()  # Visited positions

    while priority_queue:
        # Dequeue cheapest node and its path
        cost, (x, y), path = heapq.heappop(priority_queue)

        # If the goal is reached, return the path and its total cost
        if (x, y) == goal: return path, grid[x][y] + cost

        # Mark current position as visited
        visited.add((x, y))

        # Explore all valid neighbors (up, down, right, left)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Get observed neighbor's coordinates
            nx, ny = x + dx, y + dy
            
            # Check if neighbor is within bounds and traversable (not `inf` cost)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != float('inf'): 
                # Add neighbors that have not been visited to queue
                if (nx, ny) not in visited: heapq.heappush(priority_queue, (cost + grid[nx][ny], (nx, ny), path + [(nx, ny)]))

    return None, float('inf')
