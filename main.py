from strat2 import *

G1 = b111()
G2 = b12()

Graph = [G2] 
All_graphs =  [Graph]

Graph = build_sub_O2(G2)
Graph.append(G1)
All_graphs.append(Graph)
#-------------------------------------------

while(1):
	print("Ingresa la cantidad de vertices blancos hasta la cual quiere construir sus graficas:")
	n = input()
	if int(n)>3:
		build_until_m(All_graphs, int(n))
		for List in All_graphs:
			for g in List:
				if type(g) == list:
					for h in g:
						print(h.tag)
						h.draw()
				else:
					print(g.tag)
					g.draw()
		break
"""
G1.labeling(4)
print(G1.tag)
path = nx.shortest_path_length(G1, 0,1, weight = 'weight')
print(path)
#print(G1.p_graph())
"""