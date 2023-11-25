from Node import *

class Tree:
    '''Initialisation de la classe Tree'''
    def __init__(self,root):
        self.root = root
    
    '''Fonction adaptant l'algorithme A*'''
    def A(self):
        pathToSolution = []
        openList = []
        closedList = []
        iterations = 0
        stateCount = 0
        choix = int(input("Si vous voulez utilisez la méthode de Hamming tapez '0', sinon si vous voulez utilisez la méthode de Manhattan tapez '1' : "))
        if (choix==0):
            print("\nUtilisation de la methode de Hamming")
        else :
            print("\nUtilisation de la methode de Manhattan")

        openList.append(self.root)
        goalFound = False

        while len(openList) > 0 and not goalFound:
            iterations += 1
            currNode = openList.pop(0)
            closedList.append(currNode)
            currNode.extendNode()
            stateCount += 4
            for child in currNode.children:
                if child.isGoal():
                    pathToSolution = self.pathTrace(child)
                    goalFound = True
                if not self.contains(closedList,child):
                    if (choix==0):
                        child.hVal = self.hamming(child)
                    else:
                        child.hVal = self.manhattan(child)
                    openList.append(child)
            openList.sort(key = lambda x:x.hVal,reverse=False)


        return pathToSolution[::-1], iterations

    '''Fonction permettant de savoir si une node est contenue dans une liste de nodes'''
    def contains(self, nodes, Node):
        contains = False
        for node in nodes:
            if node.puzzle == Node.puzzle:
                contains = True
                break
        return contains

    '''Fonction adaptant la méthode de Hamming'''
    def hamming(self,node):
        goal = [1,2,3,4,5,6,7,8,0]
        score = 0
        for i in range(9):
            if node.puzzle[i] != goal[i]:
                score += 1
        return score

    '''Fonction adaptant la méthode de Manhattan'''
    def manhattan(self, node):
        goal = [1,2,3,4,5,6,7,8,0]
        score = 0
        for i in range(9):
            if node.puzzle[i] != 0:
                score += abs(int(node.puzzle[i]) - i)
        return score

    '''Fonction s'occupant du chemin du puzzle du début au puzzle résolu'''
    def pathTrace(self,currentNode):
        path = []
        path.append(currentNode.puzzle)

        while currentNode.parent != None:
            currentNode = currentNode.parent
            path.append(currentNode.puzzle)
        
        return path

