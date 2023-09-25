class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.adj_list = {}
        for start, end in edges:
            if start in self.adj_list:
                self.adj_list[start].append(end)
            else:
                self.adj_list[start] = [end]
        print('Adjacency List of Graph:',self.adj_list)
    
    def get_paths(self,start,end,path=[]):
        path = path + [start]
        #print(path)
        if start == end:
            return [path]
        if start not in self.adj_list:
            return []
        paths = []
        for node in self.adj_list[start]:
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    def get_shortest_paths(self,start,end,path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.adj_list:
            return None
        
        shortest_path = None
        for node in self.adj_list[start]:
            if node not in path:
                sp = self.get_shortest_paths(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path = sp
        
        return shortest_path


if __name__== '__main__':
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    start = "Mumbai" 
    end = "New York"
    route_graph = Graph(routes)
    print(f'Path from {start} to {end}',route_graph.get_paths(start,end))
    print(f'Shortest path from {start} to {end} is:',route_graph.get_shortest_paths(start,end))

        
