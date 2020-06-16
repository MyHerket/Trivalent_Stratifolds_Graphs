from strat2 import *

G1 = b111()
G2 = b12()

Graph = [G1] 
All_graphs =  [Graph]

print("Grafos sub O1")
L = build_sub_O1(G2)
for g in L:
	g.draw()

print("Grafos sub O2")
L = build_sub_O2(G2)
for g in L:
	g.draw()

print("Grafos sub O3")
L = build_sub_O3(G2, G1)
for g in L:
	g.draw()

