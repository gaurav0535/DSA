from queue import Queue

adj_list = {
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}

visited = {}
bfs_traversal_output = []

queue = Queue()

for node in adj_list.keys():
    visited[node] = False

s = 'A'

visited[s] = True
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            queue.put(v)


print("Visited -- >",visited)
print("adj_list -- >",adj_list)

print("BFS traversal output " ,bfs_traversal_output)



