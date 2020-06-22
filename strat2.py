from strat import *
import networkx.algorithms.isomorphism as iso
import os.path
from os import path

def new_ord(letter):
	"""
	Turns a letter to the number of its position in the alphabet
	"""
	return ord(letter)-96

def new_chr(pos):
	"""
	Turn a number to the letter in that position in the alphabet
	"""
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
	k = 1

	for n in White:
		temp_g = Graph.O1(n)
		temp_g.labeling(k)
		sub_list.append(temp_g)
		k +=1
	
	return(sub_list)

def build_sub_O2(Graph):
	"""
		For each white node in Graph, we create a copy of Graph and perform O2 in that node.
		Return a list of the graphs obtained.
	"""

	White = Graph.white()
	sub_list = []
	k = 1

	for n in White:
		temp_g = Graph.O2(n)
		temp_g.labeling(k)
		sub_list.append(temp_g)
		k+=1
	
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
	k = 1

	for n in White1:
		for m in White2:
			temp_g = O3(Graph1, Graph2, n, m)
			temp_g.labeling(k)
			sub_list.append(temp_g)
			k += 1
	
	return(sub_list)
	
def build_from_list_O1(list_graph):
	"""
	For each graph in the list list_graph,	we perform build_sub_O1 on it. 
	Then we build a new list of graphs with the elements of the previous lists. 
	
	"""
	graphs = []
	for grp in list_graph:
		temp_list = build_sub_O1(grp)
		graphs += temp_list
	return graphs

def build_from_list_O2(list_graph):
	"""
	For each graph in the list list_graph,	we perform build_sub_O2 on it. 
	Then we build a new list of graphs with the elements of the previous lists. 
	
	"""
	graphs = []
	for grp in list_graph:
		temp_list = build_sub_O2(grp)
		graphs += temp_list
	return graphs

def build_from_list_O3(list_graph, list2_graph):
	"""
	For each graph in the list list_graph and list2_graph,	we perform build_sub_O3 on them. 
	Then we build a new list of graphs with the elements of the previous lists. 
	
	"""
	graphs = []
	for grp in list_graph:
		for grp2 in list2_graph:
			temp_list = build_sub_O3(grp, grp2)
			graphs += temp_list
	return graphs
	

def Class_black_nodes(list_graph):
	"""
	list_graph: A list of list of graphs. 
	Creates a new list of lists of graphs by dividing the previous lists depending on the number of black nodes in each graph.
	Returns the new list.
	"""
	C_l = []
	for graph in list_graph:
		k = len(graph.black())
		if len(C_l) < k:
			for i in range(len(C_l), k):
				C_l.append([])
		C_l[k-1] += [graph]
	i = len(C_l)-1
	while i >= 0:
		if len(C_l[i]) == 0:
			C_l.pop(i)
		i += -1
	return C_l

def Class_leaves(list_graph):
	"""
	list_graph: A list of list of graphs. 
	Creates a new list of lists of graphs by dividing the previous lists depending on the number of leaves in each graph.
	Returns the new list.
	"""
	C_l = []
	for graph in list_graph:
		k = len(graph.leaves())
		if len(C_l) < k:
			for i in range(len(C_l), k):
				C_l.append([])
		C_l[k-1] += [graph]
	i = len(C_l)-1
	while i >= 0:
		if len(C_l[i]) == 0:
			C_l.pop(i)
		i += -1
	return C_l

def Class_min_path(list_graph):
	"""
	list_graph: A list of list of graphs. 
	Creates a new list of lists of graphs by dividing the previous lists depending on the minimum length of a path between two leaves in each graph.
	Returns the new list.
	"""
	C_l = []
	for graph in list_graph:
		k = graph.tag[3]
		if len(C_l) < k:
			for i in range(len(C_l), k):
				C_l.append([])
		C_l[k-1] += [graph]
	i = len(C_l)-1
	while i >= 0:
		if len(C_l[i]) == 0:
			C_l.pop(i)
		i += -1
	return C_l

