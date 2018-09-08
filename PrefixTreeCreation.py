from common import Cell, Node
import csv

def buildPrefixTree(filePath):
    '''
    :type: str
    :rtype: (Node, int)
    '''
    root = Node()
    depth = 0

    # traverse lines in dataSet
    with open(filePath) as csvfile:
        rder = csv.reader(csvfile)
        for entry in rder:
            depth = len(entry)
            # tier tree from top to down
            node = root
            # when one entry pass this node, + 1
            node.NOofEntity += 1

            t = entry
            # from each column of current row
            for i, val in enumerate(t):
                #6 - 13
                if val not in node.valToCell:
                    node.valToCell[val] = Cell(val)
                cell = node.valToCell[val]

                #14 - 22
                if i == len(t) - 1:
                    #cell.isLeaf = True
                    cell.leafCount += 1 # use leafCount > 0 to represent isLeaf
                    if cell.leafCount > 1:
                        return (-1, -1)
                else:
                    node = cell.child
                    node.NOofEntity += 1
    return (root, depth)
            
            