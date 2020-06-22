from strat2 import *

while(1):
	print("What's the number of maximum white nodes in the graph?")
	n = int(input())
	if n>1:
		G2 = b12()
		G2.draw()
		Graph = [G2] 
		All_graphs =  [Graph]
	if n>2:
		G1 = b111()
		G1.draw()
		Graph = build_sub_O2(G2)
		for g in Graph:
			g.draw()
		Graph.append(G1)
		All_graphs.append(Graph)
	if n>3:
		build_until_m(All_graphs, int(n))
		c = 'S'
		while(1):
			print("Do you want to reprint a graph? (Y/N)")
			c = input()
			if c == 'Y':
				print("Enter the numbers in the tag, one by one")
				t = []
				for i in range(6):
					t.append(int(input()))
				for graph in All_graphs[t[0]-2]:
					if graph.tag == t:
						graph.draw()
						break
			else: break
		break
	if n>1 and n <=3: break
	if n<=1: 	print("The number of white vertex must be at least 2. Please enter a valid input.")