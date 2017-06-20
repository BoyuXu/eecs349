from node import Node
from ID3 import *
from unit_tests import *


d1 = {'Class':'n','outlook':'sunny','tem':'hot','hum':'high','wind':'weak'}
d2 = {'Class':'n','outlook':'sunny','tem':'hot','hum':'high','wind':'strong'}
d3 = {'Class':'y','outlook':'over','tem':'hot','hum':'high','wind':'weak'}
d4 = {'Class':'y','outlook':'rain','tem':'mild','hum':'high','wind':'weak'}
d5 = {'Class':'y','outlook':'rain','tem':'cool','hum':'normal','wind':'weak'}
d6 = {'Class':'n','outlook':'rain','tem':'cool','hum':'normal','wind':'strong'}
d7 = {'Class':'y','outlook':'over','tem':'cool','hum':'normal','wind':'strong'}
d8 = {'Class':'n','outlook':'sunny','tem':'mild','hum':'high','wind':'weak'}
d9 = {'Class':'y','outlook':'sunny','tem':'cool','hum':'normal','wind':'weak'}
d10 = {'Class':'y','outlook':'rain','tem':'mild','hum':'normal','wind':'weak'}
d11 = {'Class':'y','outlook':'sunny','tem':'?','hum':'normal','wind':'strong'}
d12 = {'Class':'y','outlook':'over','tem':'mild','hum':'high','wind':'strong'}
d13 = {'Class':'y','outlook':'over','tem':'hot','hum':'normal','wind':'weak'}
d14 = {'Class':'n','outlook':'rain','tem':'mild','hum':'high','wind':'strong'}

# d1 = {'Class': 'n', 'Att': 1, 'Beta': 12}
# d2 = {'Class': 'n', 'Att': 0, 'Beta': 27}
# d3 = {'Class': 'y', 'Att': 1, 'Beta': 55}
# d4 = {'Class': 'y', 'Att': 1, 'Beta': 12}
# d5 = {'Class': 'y', 'Att': '?', 'Beta': 12}

# li = [d1,d2,d3,d4,d5,d2]
# xx = miss_class(li, 'Att')
# print xx
#
# d15 = {'Class':'n','outlook':'rain','tem':'mild','hum':'normal','wind':'?'}
# li = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]
# s = ID3.ID3(li, Mode(li))
#
# print s.breadth_first_search()
# print s.children.keys()
# p = s.children['rain']
# q = p.children['weak']
# print p.children.keys(), p.train_num
# print q.label
# print evaluate(s, d15)
# prune(s, li)
# print s.breadth_first_search()
# print test(s, li+[d15])


def testPruning1():
    data = [dict(a=1, b=0, Class=0), dict(a=1, b=1, Class=0), dict(a=0, b=1, Class=1)]
    validationData = [dict(a=1, b=0, Class=0), dict(a=1, b=1, Class=0), dict(a=0, b=0, Class=0), dict(a=0, b=0, Class=0)]
    tree = ID3.ID3(data, 0)
    print tree.breadth_first_search()
    ID3.prune(tree, validationData)
    print tree.breadth_first_search()
    if tree != None:
        ans = ID3.evaluate(tree, dict(a=0, b=0))
        if ans != 0:
            print "pruning test failed."
        else:
            print "pruning test succeeded."
    else:
        print "pruning test failed -- no tree returned."

def testPruning2():
  data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1), dict(a=0, b=1, Class=0), dict(a=0, b=0, Class=1)]
  validationData = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1), dict(a=0, b=0, Class=0), dict(a=0, b=0, Class=0)]
  tree = ID3.ID3(data, 0)
  print tree.breadth_first_search()
  ID3.prune(tree, validationData)
  print tree.breadth_first_search()
  if tree != None:
    ans = ID3.evaluate(tree, dict(a=0, b=0))
    if ans != 0:
      print "pruning test failed."
    else:
      print "pruning test succeeded."
  else:
    print "pruning test failed -- no tree returned."
'''
n1 = Node()
n1.label = 1
n2 = Node()
n2.label = 2
n3 = Node()
n3.label = 3
n1.children = {'a':n2, 'b':n3}
n4 = Node()
n4.label = 4
n4.train_num = {1:3, 0:1}
n5 = Node()
n5.label = 5
n5.train_num = {1:0, 0:4}
n6 = Node()
n6.label = 6
n2.children = {'a':n4, 'b':n5}
n3.children = {'a':n6, 'b':n4}
n2.train_num = train_num_from_child(n2)
n3.train_num = train_num_from_child(n3)
print train_num_from_child(n1)

print sum({}.values())'''




testPruningOnHouseData('house_votes_84.data')
testID3AndTest()
testID3AndEvaluate()
testPruning()
testPruning1()

def findleaf(root):
    trans = post_trans(root)
    leafs = []
    for n in trans:
        if n.isleaf == 1:
            if len(n.train_num) > 1:
                leafs.append(n)
    return leafs

def testPruningOnHouseData1(inFile):
    withPruning = []
    withoutPruning = []
    data = parse.parse(inFile)
    for i in range(1):
        random.shuffle(data)
        train = data[:len(data) / 2]
        valid = data[len(data) / 2:3 * len(data) / 4]
        test = data[3 * len(data) / 4:]

        tree = ID3.ID3(train, 'democrat')
        nlist = findleaf(tree)
        for n in nlist:
            print n.label, n.train_num
        #print tree.breadth_first_search()
        acc = ID3.test(tree, train)
        print "training accuracy: ", acc
        # acc = ID3.test(tree, valid)
        # #print "validation accuracy: ", acc
        # acc = ID3.test(tree, test)
        # #print "test accuracy: ", acc
    #
    #     ID3.prune(tree, valid)
    #     acc = ID3.test(tree, train)
    #     #print "pruned tree train accuracy: ", acc
    #     acc = ID3.test(tree, valid)
    #     #print "pruned tree validation accuracy: ", acc
    #     acc = ID3.test(tree, test)
    #     #print "pruned tree test accuracy: ", acc
    #     withPruning.append(acc)
    #     tree = ID3.ID3(train + valid, 'democrat')
    #     acc = ID3.test(tree, test)
    #     #print "no pruning test accuracy: ", acc
    #     withoutPruning.append(acc)
    # #print withPruning
    # #print withoutPruning
    # print "average with pruning", sum(withPruning) / len(withPruning), " without: ", sum(withoutPruning) / len(
    #     withoutPruning)

# testPruningOnHouseData1('house_votes_84.data')

# data = parse.parse('house_votes_84.data')
# tree = ID3.ID3(data, 'democrat')
# print test(tree,data)
# nlist = findleaf(tree)
# for n in nlist:
#     print n.label, n.train_num
#     print n.parent.label, n.parent.children.keys(), n.parent.train_num
#     n = n.parent.children['y']
#     print n.label
# dx = {'handicapped-infants': 'y', 'export-administration-act-south-africa': 'y', 'superfund-right-to-sue': 'y', 'education-spending': 'n', 'duty-free-exports': 'n', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'y', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'y', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'n', 'Class': 'democrat'}
# print evaluate(tree, dx)
# data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1), dict(a=0, b=1, Class=0), dict(a=0, b=0, Class=1), dict(a=0, b=0, Class=0)]
# tree = ID3.ID3(data, 0)
# print tree.breadth_first_search()
# print test(tree, data)
