from strat2 import *

G1 = b111()
G1.draw()
G2 = b12()
G2.draw()
Graph = [G2] 
All_graphs =  [Graph]

Graph = build_sub_O2(G2)
for g in Graph:
	g.draw()
Graph.append(G1)
All_graphs.append(Graph)
#-------------------------------------------

while(1):
	print("Ingresa la cantidad de vertices blancos hasta la cual quiere construir sus graficas:")
	n = input()
	if int(n)>3:
		build_until_m(All_graphs, int(n))
		break


#print(leaf_matrix(All_graphs[1][0]))
#print(leaf_matrix(All_graphs[1][1]))
#print(All_graphs[1][0].M == All_graphs[1][0])
#path = nx.shortest_path_length(G2, 0,1, weight = 'weight')
#print(path)