# algorithms/ids.py

def search(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) # Grid bounds

    def dfs_limit(current, path, depth, visited):
        x, y = current
        
        # If the goal is reached, return the path and its total cost
        if (x, y) == goal: return path, sum(grid[px][py] for px, py in path)

        # If the depth limit is reached, no possible path here
        if depth == 0: return None, float('inf')

        # Mark current position as visited
        visited.add((x, y))

        # Explore all neighbors (up, down, right, left)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Compute observed neighbor's coordinates
            nx, ny = x + dx, y + dy
            
            # Check if neighbor is within bounds and traversable (not `inf` cost)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != float('inf'):
                # Skip neighbors that have already been visited
                if (nx, ny) not in visited:
                    # Perform a recursive depth-first search with reduced depth on valid neighbor
                    result, cost = dfs_limit((nx, ny), path + [(nx, ny)], depth - 1, visited)
                    # If a valid final path is found, leave
                    if result: return result, cost
        
        # No valid path found at this depth          
        return None, float('inf')

    # For all possible depths
    for depth in range(rows * cols):
        visited = set() # Visited positions
        # Call dfs for that depth
        result, cost = dfs_limit(start, [start], depth, visited)
        # If a valid final path is found, leave
        if result: return result, cost
    
    # Return None if no path is found
    return None, float('inf')
