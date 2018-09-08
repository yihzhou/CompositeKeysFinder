from PrefixTreeMerge import merge

class NonKeyFinder:
    def __init__(self, depth):
        self.NonKeySet = set() # all nonKeys
        self.curNonKey = 0 # processing nonKey
        self.depth = depth # how many columns

    def insert(self, NonKey):
        '''
        :type: int
        '''
        toAdd = True
        # if any stored non-key covers this non-key, then not add it
        for storedNonKey in self.NonKeySet:
            if storedNonKey & NonKey == NonKey:
                toAdd = False
                break
        
        # if add this non-key, remove all stored non-keys that are covered by this non-key
        if toAdd:
            for storedNonKey in list(self.NonKeySet):
                if storedNonKey & NonKey == storedNonKey:
                    self.NonKeySet.remove(storedNonKey)
            self.NonKeySet.add(NonKey)
            print(NonKey)

    def find(self, root, attrNo):
        '''
        :type: Node
        :type: int
        '''
        root.visited = True

        #record current non-key as origin, and add attrNo to it, get new current non-key
        origin = self.curNonKey
        self.curNonKey |= (1 << attrNo) # set current attribute(column) as 1 (included)

        isLeaf = any(cell.isLeaf() for cell in root.valToCell.values())

        # if more than one entity pass the leaf, then add current non-key
        if isLeaf:
            for cell in root.valToCell.values():
                if cell.leafCount != 1:
                    self.insert(self.curNonKey)
                    break

            # remove attrNo, rollback current non-key
            # if it has multiple branches of cells or in one single branch, there is multiple entity passing it, then insert origin non-key
            self.curNonKey = origin
            if len(root.valToCell) > 1 or any(cell.leafCount > 1 for cell in root.valToCell.values()):
                self.insert(self.curNonKey)
        else:
            # if only one entity pass here, it must not be a non-key
            if root.NOofEntity == 1:
                return

            for cell in root.valToCell.values():
                # singleton pruning, if visited, it is shared prefix tree node, no need to visit again
                if not cell.child.visited:
                    self.find(cell.child, attrNo + 1)
            
            self.curNonKey = origin # remove attribute(column) from curNonKey

            # futile pruning, if there is a stored non-key covering all possible non-keys to be processed, then no need to continue
            # example, unremoved curNonKey 001 110, origin 000 110, check whether 110 110 is futile or not
            # if there is more than one cell (child node) to be merged
            if len(root.valToCell) > 1: 
                nonKey = self.curNonKey
                for i in range(attrNo + 1, self.depth):
                    nonKey |= (1 << i)
                if self.isFutile(nonKey):
                    return
                
                mergeTree = merge([cell.child for cell in root.valToCell.values()])
                self.find(mergeTree, attrNo + 1)


    def isFutile(self, nonKey):
        '''
        :type: int
        :rtype: bool
        '''
        for storedNonKey in self.NonKeySet:
            if storedNonKey & nonKey == nonKey:
                return True
        return False