class Node:
    def __init__(self, node):
        self.branches = []
        self.content = node

class tree:
    def __init__(self, node):
        self.node = Node(node)

    def addNode(self, path, node, currentNode):
        if currentNode == None:
            currentNode = self.node
        words = path.split()
        if words[len(words)-1] == currentNode.content:
            currentNode.branches.append(Node(node))
            return
        branchToGo = self.pathLocation(path, currentNode.branches)
        if branchToGo == -1:
            return
        self.addNode(path, node, currentNode.branches[branchToGo])

    def searchTree(self, searchType, nodeToFind):
        if searchType == "breadth":
            return self.breadthSearch(nodeToFind, self.node, [])
        else:
            return self.depthSearch(nodeToFind, self.node, [])

    def depthSearch(self, nodeToFind, currentNode, path):
        path.append(currentNode.content)
        if currentNode.content == nodeToFind:
            return True, path
        nodeFound = False
        x = 0
        while((x < len(currentNode.branches)) and (nodeFound == False)):
            nodeFound, path = self.depthSearch(nodeToFind, currentNode.branches[x], path)
            if nodeFound == False:
                del path[-1]
            x+=1
        return nodeFound, path

    def pathLocation(self, path, branches):
        x = 0
        while(x < len(branches)):
            if branches[x].content in path:
                break
            x+=1
        if x == len(branches):
            return -1
        return x

    def printTree(self, printType):
        if printType == "breadth":
            return self.breadthPrint(self.node, [])
        else:
            return self.depthPrint(self.node, [])

    def depthPrint(self, node, nodes):
        for x in range(len(node.branches)):
            nodes = self.depthPrint(node.branches[x], nodes)
        nodes.append(node.content)
        return nodes

    def breadthPrint(self, node, nodes):
        nodes.append(node.content)
        for x in range(len(node.branches)):
            nodes = self.breadthPrint(node.branches[x], nodes)
        return nodes



folders = tree("Documents")
folders.addNode("Documents", "Pictures", None)
folders.addNode("Documents Pictures", "Photo", None)
folders.addNode("Documents", "Music", None)
folders.addNode("Documents", "Code", None)
folders.addNode("Documents Code", "PythonCode", None)
#print(folders.printTree("depth"))
#print(folders.printTree("breadth"))
nodeFound , path = folders.searchTree("depth", "Code")
