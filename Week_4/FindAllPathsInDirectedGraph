# Python function to find all possible paths from source vertex to destination vertesx in directed graph.

def findAllPaths(vertices, gList, source, destination):
    allpath=[]
    temp_path=[]
    visited={v:False for v in vertices}
    findAllPathsRecursive(vertices, gList, visited, source, destination, allpath, temp_path)
    return allpath
    
def findAllPathsRecursive(vertices, gList, visited, src, dest,allpath, path):
    visited[src]=True
    path.append(src)
    
    if src == dest:
        allpath.append(path.copy())
    
    for e in gList[src]:
        if not visited[e]:
            findAllPathsRecursive(vertices, gList, visited, e, dest, allpath, path)
    
    path.pop()
    visited[src]=False
    
    
#Vertices are expected to be labelled as single letter or single digit 

#Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
  Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))
