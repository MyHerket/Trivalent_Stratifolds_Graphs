from strat import *


def dfs(graph, source, father):
	"""
	Deep-first Search implementation in the graph. It is a recursive function that maps all the paths from one node to another.
	"""
	if graph.degree(source) == 1 and father != -1:
		return [source]
	else:
		neighbor = list(graph.neighbors(source))
		if father != -1: neighbor.remove(father)
		longestPath = []
		length = 0
		for n in neighbor:
			path = dfs(graph, n, source)
			if(len(path) > length ):
				length = len(path)
				longestPath = path
		return [source]+longestPath

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
	node = list(G.nodes())[0]

	longestPath = dfs(G, node, -1)
	longestPath = dfs(G, longestPath[-1], -1)

	center_i = int((len(longestPath)-1)/2)

	graph.root = longestPath[center_i]
	#graph.tag[3] = shortest

	return longestPath[center_i]

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

def dfsGetDistinctWhites(graph, source, father):
	"""
	This the DFS recursive implementation to compute the distinct white vertices
	of graph under automorphism.
	"""
	if graph.degree(source) == 1 and father != -1:
		if graph.nodes[source]['bipartite'] == 0 :
			return [source]
		else:
			return []
	else:
		neighbor = list(graph.neighbors(source))
		if father != -1: neighbor.remove(father)
		whitesDir = {}
		length = 0
		for n in neighbor:
			node_whites = dfsGetDistinctWhites(graph, n, source)
			whitesDir[graph.nodes[n]['word']] = node_whites
		if graph.nodes[source]['bipartite'] == 0:
			return sum(whitesDir.values(),[source])
		else:
			return sum(whitesDir.values(),[])

def getDistinctWhites(G):
	"""
	Returns the distinct number of vertices under automorphisms of G.
	"""
	root = list(G.nodes())[0]
	if hasattr(G, 'root'):
		root = G.root

	whites = dfsGetDistinctWhites(G, root, -1)

	return whites

def test():
	G2=strat_graph()
	#edgs=[(1,'a',2),(1,'b',2),(2,'a'),(3,'b')]
	#edgs=[(0,'a'),(0, 'b'),(1,'a',2), (2,'b'),(3,'b')]
	#edgs=[(0,'a',2),(2,'b'),(3,'c'), (4,'d'), (1,'a'),(1,'b',2),(1,'c',2),(1,'d',2)]
	#edgs=[(1,'a'),(2,'a'),(5,'d'),(4,'c'),(3,'b'),(0,'a'),(0,'b',2),(0,'c',2), (0,'d',2)]
	edgs=[(1,'a'),(2,'a'),(0,'a'),(0,'b'),(3,'b'),(4,'b'),(4,'c'),(6,'c'),(5,'c')]

	G2.addEdg(edgs)
	G2.tag = 'example'
	G2.draw(trivalent=True)
	center(G2)
	print(G2.root)

	print(rooted_tree(G2, G2.root, -1))

	print(getDistinctWhites(G2))




if __name__ == "__main__":
	test()
