from AHU_Algorithm import *
import os.path
from os import path

##Funtions to manipulate nodes' names
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


#Building Functions
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
		creates a new strat_graph object which is the result of performing the operation O1* on those nodes.
		Returns a list of the graphs obtained.
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
	Performs build_sub_O1 on each graph of the list list_graph.
	Then builds a new list with the elements of the previous lists generated.
	"""
	graphs = []
	for grp in list_graph:
		temp_list = build_sub_O1(grp)
		graphs += temp_list
	return graphs

def build_from_list_O2(list_graph):
	"""

	Performs build_sub_O2 on each graph of the list list_graph.
	Then builds a new list with the elements of the previous lists generated.
	"""
	graphs = []
	for grp in list_graph:
		temp_list = build_sub_O2(grp)
		graphs += temp_list
	return graphs

def build_from_list_O3(list_graph, list2_graph):
	"""
	Performs build_sub_O3 on every pair of graphs where the first one is an element of list_graph and the second is an element of list2_graph.
	Then builds a new list with the elements of the lists generated.
	"""
	graphs = []
	for grp in list_graph:
		for grp2 in list2_graph:
			temp_list = build_sub_O3(grp, grp2)
			graphs += temp_list
	return graphs


#Functions for order_by
def order_by_black_nodes(list_graph):
	"""
	list_graph: A list of lists of graphs.
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

def order_by_leaves(list_graph):
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

def order_by_min_path(list_graph):
	"""
	list_graph: A list of list of graphs.
	Creates a new list of lists of graphs by dividing the previous lists depending on  the length of the shortest path between two leaves in each graph.
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

def order_by_max_path(list_graph):
	"""
	list_graph: A list of list of graphs.
	Creates a new list of lists of graphs by dividing the previous lists depending on the length of the largest path between two leaves in each graph.
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

def order_by_string(list_graph):
	"""
	list_graph: A list of list of graphs.
	Creates a new list of lists of graphs by dividing the previous lists depending on the leaf matrix of each graph.\\
    If two or more graphs have the same leaf matrix, delete all of them except one.\\
    Draws each of the remaining graphs and save them with the name "[tag].png" following the nomenclature in "Trivalent_Stratifold_Documentation.pdf".\\
    Then flatten the list of lists with one element, and returns this flatten list.
	"""
	C_l = []
	for graph in list_graph:
		flag = 0
		center(graph)
		graph.string = rooted_tree(graph, graph.root, -1)
		if len(C_l) == 0:
			C_l.append(graph)
		for sub_list in C_l:
			compare = graph.string == sub_list.string
			if compare:
				flag = 1
				break
		if flag == 0:
			C_l.append(graph)
		C_l.sort(key = four_for_graph)
	k = 1
	for g in C_l:
		g.labeling(k)
		name = str(g.tag) + ".png"
		#center(g, True);
		#print(name, g.root, g.string)

		#if not(path.exists(name)):
		#	g.draw()
		k += 1
	return C_l

def Categories(list_graph):
	"""
	list_graph: A list of list of graphs.
	Creates a new  list of graphs by applying to the previous lists the functions order_by_black_nodes, order_by_leaves, order_by_min_path, order_by_max_path, order_by_isomorphic in that order.
	Returns the new list.
	"""
	CL = order_by_black_nodes(list_graph)
	GC = []
	for g_list in CL:
		GC += order_by_leaves(g_list)
	CL = []
	for g_list in GC:
		CL += order_by_min_path(g_list)
	GC = []
	for g_list in CL:
		GC += order_by_max_path(g_list)
	CL = []
	for g_list in GC:
		CL += order_by_string(g_list)
	return CL


def build_until_m(All_graphs, m):
	"""
	All_graphs must be a list of lists of graphs divided by the number of white nodes in them.
	m An integer greater than or equal to 2.
	Creates the list of graphs with m white nodes without repetition, using the lists of graphs with fewer white nodes.Further details in Trivalent_Stratifold_Documentation.pdf
	Returns All_graphs the list of lists of graphs with  n white nodes from 2 to m.\
	"""
	if m>1 and len(All_graphs) == 0:
		G2 = b12()
		G2.draw()
		Graph = [G2]
		All_graphs =  [Graph]
	if m>2 and len(All_graphs) == 1:
		G1 = b111()
		G1.draw()
		Graph = build_sub_O2(G2)
		for g in Graph:
			g.draw()
		Graph.append(G1)
		All_graphs.append(Graph)
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
			flat_list = Categories(new_list)
			print("For ", n, " white nodes, we have ", len(flat_list), " different graphs.")
			All_graphs.append(flat_list)
