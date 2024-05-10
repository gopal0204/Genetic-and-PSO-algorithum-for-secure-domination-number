import math
def adjacency_list(v,edges):
    adjacencyList={}
    for vertex in v:
        adjacencyList[vertex]= []
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        adjacencyList[v1].append(v2)
        adjacencyList[v2].append(v1)
    return adjacencyList,v

n1,n2 = map(int,input().split())
v = []
for i in range(1,n1+1):
    v.append(i)
edges = []
for i in range(1,n2+1):
    v1,v2 = map(int,input().split())
    edges.append([v1,v2])
adjacencyList, v = adjacency_list(v,edges)

u1 = []
u2 = []
adjacencyList2 = {}
for x in adjacencyList.values():
    u1.append(len(x))
for y in adjacencyList:
    u2.append(y)
for z in range(len(u1)):
    adjacencyList2[u2[z]] = u1[z]
adjacencyList3 = dict(sorted(adjacencyList2.items(), key=lambda x: x[1], reverse=False))
uu1 = []
for i in adjacencyList3.values():
    uu1.append(i)

print(adjacencyList3.values())

print("min_degree", uu1[0])
a = uu1[0] + 1
b = math.log(a)
c = 2 * b
d= c + 1
print(d)
e = d / a
print(e)
f = e * len(v)
print("UB",math.ceil(f))