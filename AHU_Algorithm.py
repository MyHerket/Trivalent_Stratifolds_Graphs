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

def clean_leaf(graph, leaf):
	neighbor = list(graph.neighbors(leaf))[0]
	if graph.degree(neighbor) == 1:
		graph.remove_node(neighbor)
		graph.remove_node(leaf)
	elif graph.degree(neighbor) == 2:
		graph.remove_node(leaf)
		clean_leaf(graph, neighbor)
	else: 
		graph.remove_node(leaf)
	return


def center(graph):
	G = graph.copy()
	#paths = []
	largest = 0
	while len(G.leaves()) > 0:
		node = list(G.leaves())[0]
		dfs_list = dfs(G, node, -1)
		for p in dfs_list:
			if p[-1] > largest:
				largest = p[-1]
				l_path = p
		#paths += dfs_list
		clean_leaf(G, node)
	center_i = int((l_path[-1]-1)/2)
	#print("El camino mas largo fue: ", l_path, " y el centro es ", l_path[center_i])
	return l_path[center_i]




G = b111()
G = G.O1(0)
G= G.O1(0)

print(center(G))