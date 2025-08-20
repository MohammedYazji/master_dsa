class Edge:
    def __init__(self, target, weight):
        # target to the target vertex
        self.target = target
        # the cost of the edge
        self.weight = weight

class Vertex:
    def __init__(self, label):
        # the vertex value
        self.label = label
        # List of Edge linking with adjacent
        # each edge has target and weight
        self.edges = []  

    def add_edge(self, target_vertex, weight):
        # make an edge then append it to the edges list
        self.edges.append(Edge(target_vertex, weight))

    def remove_edge(self, target_vertex):
        # update the list of edges of this instance of vertex
        # jsu make the edges all of them expect this target
        self.edges = [e for e in self.edges if e.target != target_vertex]

class Graph:
    def __init__(self):
        # List of Vertex in all the graph
        self.vertices = []  

    def add_vertex(self, label):
        # if the vertex doesn't exist before in the list of vertex append it
        if not any(v.label == label for v in self.vertices):
            self.vertices.append(Vertex(label))

    def find_vertex(self, label):
        # loop over the list of vertex then return the one we need
        for v in self.vertices:
            if v.label == label:
                return v
        return None

    def add_edge(self, from_label, to_label, weight):
        # get the start vertex and target one
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        # if we found the two vertex add edges for both
        if from_vertex and to_vertex:
            from_vertex.add_edge(to_vertex, weight)

    def remove_edge(self, from_label, to_label):
        # get the two vertex to remove the edge between
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.remove_edge(to_vertex)


    def remove_vertex(self, label):
        # get the vertex then
        target_vertex = self.find_vertex(label)
        # if exist loop over the list of vertex and remove it
        if target_vertex:
            # remove it from the vertices list
            self.vertices = [v for v in self.vertices if v != target_vertex]
            # then remove any edge with it
            for v in self.vertices:
                v.remove_edge(target_vertex)

    def bfs(self, start_label):
        # start point
        start_vertex = self.find_vertex(start_label)
        if not start_vertex:
            return

        # set to store all vertex we visited
        visited = set()
        # init the queue with the first vertex
        queue = [start_vertex]

        # while there's any vertex in the queue
        while queue:
            # pop it after the process
            vertex = queue.pop(0)
            # if not visited yet print it and mark it as visited [push to set]
            if vertex.label not in visited:
                print(vertex.label)
                visited.add(vertex.label)
                # then get the adjecent vertex of this vertex and if not visited push to the queue to visit them one by one after implement FIFO
                for edge in vertex.edges:
                    if edge.target.label not in visited:
                        queue.append(edge.target)

    def dfs(self, start_label): 
        # start point
        start_vertex = self.find_vertex(start_label)
        if not start_vertex:
            return

        # set to store all vertex we visited
        visited = set()
        # init the stack wuith the first vertex
        stack = [start_vertex]

        # while there's any vertex in the stack
        while stack:
            # pop it after the process
            vertex = stack.pop()
            # if not visited yet print it and mark it as visited [push to set]
            if vertex.label not in visited:
                print(vertex.label)
                visited.add(vertex.label)
                # then get the adjecent vertex of this vertex and if not visited push to the stack to visit them one by one after implement LIFO
                for edge in vertex.edges:
                    if edge.target.label not in visited:
                        stack.append(edge.target)

    def valid_path(self, start_label, end_label):
        # get the two vertex to check
        start_vertex = self.find_vertex(start_label)
        end_vertex = self.find_vertex(end_label)

        # if one of them doesn't exist => return
        if not start_vertex or not end_vertex:
            return False

        # using bfs
        # set to store all vertex we visited
        visited = set()
        # init the queue with the start vertex
        queue = [start_vertex]

        # while we have vertex not visited yet
        while queue:
            # get the vertex from the queue
            vertex = queue.pop(0)
            
            # so if we reach the end point so there's a path
            if vertex.label == end_label:
                return True
            
            # else =. we dont found it yet, so push the vertex to the visited set
            if vertex.label not in visited:
                visited.add(vertex.label)
                # so we finish it now will push its adjacent to the queue to process them
                for edge in vertex.edges:
                    if edge.target.label not in visited:
                        queue.append(edge.target)

        return False

    def is_cyclic(self):
        # store visited vertices and the recursion stack
        visited = set()
        # recursion stack to keep track of the vertices in the current path
        rec_stack = set()

        def dfs(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)

            for edge in vertex.edges:
                neighbor = edge.target
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True  # Found a cycle

            rec_stack.remove(vertex)
            return False

        for vertex in self.vertices:
            if vertex not in visited:
                if dfs(vertex):
                    return True
        return False
    

# Example usage simple
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B", 1)
g.add_edge("B", "C", 2)
g.add_edge("C", "A", 3)

print(g.valid_path("A", "C"))
print(g.is_cyclic())