def Class_max_path(list_graph):
	"""
	list_graph: A list of list of graphs. 
	Creates a new list of lists of graphs by dividing the previous lists depending on the maximum length of a path between two leaves in each graph.
	Returns the new list.
	"""
	C_l = []
	for graph in list_graph:
		k = graph.tag[4]
		if len(C_l) < k:
			for i in range(len(C_l), k):
				C_l.append([])
		C_l[k-1] += [graph]
	i = len(C_l)-1
	while i >= 0:
		if len(C_l[i]) == 0:
			C_l.pop(i)
		i += -1
	return C_l

def leaf_matrix(graph):
	"""
	Given a graph, for each leaf in it, calculates the length of the minimum path from this leaf to every other node. 
	Each leaf gives a row for the matrix. The next step is sort the numbers in the row, from low to high.
	At last we sort the rows of the matrix from low to high.
	"""
	matrix = []
	for leaf in graph.leaves():
		a = []
		for node in graph.nodes():
			path = nx.shortest_path_length(graph, leaf,node, weight = 'weight')
			a.append(path)
			a.sort()
		matrix.append(a)
	matrix.sort()
	graph.M = matrix
	return matrix

def Class_isomorphic(list_graph):
	"""
	list_graph: A list of list of graphs. 
	Creates a new list of lists of graphs by dividing the previous lists depending on the leaf matrix in each graph.
	Draws each of this graphs and save them with the name "[tag].png", where the tag deppends in each graph.
	Returns the new list.
	"""
	C_l = []
	for graph in list_graph:
		flag = 0
		leaf_matrix(graph)
		if len(C_l) == 0:
			graph.labeling(1)
			name = str(graph.tag) + ".png"
			if not(path.exists(name)):
				graph.draw()
			C_l.append([graph])
		for sub_list in C_l:
			compare = graph.M == sub_list[0].M
			if compare:
				flag = 1
				break
		if flag == 0:
			graph.labeling(len(C_l)+1)
			name = str(graph.tag) + ".png"
			if not(path.exists(name)):
				graph.draw()
			C_l.append([graph])
	return C_l

def Categories(Graph_list):
	"""
	list_graph: A list of list of graphs. 
	Creates a new list of lists of graphs by applying the previous lists the functions Class_black_nodes, Class_leaves, Class_min_path, Class_max_path, Class_isomorphic in that order.
	Returns the new list.
	"""
	CL = Class_black_nodes(Graph_list)
	GC = []
	for g_list in CL:
		GC += Class_leaves(g_list)
	CL = []
	for g_list in GC:
		CL += Class_min_path(g_list)
	GC = []
	for g_list in CL:
		GC += Class_max_path(g_list)
	CL = []
	for g_list in GC:
		CL += Class_isomorphic(g_list)
	return CL


def build_until_m(All_graphs, m):
	"""
	All_graphs: A list of lists of graphs divided by the number of white nodes in them. At least it has the lists of 2 and 3 white nodes.
	m: An integer greater than or equal to 4.
	Creates a list of graphs with n white nodes using the lists of graphs with fewer white nodes. For more information read *.pdf
	Appends this list to All_graphs.
	"""
	if m > 3:
		k = len(All_graphs)
		for n in range(k+2, m+1):
			G1 = build_from_list_O2(All_graphs[n-3])
			G2 = build_from_list_O1(All_graphs[n-4])
			new_list = G1 + G2
			for i in range(n):
				if n-i-5 >= 0:
					G3 = build_from_list_O3(All_graphs[i], All_graphs[n-i-5])
					new_list += G3
				else: 
					break
			new_list = Categories(new_list)
			flat_list = [item for l in new_list for item in l]
			print("For ", n, " white nodes, we have ", len(flat_list), " different graphs.")
			All_graphs.append(flat_list)