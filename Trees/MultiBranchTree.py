class Node:
    def __init__(self, node):
        self.branches = []
        self.content = node

class Queue:
    def __init__(self):
        self.nodesToVisit = []

    def deQueue(self):
        return self.nodesToVisit.pop(0)

    def enQueue(self, item):
        self.nodesToVisit.append(item)
        print(self.returnQueue())

    def QueueSize(self):
        return len(self.nodesToVisit)

    def returnQueue(self):
        nodes = []
        for x in range(len(self.nodesToVisit)):
            nodes.append(self.nodesToVisit[x].content)
        return nodes

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
            toVisit = Queue()
            toVisit.enQueue(self.node)
            nodes =  self.breadthPrint(toVisit, [])
            nodes.insert(0, self.node.content)
            return nodes
        else:
            return self.depthPrint(self.node, [])

    def depthPrint(self, node, nodes):
        for x in range(len(node.branches)):
            nodes = self.depthPrint(node.branches[x], nodes)
        nodes.append(node.content)
        return nodes

    def breadthPrint(self, toVisit, nodes):
        currentNode = toVisit.deQueue()

        for x in range(len(currentNode.branches)):
            nodes.append(currentNode.branches[x].content)
            if len(currentNode.branches[x].branches) > 0:
                toVisit.enQueue(currentNode.branches[x])

        if toVisit.QueueSize() > 0:
            self.breadthPrint(toVisit, nodes)

        return nodes

folders = tree("Documents")
folders.addNode("Documents", "Pictures", None)
folders.addNode("Documents Pictures", "Photo", None)
folders.addNode("Documents", "Music", None)
folders.addNode("Documents", "Code", None)
folders.addNode("Documents Code", "PythonCode", None)
folders.addNode("Documents Code PythonCode", "TreeProg", None)
#print(folders.printTree("depth"))
print(folders.printTree("breadth"))
nodeFound , path = folders.searchTree("depth", "Code")
