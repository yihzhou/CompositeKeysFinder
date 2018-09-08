from EditDistance import isSameAttr
import sys

class AttrStorage:
    def __init__(self):
        self.dic = {} # attr -> parent attr, ancestor's parent is itself, child's parent is parent
        self.attrs = set()

    # union find to group attributes
    def findAncestor(self, attr):
        """
        :type: str, attribute
        :rtype: str, ancestor
        """
        while attr != self.dic[attr]:
            attr = self.dic[attr]
        return attr

    def insert(self, attr):
        """
        :type: str, attribute to be inserted
        :rtype: str, attribute's or similar attribute's ancestor
        """
        if attr in self.attrs:
            return self.findAncestor(attr)

        toFind = attr
        minDistance = sys.maxsize
        for storedAttr in self.attrs:
            # |attr's length - storedAttr's length| less then 10% attr's length
            # and (attr's set - storedAttr's set) less than 10% attr's length
            # and (storedAttr's set - attr's set) less than 10% attr's length
            # this is used to optimize
            s1 = set(attr)
            s2 = set(storedAttr)
            if max(abs(len(attr) - len(storedAttr)), len(s1 - s2), len(s2 - s1)) * 10 <= len(attr):
                isSame, distance = isSameAttr(attr, storedAttr, len(attr) // 10)
                if isSame:
                    if distance < minDistance:
                        minDistance = distance
                        toFind = storedAttr
        
        if toFind not in self.dic: # means toFind is attr, and it is never met before
            ancestor = toFind
        else: # means toFind is a similar storedAttr
            ancestor = self.findAncestor(toFind)
            
        self.dic[attr] = ancestor
        self.attrs.add(attr)

        return ancestor
            