from numpy import *
from matplotlib.pyplot import *
import ID3, parse, random

'''
d1 = {'Class': 'n', 'Att': 1, 'Beta': 12}
d2 = {'Class': 'n', 'Att': 0, 'Beta': 27}
d3 = {'Class': 'y', 'Att': 0, 'Beta': 55}
d4 = {'Class': 'y', 'Att': 1, 'Beta': 12}
d5 = {'Class': 'y', 'Att': '?', 'Beta': 12}
examples1 = [d1, d2, d3, d4, d5, d1, d2, d5, d4, d5]
'''
'''
ex = [{'a':1, 'b':1, 'Class':2}, {'a':1, 'b':0, 'Class':2}, {'a':0, 'b':1, 'Class':1}, {'a':0, 'b':0, 'Class':0}]
tree = ID3.ID3(ex, 0)
print tree.breadth_first_search()
print tree.children.keys()
p = tree.children[1]
print p.train_num
testPruning()
testID3AndEvaluate()
testID3AndTest()
'''


def test_result(inFile):
    number1 = arange(10,25,1)
    number2 = arange(25,40,2)
    number3 = arange(40, 310, 10)
    number = concatenate((number1, number2, number3))
    result_np = []
    result_p = []
    data = parse.parse(inFile)
    ll = len(data)
    for j in number:
        print j
        withPruning = []
        withoutPruning = []
        for i in range(100):
            random.shuffle(data)
            train, valid, test = data[:2*j/3], data[2*j/3:j], data[j:]
            tree = ID3.ID3(train, 'democrat')
            acc_test = ID3.test(tree, test)
            # print "test accuracy: ", acc
            ID3.prune(tree, valid)
            acc_test_pruned = ID3.test(tree, test)
            # print "pruned tree train accuracy: ", acc
            withPruning.append(acc_test_pruned)
            withoutPruning.append(acc_test)
        average_acc_p = sum(withPruning) / len(withPruning)
        average_acc_np = sum(withoutPruning) / len(withoutPruning)
        result_np.append(average_acc_np)
        result_p.append(average_acc_p)
    print result_np
    print len(result_np), len(withoutPruning)
    print result_p
    print len(result_p), len(withPruning)
    print number
    print len(number)
    xlim(0, 310)
    ylim(0.7, 1)
    xlabel('Traning Number')
    ylabel('Accuracy')
    plot(number, result_np, color='blue', label="Without pruning")
    plot(number, result_p, color='orange', label="With pruning")
    legend(loc='lower right')
    show()


def test_result_1(inFile):
    number1 = arange(10,50,1)
    number2 = arange(50,150,5)
    number3 = arange(150, 305, 5)
    number = concatenate((number1, number2, number3))
    validnum = concatenate((number1*2, number2 + number2/2, number3 + number3/5))
    result_np = []
    result_p = []
    data = parse.parse(inFile)
    ll = len(data)
    c = 0
    for j in number:
        print j
        withPruning = []
        withoutPruning = []
        for i in range(100):
            random.shuffle(data)
            train, valid, test = data[:j], data[j:validnum[c]], data[validnum[c]:]
            tree = ID3.ID3(train, 'democrat')
            acc_test = ID3.test(tree, test)
            # print "test accuracy: ", acc
            ID3.prune(tree, valid)
            acc_test_pruned = ID3.test(tree, test)
            # print "pruned tree train accuracy: ", acc
            withPruning.append(acc_test_pruned)
            withoutPruning.append(acc_test)
        average_acc_p = sum(withPruning) / len(withPruning)
        average_acc_np = sum(withoutPruning) / len(withoutPruning)
        result_np.append(average_acc_np)
        result_p.append(average_acc_p)
        c = c+1
    print len(validnum), c
    print result_np
    print len(result_np), len(withoutPruning)
    print result_p
    print len(result_p), len(withPruning)
    #number = concatenate((number1, number2))
    print number
    print len(number)
    xlim(0, 305)
    ylim(0.8, 1)
    xlabel('Traning Number')
    ylabel('Accuracy')
    plot(number, result_np, color='blue', label="Without pruning")
    plot(number, result_p, color='orange', label="With pruning")
    legend(loc='lower right')
    show()
'''data = range(1,101)
ll = len(data)
j = 10
train, valid, test = data[:j], data[j:j+(ll-j)/2], data[j+(ll-j)/2:]
print train
print valid
print test'''
#data = parse.parse('house_votes_84.data')
#print len(data)

test_result_1('house_votes_84.data')

'''
number = range(50,100)
print number
result_np = arange(0.5,1,0.01)
print result_np
result_p = arange(0.75,1,0.005)
plot(number, result_p, color='orange', label="With pruning")
plot(number, result_np, color='orange', label="Without pruning")
print 'OK'
xlim(0, 310)
ylim(0.5, 1)
xlabel('Traning Number')
ylabel('Accuracy')
#plot(number, result_p, color='orange', label="With pruning")
#legend(loc='upper left')
show()'''
