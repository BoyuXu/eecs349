import sys
from sys import  path
path.append(r'//Users/apple/Desktop/Boyu_Xu_hw1')
import MainDT

if __name__ == '__main__':
    inputFileName, \
    trainingSetSize, \
    numberOfTrials, \
    verbose = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    sum_pp, sum_pt = 0, 0
    for i in range(numberOfTrials):
        print '\n'
        print 'TRIAL NUMBER: {}'.format(i)
        print '\n'
        len_train, len_test, pt, pp = MainDT.main(inputFileName, trainingSetSize, verbose)
        sum_pt += pt
        sum_pp += pp

    print '\n'
    print 'example file used = {}'.format(inputFileName)
    print 'number of trials = {}'.format(numberOfTrials)
    print 'training set size for each trial = {}'.format(len_train)
    print 'testing set size for each trial = {}'.format(len_test)
    print 'mean performance of decision tree over all trials = {}% correct classification'.format(sum_pt / numberOfTrials)
    print 'mean performance of using prior probability derived from the training set = {}% correct classification'.format(sum_pp / numberOfTrials)
