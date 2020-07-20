from strat2 import *
import random


while(1):
	print("What's the number of maximum white nodes in the graph?")
	n = int(input())
	All_graphs = []
	if n>1:
		build_until_m(All_graphs, n)
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
	if n<=1: 	print("The number of white vertex must be at least 2. Please enter a valid input.")
