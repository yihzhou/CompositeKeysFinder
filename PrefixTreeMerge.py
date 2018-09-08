from common import Node, Cell

#toMerge : [Node]
def merge(toMerge):
    '''
    :type: [Node]
    :rtype: Node
    '''
    # if there is only one node, return this node
    if len(toMerge) == 1:
        mergedNode = toMerge[0]
    else:
        mergedNode = Node()
        # mergedNode's number of entity passing it equals to sum of all toMerged nodes
        mergedNode.NOofEntity = sum(node.NOofEntity for node in toMerge)
        dic = {} #key: val, value: [cell]
        isLeaf = False #judge whether this is at the leaf level
        for node in toMerge:
            for val, cell in node.valToCell.items():
                if val not in dic:
                    dic[val] = []
                dic[val].append(cell)

                if cell.isLeaf():
                    isLeaf = True

        # 5
        for val, cellList in dic.items():
            # merge cells with the same val
            mergedNode.valToCell[val] = Cell(val)
            newCell = mergedNode.valToCell[val]

            if isLeaf:
                newCell.leafCount = sum(cell.leafCount for cell in cellList)
            else:
                # merge cells' children with the same val
                partialSet = [cell.child for cell in cellList]
                newCell.child = merge(partialSet)
    return mergedNode