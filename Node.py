class Node:
    '''Initialisation de la classe Node'''
    def __init__(self,puzzle):
        self.children = []
        self.parent = None
        self.puzzle = puzzle
        self.zeroInd = self.puzzle.index(0)
    
    '''Fonction permettant de vérifier si le puzzle est résolu'''
    def isGoal(self):
        return self.puzzle == [1,2,3,4,5,6,7,8,0]

    '''Fonction permettant d'effectuer une translation vers la droite'''
    def moveToRight(self):
        if self.zeroInd != 2 and self.zeroInd != 5 and self.zeroInd != 8:
            newPuzzle = self.puzzle.copy()
            newPuzzle[self.zeroInd], newPuzzle[self.zeroInd+1] = newPuzzle[self.zeroInd+1], newPuzzle[self.zeroInd]
            newNode = Node(newPuzzle)
            newNode.parent = self
            self.children.append(newNode)

    '''Fonction permettant d'effectuer une translation vers la gauche'''
    def moveToLeft(self):
        if self.zeroInd != 0 and self.zeroInd != 3 and self.zeroInd != 6:
            newPuzzle = self.puzzle.copy()
            newPuzzle[self.zeroInd], newPuzzle[self.zeroInd-1] = newPuzzle[self.zeroInd-1], newPuzzle[self.zeroInd]
            newNode = Node(newPuzzle)
            newNode.parent = self
            self.children.append(newNode)

    '''Fonction permettant d'effectuer une translation vers le haut'''
    def moveToUp(self):
        if self.zeroInd > 2:
            newPuzzle = self.puzzle.copy()
            newPuzzle[self.zeroInd], newPuzzle[self.zeroInd-3] = newPuzzle[self.zeroInd-3], newPuzzle[self.zeroInd]
            newNode = Node(newPuzzle)
            newNode.parent = self
            self.children.append(newNode)

    '''Fonction permettant d'effectuer une translation vers le bas'''
    def moveToDown(self):
        if self.zeroInd < 6:
            newPuzzle = self.puzzle.copy()
            newPuzzle[self.zeroInd], newPuzzle[self.zeroInd+3] = newPuzzle[self.zeroInd+3], newPuzzle[self.zeroInd]
            newNode = Node(newPuzzle)
            newNode.parent = self
            self.children.append(newNode)
            
    '''Fonction vérifiant tous les voisins pour voir si un des voisins n'est pas l'objectif'''
    def extendNode(self):
        self.moveToRight()
        self.moveToLeft()
        self.moveToUp()
        self.moveToDown()

