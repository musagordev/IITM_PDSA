#Python Function to compute the number of connected components in undirected graph.

class Queue:
    def __init__(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    
    def isempty(self):
        return(self.queue == [])

    def __str__(self):
        return(str(self.queue))

def findComponents_undirectedGraph(vertices,edges):
    components=0
    visited = {v:False for v in vertices}
    q_list = Queue()
    gList={}
    for v in vertices:
        gList[v]=[]
    for k,v in edges:
        gList[k].append(v)
        gList[v].append(k)
    for k_1,v_1 in visited.items():
        if not visited[k_1]:
            components += 1
            q_list.addq(k_1)
            while not q_list.isempty():
                w = q_list.delq()
                if not visited[w]:
                    for keys in gList:
                        if keys == w:
                            for i in range(len(gList[keys])):
                                q_list.addq(gList[keys][i])
                visited[w] = True
                
    return components
