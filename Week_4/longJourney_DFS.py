#A tourist wants to travel around India from north to south. He has a policy that he never travels
#back towards the north. Write a Python function longJourney(AList) to find him a route with
#which he can visit the maximum number of cities according to his policy, where AList represents
#a graph of cities and routes between them. Every edge in adjacency list AList is a feasible route
#between one city to another from north to south. The function should return a list in the order
#the cities are to be visited to visit maximum cities.

def longJourney(AList):
    # Helper function to perform DFS and find the longest path
    def dfs(city, visited, memo):
        if city in memo:
            return memo[city]
        
        visited.add(city)
        max_path = [city]
        
        for neighbor in AList.get(city, []):
            if neighbor not in visited:
                path = dfs(neighbor, visited, memo)
                if len(path) + 1 > len(max_path):
                    max_path = [city] + path

        visited.remove(city)
        memo[city] = max_path
        return max_path

    # Store the longest route starting from each city
    longest_route = []
    memo = {}
    
    # Visit all cities to account for possible disconnections in the graph
    for city in AList.keys():
        route = dfs(city, set(), memo)
        if len(route) > len(longest_route):
            longest_route = route
    
    return longest_route
