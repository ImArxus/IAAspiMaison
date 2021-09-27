from Robot import Robot
from Tree import Node

#Obtenir la position de l'aspirateur
rbt = Robot(2,0)
print(rbt)
rbt.moveLeft()
rbt.moveUp()
print(rbt)
#Créer un arbre de recherches et un stockage
a= Node(5)
print(a)
a.insert(1,'up')
a.insert(0,'left')
a.insert(2,'down')
print(a)
a.insert(0,'up')
print(a)
#Analyser l'état de la pièce actuelle
    #S'il y a de la poussière > aspirer
    #S'il y a un bijou > le ramasser
    #Sinon récursivité :
    #Chercher les pièces juxtaposées jamais explorées et en créer des noeuds à ajouter à l'arbre et au stockage
    #Répéter jusqu'à trouver une pièce sale puis retourner l'arbre créé
    #En utilisant l'arbre déplacer le robot puis aspirer ou ramasser
    #Répéter
