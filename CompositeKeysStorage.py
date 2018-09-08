from AttributesStorage import AttrStorage

# lazy mode is to find any one composite key, greedy is to find all composite keys from existing keys
LAZY, GREEDY = 0, 1

class KeysStorage:
    def __init__(self):
        self.keys = [] # [attrs]
        self.attrs = AttrStorage()
    
    #this function is for the key that is discovered by Gordian Algorithm
    def insert(self, key):
        """
        :type: set(str)
        """
        # if len(key) <= 1:
        #     return

        new_key = set()
        for attr in key:
            ancestor = self.attrs.insert(attr)
            new_key.add(ancestor)

        if any(new_key == storedAttrs for storedAttrs in self.keys):
            return

        self.keys.append(new_key)

    #this function is for discovering keys without running Gordian
    #it returns only keys consisting of two or more attributes
    def findCompositeKeys(self, allAttrs, mode=GREEDY):
        """
        :type: set(str)
        :type: LAZY or GREEDY
        :rtype: [set(str)]
        """
        # ancestor attr -> this attr
        newToOldAttrs = {}
        # set(ancestor attr)
        new_allAttrs = set()

        # convert attrs to ancestors
        for attr in allAttrs:
            ancestor = self.attrs.insert(attr)
            newToOldAttrs[ancestor] = attr
            new_allAttrs.add(ancestor)

        res = []
        # if existing key is a subset of this attrs, then add it to result (only record composite keys consisting of more than 1 attrs)
        for storedAttrs in self.keys:
            if storedAttrs.issubset(new_allAttrs):
                old_Attrs = set(newToOldAttrs[attr] for attr in storedAttrs)
                if len(old_Attrs) >= 2:
                    res.append(old_Attrs)
                    if mode == LAZY:
                        return res
        return res
        