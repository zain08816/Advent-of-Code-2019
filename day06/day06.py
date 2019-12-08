import networkx

inp = open('day06.txt', 'r')

graph = []
for x in inp:
	y = x.replace("\n", '')
	graph.append(y.split(')'))

h = networkx.Graph(graph)
res = sum(networkx.shortest_path_length(h, x, 'COM') for x in h.nodes)
res2 = networkx.shortest_path_length(h, 'YOU', 'SAN') - 2

print(graph)
print(res)
print(res2)