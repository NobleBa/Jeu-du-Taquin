import random

''' Fonction permettant de générer un puzzle 3*3 aléatoire'''
def generatePuzzle():
    puzzle = [1,2,3,4,5,6,7,8,0];
    random.shuffle(puzzle)
    while not isSolvable(puzzle):
        random.shuffle(puzzle)
    return puzzle

''' Fonction permettant de vérifier si le puzzle est résolvable'''
def isSolvable(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i+1,len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

'''Fonction permettant de calculer l'heuristique de Hamming'''
def hamming(puzzle):
        goal = [1,2,3,4,5,6,7,8,0]
        score = 0
        for i in range(9):
            if puzzle[i] != goal[i]:
                score += 1
        return score

'''Fonction permettant de calculer l'heuristique de Manhattan'''
def manhattan(puzzle):
    goal = [1,2,3,4,5,6,7,8,0]
    score = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                goal_i, goal_j = divmod(puzzle[i][j] - 1, 3)
                score += abs(i - goal_i) + abs(j - goal_j)
    return score

'''Fonction permettant d'afficher le puzzle sous forme de grille'''
def affichage(puzzle) :
    for i in range(9):
            if(puzzle[i]==0):
                puzzle[i] = 'X'
    print("#-----#-----#-----#")
    print("| ",puzzle[0]," | ",puzzle[1]," | ", puzzle[2]," |")
    print("#-----#-----#-----#")
    print("| ",puzzle[3]," | ",puzzle[4]," | ", puzzle[5]," |")
    print("#-----#-----#-----#")
    print("| ",puzzle[6]," | ",puzzle[7]," | ", puzzle[8]," |")
    print("#-----#-----#-----#")
    for i in range(9):
            if(puzzle[i]=='X'):
                puzzle[i] = 0