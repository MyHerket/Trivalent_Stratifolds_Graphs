from strat import *

def new_ord(letter):
	return ord(letter)-96

def new_chr(pos):
	return chr(pos + 96)

def O3(G1, G2, Node1, Node2):
	"""
		Performs operation O1* for graphs G1 and G2.
		For the new white and black vertices the defaults name are used.
		-G1: First graph that is used.
		-G2: Second graph that is used.
		-Node1: Node in G1 where O1* will be performed.
		-Node2: Node in G2 where O1* will be performed.
		Returns a new strat_graph object
		"""
	G = G1.copy()
	W = next(get_int(G.white()))
	B = next(get_str(G.black()))
	B = new_ord(B)-1
	Node2 += W

	n_edges = []
	for E in G2.edges(data = 'weight'):
		aux = list(E)
		aux[0] += W
		aux[1] = new_chr(new_ord(aux[1])+B)
		E = tuple(aux)
		n_edges.append(E)

	G.addEdg(n_edges)
	W = next(get_int(G.white()))
	B = next(get_str(G.black()))
	G.addEdg([(Node1, B), (Node2, B), (W, B)])
	return(G)

def build_sub_O1(Graph):
	"""
		For each white node in Graph, we create a copy of Graph and perform O1 in that node.
		Return a list of the graphs obtained.
	"""

	White = Graph.white()
	sub_list = []

	for n in White:
		temp_g = Graph.O1(n)
		sub_list.append(temp_g)
	
	return(sub_list)

def build_sub_O2(Graph):
	"""
		For each white node in Graph, we create a copy of Graph and perform O2 in that node.
		Return a list of the graphs obtained.
	"""

	White = Graph.white()
	sub_list = []

	for n in White:
		temp_g = Graph.O2(n)
		sub_list.append(temp_g)
	
	return(sub_list)

def build_sub_O3(Graph1, Graph2):
	"""
		For each white node in Graph1 and each white node in Graph2,
		we create a new strat_graph object which is the result of performing the operation O1* in those nodes.
		Return a list of the graphs obtained.
	"""

	White1 = Graph1.white()
	White2 = Graph2.white()
	sub_list = []

	for n in White1:
		for m in White2:
			temp_g = O3(Graph1, Graph2, n, m)
			sub_list.append(temp_g)
	
	return(sub_list)
	