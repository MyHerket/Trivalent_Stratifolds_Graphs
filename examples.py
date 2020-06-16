from strat import *

###########Test if a graph is Horned Tree
#G1=strat_graph()
#edgs=[(1,'a',2),(3,'a'),(3,'c'),
#      (2,'b',2),(4,'b'),(4,'c'),
#      (5,'c'),(5,'d'),(6,'d'),(6,'e'),
#      (8,'e',2),(7,'d'),(7,'f'),(9,'f',2)]
#G1.addEdg(edgs)
#print(G1.is_horned_tree())
#G1.draw(trivalent=True)

###########Test if a graph is 2,1-collapsible
#G2=strat_graph()
#edgs=[(1,'a',2),(1,'b',2),(2,'a'),(3,'b')]
#G2.addEdg(edgs)
#print(G2.is_21_collapsible())
#G2.draw(trivalent=True)

###########Test if a graph is trivalent and simply connected
#G3=strat_graph()
#edgs=[(1,'a',2),(2,'a'),(2,'b',2),(3,'b'),
#      (3,'c',2),(4,'c'),(1,'d',2),(5,'d'),
#      (5,'e',2),(6,'e'),(5,'f',2),(7,'f'),
#      (7,'g',2),(7,'h',2),(7,'i',2),(8,'g'),
#      (9,'h'),(10,'i'),
#      (4,'j'),(11,'j'),(12,'j'),(12,'k'),
#      (13,'k'),(13,'l'),(15,'l',2),(15,'n',2),
#      (17,'n'),(14,'k'),(14,'m'),(16,'m',2),
#      (16,'o',2),(16,'p',2),(18,'o'),(19,'p'),
#      (19,'q'),(20,'q'),(21,'q')]
#G3.addEdg(edgs)
#
#print(G3.is_simply_connected())
#G3.draw(trivalent=True)


###########Constructing graph with operations O1,O1* and O2
W=get_int()
B=get_str()

#Start with a single white vertex
G4=strat_graph(white=[next(W)])
G4.draw(True)

#Perform O1 on it
G4=G4.O1(0,[],[],next(W),next(W),next(B))
G4.draw(True)

#Perform O2 on vertex 0
G4.O2(0,next(W),next(B))
G4.draw(True)

#Perform O1* on vertex 2, where the second graph is a b111-tree
aux=b111(black=next(B),white=[next(W) for i in range(3)])
G4=G4.O1_1(2,aux,list(aux.white())[0],black=next(B),white=next(W))
G4.draw(True)

print(G4.is_simply_connected())