# algorithms/astar.py
import heapq

# Manhattan distance: |x1 - x2| + |y1 - y2|
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def search(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) # Grid bounds
    priority_queue = [(0 + heuristic(start, goal), start, [start], 0)]  # (cost + heuristic_value, current_position, path, cost)
    visited = set() # Visited position
    costs = {start: 0}  # cost of shortest path to node

    while priority_queue:
        # Dequeue node with the smallest heuristic value, its path and its cost
        _, (x, y), path, cost = heapq.heappop(priority_queue)

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
                if (nx, ny) not in visited:
                    # Calculate the new cost to reach this neighbor
                    new_cost = cost + grid[nx][ny]
                
                    # If the new cost to this neighbor is cheaper than the previous cost
                    if (nx, ny) not in costs or new_cost < costs[(nx, ny)]:
                        # Store cheapest cost
                        costs[(nx, ny)] = new_cost
                        # Calculate the new cost to reach this neighbor
                        heapq.heappush(priority_queue, (new_cost + heuristic((nx, ny), goal), (nx, ny), path + [(nx, ny)], new_cost))

    # Return None if no path is found
    return None, float('inf')
