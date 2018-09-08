from common import decode
from CompositeKeysStorage import KeysStorage
from PrefixTreeCreation import buildPrefixTree
from NonKeyFind import NonKeyFinder
from KeyFind import KeyFinder

def callMeStart(filePaths, columnNames):
    '''
    :type: [str]
    :type: [[str]]
    :rtype: {str : set(str)} 
    '''

    ks = KeysStorage()
    dic = {} # path -> keys

    for i, path in enumerate(filePaths):

        keys = ks.findCompositeKeys(columnNames[i])
        if len(keys) == 0:
            # build prefix tree
            root, depth = buildPrefixTree(path)
            if root == -1:
                dic[path] = []
            else:
                # initialize NonKeyFinder and find non-keys
                nonKFinder = NonKeyFinder(depth)
                nonKFinder.find(root, 0)

                # initialize KeyFinder and find keys from non-keys
                kFinder = KeyFinder(depth)
                keys = kFinder.find(nonKFinder.NonKeySet) # format {29318, 21938, 1121}

                translatedKeys = [] # [{'col1', 'col2', 'col3'}, {'col2', 'col4'}]
                for key in decode(keys, depth): # format ['000000010110010000', '100000000000000000', '010000000010010000']

                    # translate '000000010110010000' to format {'col1', 'col2', 'col3'}
                    translatedKey = set(columnNames[i][j] for j, digit in enumerate(key) if digit == '1')

                    # format [{'col1', 'col2', 'col3'}, {'col2', 'col4'}]
                    translatedKeys.append(translatedKey)

                    # record the key
                    ks.insert(translatedKey)
                dic[path] = translatedKeys
        else:
            dic[path] = keys

    return dic

if __name__ == '__main__':
    filePaths = ['d:\\toytest.csv', 'd:\\open-10000-1.csv', 'd:\\parking-10000.csv', 'd:\\4.csv', 'd:\\5.csv', 'd:\\6.csv', 'd:\\7.csv', 'd:\\8.csv']

    columnNames = [['col1', 'col2', 'col3'], ['col1', 'col3'], ['col1', 'col2', 'col3'], ['col1', 'col2',], ['col2', 'col3'], ['col1', 'col2', 'col3'], ['col2', 'col3'], ['col1', 'col2', 'col3']]

    callMeStart(filePaths, columnNames)