# algorithms/ids.py

def search(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) # Grid bounds

    def dfs_limit(current, path, depth):
        x, y = current
        
        # If the goal is reached, return the path and its total cost
        if (x, y) == goal: return path, sum(grid[px][py] for px, py in path)

        # If the depth limit is reached, no possible path here
        if depth == 0: return None, float('inf')

        # Explore all neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # Compute observed neighbor's coordinates
            nx, ny = x + dx, y + dy
            
            # Check if neighbor is within bounds and traversable (not `inf` cost), and we are not revisinng
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != float('inf') and (nx, ny) not in path:
                # Perform a recursive depth-first search with reduced depth on valid neighbor
                result, cost = dfs_limit((nx, ny), path + [(nx, ny)], depth - 1)
                # If a valid final path is found, leave
                if result: return result, cost
        
        # No valid path found at this depth          
        return None, float('inf')

    # For all possible depths
    for depth in range(rows * cols):
        # Call dfs for that depth
        result, cost = dfs_limit(start, [start], depth)
        # If a valid final path is found, leave
        if result: return result, cost
    
    # Return None if no path is found
    return None, float('inf')
