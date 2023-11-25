from Tree import *
from Functions import *

'''Génère un puzzle et l'affiche sous forme de grille'''
puzzle = generatePuzzle()
#puzzle = [1,2,3,4,5,7,6,0,8] Pour générer un puzzle précis
print("\nStart puzzle: \n",affichage(puzzle))
print("-----------------------------------------------------------------------------------------")

'''Cherche le chemin le plus court jusqu'a la solution grace à l'algorithme A*'''
start_node = Node(puzzle)
tree = Tree(start_node)
solution, iterations = tree.A()

'''Affiche toutes les grilles et les informations additionnelles'''
print("\n\n")
c=0
for i in solution : 
    print("Etape ",c,"\n")
    affichage(i)
    print("\n")
    c+=1
print("\n\nNombre de mouvement pour résoudre le puzzle : ",len(solution)-1,"\n")
print("\nNombre d'itération totales de l'algorithme : ",iterations,"\n")
print("-----------------------------------------------------------------------------------------")
