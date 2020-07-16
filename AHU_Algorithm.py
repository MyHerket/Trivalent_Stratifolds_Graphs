from strat import *


def dfs(graph, source, father):
	path_list = []
	if graph.degree(source) == 1 and father != -1:
		return [[source, 1]]
	else:
		neighbor = list(graph.neighbors(source))
		if father != -1: neighbor.remove(father)
		for n in neighbor:
			paths = dfs(graph, n, source)
			for p in paths:
				p[-1] += 1
				path_list.append([source]+p)
		return path_list

def center(graph):
	G = graph.copy()
	paths = []
	largest = 0
	while len(G.leaves()) > 0:
		node = list(G.leaves())[0]
		dfs_list = dfs(G, node, -1)
		for p in dfs_list:
			if p[-1] > largest:
				largest = p[-1]
				l_path = p
		paths += dfs_list
		neighbor = list(G.neighbors(node))[0]
		if G.degree(neighbor) == 2: 
			G.remove_node(neighbor)
		G.remove_node(node)
	print("El camino mas largo fue: ", l_path)
	print("El dfs es: ")
	for p in paths: print(p)




G = b111()
G = G.O1(0)
G= G.O1(0)
prueba = center(G)