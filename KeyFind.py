
class KeyFinder:
    def __init__(self, depth):
        self.depth = depth
        # construct a all-one binary integer 111111111
        self.allOnes = 0
        for i in range(depth):
            self.allOnes |= (1 << i)

    def insert(self, KeySet, key):
        '''
        :type: {int}
        :type: int
        '''
        toAdd = True
        # if key covers stored key, then stored key is candidate key that covers key, so not add key
        for storedKey in KeySet:
            if storedKey & key == storedKey:
                toAdd = False
                break
        
        # if add key, remove all stored keys that are covered by key
        if toAdd:
            for storedKey in list(KeySet):
                if storedKey & key == key:
                    KeySet.remove(storedKey)
            KeySet.add(key)

    def find(self, NonKeySet):
        '''
        :type: {int}
        :rtype: {int}
        '''
        KeySet = set()
        for nonKey in NonKeySet:
            complementSet = nonKey ^ self.allOnes # complement of nonKey, example nonKey: 1010101, complement: 0101010

            if len(KeySet) == 0:
                for i in range(self.depth):
                    if (complementSet >> i) & 1 == 1:
                        KeySet.add(1 << i) # {0100000, 0001000, 0000010}, this three keys are not included by nonKey 1010101
            else:
                newSet = set()
                for i in range(self.depth):
                    if (complementSet >> i) & 1 == 1:
                        pKey = (1 << i)
                    
                        for key in KeySet:
                            newKey = key | pKey # the key not included by curNonKey and previous NonKey
                            self.insert(newSet, newKey)
                KeySet = newSet
        return KeySet