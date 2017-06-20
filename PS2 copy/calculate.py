from node import Node
from ID3 import *
from unit_tests import *
'''
d1 = {'Class':'n','outlook':'sunny','tem':'hot','hum':'high','wind':'weak'}
d2 = {'Class':'n','outlook':'sunny','tem':'hot','hum':'high','wind':'strong'}
d3 = {'Class':'y','outlook':'over','tem':'hot','hum':'high','wind':'weak'}
d4 = {'Class':'y','outlook':'rain','tem':'mild','hum':'high','wind':'weak'}
d5 = {'Class':'y','outlook':'rain','tem':'cool','hum':'normal','wind':'weak'}
d6 = {'Class':'n','outlook':'rain','tem':'cool','hum':'normal','wind':'strong'}
d7 = {'Class':'y','outlook':'over','tem':'cool','hum':'normal','wind':'strong'}
d8 = {'Class':'n','outlook':'?','tem':'mild','hum':'high','wind':'weak'}
d9 = {'Class':'y','outlook':'sunny','tem':'cool','hum':'normal','wind':'weak'}
d10 = {'Class':'y','outlook':'rain','tem':'mild','hum':'normal','wind':'weak'}
d11 = {'Class':'y','outlook':'sunny','tem':'?','hum':'normal','wind':'strong'}
d12 = {'Class':'y','outlook':'over','tem':'mild','hum':'high','wind':'strong'}
d13 = {'Class':'y','outlook':'over','tem':'hot','hum':'normal','wind':'weak'}
d14 = {'Class':'n','outlook':'rain','tem':'mild','hum':'high','wind':'strong'}

d15 = {'Class':'n','outlook':'rain','tem':'mild','hum':'?','wind':'weak'}
li = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]
s = ID3.ID3(li, Mode(li))

print s.breadth_first_search()
print s.children.keys()
p = s.children['rain']
p = p.children['weak']
print p.children.keys(), p.train_num
print p.label, p.parent.label, p.isleaf
print evaluate(s, d15)
prune(s, li)
print s.breadth_first_search()
'''
#testPruningOnHouseData('house_votes_84.data')
testID3AndTest()
testID3AndEvaluate()
testPruning()

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
