from strat2 import *

G1 = b111()
G2 = b12()

Graph = [G1] 
All_graphs =  [Graph]

G1.draw()
G3 = G1.O1(1)
G3.draw()
G3 = G1.O2(1)
G2.draw()
G3.draw()