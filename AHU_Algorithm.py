from strat import *


def dfs(graph, source, father):
	"""
	Deep-first Search implementation in the graph. It is a recursive function that maps all the paths from one node to another.
	"""
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
	"""
	This function helps eliminates a leaf and the edges conected to that leaf. 
	Also ereases all the nodes that turns into a leaf when the first one is eliminated.
	"""
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
	"""
	Returns the name of the node that is the center of a graph
	"""
	G = graph.copy()
	largest = 0
	shortest = 100000000
	while len(G.leaves()) > 0:
		node = list(G.leaves())[0]
		dfs_list = dfs(G, node, -1)
		for p in dfs_list:
			if p[-1] > largest:
				largest = p[-1]
				l_path = p
			if p[-1] < shortest: 
				shortest = p[-1]
		clean_leaf(G, node)
	center_i = int((l_path[-1]-1)/2)
	graph.root = l_path[center_i]
	#graph.tag[3] = shortest
	#graph.tag[4] = largest
	return l_path[center_i]

def four(name):
	"""
	Turns a string of a number in base 4 into an integer.
	"""
	return int(name, 4)

def four_for_graph(graph):
	"""
	Turns the string associated to a graph into an integer that is comparable.
	"""
	return int(graph.string, 4)

def rooted_tree(graph, source, father):
	"""
	Builds the string associated to a graph using the center of it.
	For each node saves the string associated to that node.
	"""
	path_list = []
	if father == -1:
		a = '0'
		b = '1'
	else:
		w = graph[source][father][0]['weight']
		if w == 1: 
			a = '0'
			b = '1'
		elif w == 2: 
			a = '2'
			b = '3'
	
	if graph.degree(source) == 1:
		return a+b
	else:
		neighbor = list(graph.neighbors(source))
		if father != -1: neighbor.remove(father)
		for n in neighbor:
			paths = rooted_tree(graph, n, source)
			graph.nodes[n]['word'] = paths #Esta línea guarda la palabra generada para el nodo en el nodo 
			path_list.append(paths)
		path_list.sort(key = four)
		string = a
		for p in path_list: string+=p
		return string + b


 