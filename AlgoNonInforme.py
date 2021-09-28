from Robot import Robot
from Tree import Node

#Obtenir la position de l'aspirateur
print('Test robot : ')
rbt = Robot(2,0)
print(rbt)
rbt.moveLeft()
rbt.moveUp()
print(rbt)
#Créer un arbre de recherches et un stockage
print('Test arbre : ')
a= Node(5)
print(a)
b= Node(4)
c= Node(3)
d= Node(2)
e= Node(1)
f= Node(0)
a.insert(b,'up')
a.insert(c,'left')
a.insert(d,'right')
print(a)
b.insert(e,'up')
print(a)
e.insert(f,'up')
print(a)

#Analyser l'état de la pièce actuelle
    #S'il y a de la poussière > aspirer
    #S'il y a un bijou > le ramasser
    #Sinon récursivité :
    #Chercher les pièces juxtaposées jamais explorées et en créer des noeuds à ajouter à l'arbre et au stockage
    #Répéter jusqu'à trouver une pièce sale puis retourner l'arbre créé
    #En utilisant l'arbre déplacer le robot puis aspirer ou ramasser
    #Répéter
