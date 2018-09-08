from CompositeKeysStorage import KeysStorage

keys = [set(['this is the 1st', 'this is the 2nd', 'this is the 3rd']),
        set(['this is he 2nd', 'this is the 3rrd', 'this is the 4th']),
        set(['this is the 1st']),
        set(['this is the 2nd']),
        set(['this is th 1st', 'this is tha 2nd', 'this is the 3rd'])]

attrslst = [set(['this s the 1st', 'thiis is the 2nd', 'this is the 3rd', 'this', 'is', 'nothing']),
            set(['thi si the 1st', 'this is the 2nd', 'this is the 3rd', 'attach', 'nothing']),
            set(['meaningless', 'this is he 2nd0', 'yes', 'this is the 3rrd0', 'no', 'this is the 4th'])]

ks = KeysStorage()
for key in keys:
    ks.insert(key)

for allAttrs in attrslst:
    res = ks.findCompositeKeys(allAttrs)
    print(res)
    print(0)