# CompositeKeysFinder
Efficient and scalable discovery of composite keys over large-size dataset

## Build prefix tree
PrefixTreeCreation.py  
root, depth = buildPrefixTree(path)  

## Merge prefix tree nodes
PrefixTreeMerge.py

## Find all non-keys
NonKeyFind.py  
nonKFinder = NonKeyFinder(depth)  
nonKFinder.find(root, 0)  

## Find keys from non-keys
KeyFind.py  
kFinder = KeyFinder(depth)  
keys = kFinder.find(nonKFinder.NonKeySet)  

## Attribute storage & Keys storage
AttributesStorage.py  
CompositeKeysStorage.py  
Used to find keys based on stored keys
