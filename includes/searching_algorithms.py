import heapq

class Algorithms:
    def __init__(self):
        pass

    def BFS(graph: dict, start: str, goal: str) -> list[str]:
        """
        Breadth First Search Algorithm

        Args:
            graph (dict): Graph representation
            start (str): Starting node
            goal (str): Goal node
        Returns:
            str: Path from start to goal
        """

        visited = [] # Explored set
        queue = [(start, [start])] # fronter

        while queue:
            current_node, path = queue.pop(0)

            if current_node == goal:
                return path  # Goal found, return the path

            visited.append(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited :
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

        return None  # If the goal is not reached

    def UCS(graph: dict, start:str, goal:str) -> list[str]:
        """
        Uniform Cost Search Algorithm

        Args:
            graph (dict): Graph representation
            start (str): Starting node
            goal (str): Goal node
        Returns:
            str: Path from start to goal
        """
        priority_queue = [(0, start, [])]  # Each element is a tuple (cost, node, path)
        visited = []

        while priority_queue:
            current_cost, current_node, path_so_far = heapq.heappop(priority_queue)

            if current_node == goal:
                return current_cost, path_so_far + [current_node]  # Return cost and path

            if current_node in visited:
                continue

            visited.append(current_node)

            for neighbor, cost in graph[current_node].items():
                if neighbor not in visited:
                    total_cost = current_cost + cost
                    heapq.heappush(priority_queue, (total_cost, neighbor, path_so_far + [current_node]))

        return None, []  # Return none if no path is found

    def DFS(graph: dict, start:str, goal:str) -> list[str]:
        """
        Depth First Search Algorithm

        Args:
            graph (dict): Graph representation
            start (str): Starting node
            goal (str): Goal node

        Returns:
            str: Path from start to goal
        """
        stack = [(start, [start])]
        visited = []

        while stack:
            #print(stack)
            current_node, path = stack.pop()

            if current_node == goal:
                return path

            if current_node in visited:
                continue

            visited.append(current_node)

            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited :
                    stack.append((neighbor, path + [neighbor]))

        return None

    def DLS(graph: dict, start:str, goal:str, depth_limit:int) -> list[str]:
        """
        Depth Limited Search Algorithm

        Args:
            graph (dict): Graph representation
            start (str): Starting node
            goal (str): Goal node

        Returns:
            str: Path from start to goal
        """
        stack = [(start, [start], 0)]
        visited = []

        while stack:
            current_node, path, depth = stack.pop()
            if current_node == goal:
                return path

            if depth < depth_limit:

                if current_node in visited:
                    continue

                visited.append(current_node)
                for neighbor in reversed(graph[current_node]):
                    if neighbor not in visited :
                        stack.append((neighbor, path + [neighbor], depth + 1))

        return

    def IDDFS(graph: dict, start:str, goal:str) -> list[str]:
        """
        Performs an Iterative Deepening Depth-First Search (IDDFS) on a graph.

        Args:
            graph (dict): The graph represented as a dictionary.
            start (str): The starting node.
            goal (str): The goal node.

        Returns:
            list[str]: The path from the starting node to the goal node, if it exists. Otherwise, returns None.
        """
        depth_limit = 0
        while True:
            path = Algorithms.DLS(graph, start, goal, depth_limit)

            if path is not None:
                return path

            depth_limit += 1
    
    def BDS(graph: dict, start: str, goal: str) -> list[str]:
        """
        Bidirectional Search (BDS) algorithm to find the shortest path between two nodes in a graph.

        Args:
            graph (dict): The graph represented as a dictionary where the keys are nodes and the values are lists of neighbors.
            start: The starting node.
            goal: The goal node.

        Returns:
            list or None: The shortest path from the start node to the goal node, or None if no path is found.
        """
        start_queue = [(start, [start])]  # Queue for the forward search
        goal_queue = [(goal, [goal])]    # Queue for the backward search

        visited_start = []  # Set to keep track of visited nodes in the forward search
        visited_goal = []  # Set to keep track of visited nodes in the backward search

        # Initialize path lists for forward and backward search
        forward_paths = {start: [start]}
        backward_paths = {goal: [goal]}

        while start_queue and goal_queue:
            # Forward search
            current_node, path_start = start_queue.pop(0)
            visited_start.append(current_node)

            if current_node in visited_goal:
                backward_path = backward_paths[current_node]
                backward_path.pop()
                return forward_paths[current_node] + backward_path[::-1]

            for neighbor in graph[current_node]:
                if neighbor not in visited_start:
                    start_queue.append((neighbor, path_start + [neighbor]))
                    forward_paths[neighbor] = path_start + [neighbor]

            # Backward search
            current_goal, path_goal = goal_queue.pop(0)
            visited_goal.append(current_goal)

            if current_goal in visited_start:
                forward_path = forward_paths[current_goal]
                forward_path.pop()
                return forward_path + backward_paths[current_goal][::-1]

            for neighbor in graph[current_goal]:
                if neighbor not in visited_goal:
                    goal_queue.append((neighbor, path_goal + [neighbor]))
                    backward_paths[neighbor] =  path_goal + [neighbor]

        return None  # No path found

    def GBFS(graph: dict, start: str, goal: str, heuristic: dict) -> list[str]:
        """
        Greedy Best-First Search (GBFS) algorithm to find the shortest path between two nodes in a graph.

        Args:
            graph (dict): The graph represented as a dictionary where the keys are nodes and the values are lists of neighbors.
            start: The starting node.
            goal: The goal node.
            heuristic (dict): A dictionary containing the heuristic values for each node.

        Returns:
            list or None: The shortest path from the start node to the goal node, or None if no path is found.
        """
        queue = [(heuristic[start], start, [start])]
        visited = []

        while queue:
            _, node, path = heapq.heappop(queue)

            if node == goal:
                return path  # Return the path from start to goal

            visited.append(node)

            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        heapq.heappush(queue, (heuristic[neighbor], neighbor, new_path))

        return None  # No path from start to goal found
    
    def AStar(graph: dict, start: str, goal: str, heuristic: dict) -> list[str]:
        queue = [(0 + heuristic[start] , start, [start])]
        visited = []

        while queue:
            cost, node, path = heapq.heappop(queue)
            cost = cost - heuristic[node]

            if node == goal:
                return path, cost  # Return the path and cost from start to goal

            visited.append(node)

            if node in graph:
                neighbors = graph[node]
                for neighbor, edge_cost in neighbors.items():
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        new_cost = cost + edge_cost
                        total_cost = new_cost + heuristic[neighbor]
                        heapq.heappush(queue, (total_cost, neighbor, new_path))

        return None  # No path from start to goal found
    
if __name__ == "__main__":
    pass