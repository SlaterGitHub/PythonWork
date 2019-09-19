class Node:
    def __init__(self, node):
        self.branches = []
        self.node = Node

class tree:
    def __init__(self, node):
        self.tree = Node(node)

    def addNode(self, path, node, currentNode):
        if path == currentNode:
            currentNode.branches.append(node)
            return
        branchToGo = self.pathLocation(path, currentNode.branches)
        if branchToGo == -1:
            return
        self.addNode(path, node, currentNode.branches[branchToGo])

    def pathLocation(self, path, branches):
        x = 0
        while(x < len(branches)):
            if braches[x] in path:
                break
            x+=1
        if x = len(branches):
            return -1
        return x
