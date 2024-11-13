def traveling_salesman(graph, start):
    # Get all vertices except the starting point
    vertices = list(range(len(graph)))
    vertices.remove(start)
    
    # Initialize minimum path and cost
    min_path = None
    min_cost = float('inf')
    
    def calculate_path_cost(path):
        # Calculate total cost of a path
        cost = 0
        prev = start
        for vertex in path:
            cost += graph[prev][vertex]
            prev = vertex
        cost += graph[prev][start] # Return to start
        return cost
    
    def permutations(vertices, path=[]):
        nonlocal min_path, min_cost
        
        if not vertices:
            # Calculate cost of current path
            current_cost = calculate_path_cost(path)
            
            # Update minimum if current is better
            if current_cost < min_cost:
                min_cost = current_cost
                min_path = path[:]
            return
            
        # Try all possible next cities
        for i, vertex in enumerate(vertices):
            remaining = vertices[:i] + vertices[i+1:]
            permutations(remaining, path + [vertex])
    
    # Find best path
    permutations(vertices)
    
    # Format result
    complete_path = [start] + min_path + [start]
    return complete_path, min_cost

# Example usage:
if __name__ == "__main__":
    # Example graph represented as adjacency matrix
    # graph[i][j] represents the distance between cities i and j
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    start = 0  # Starting city
    
    path, cost = traveling_salesman(graph, start)
    print(f"Shortest path: {path}")
    print(f"Total cost: {cost}")
