import csv
import random
import math
#read file(dic)
def read_file(fileName):
    dataset = []
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            dataset.append(row)
    return dataset

#split to traning and testing(dic)
def split_sample(dataset, train_num):
    random.shuffle(dataset)
    training, testing = dataset[:train_num], dataset[train_num:]
    return training, testing

#calculate entrophy
#calculate while class=true, propotion`
def get_prior(sample):
    num_true = sum([1 if x['CLASS'] == 'true' else 0 for x in sample])
    return float(num_true) / len(sample)

#entrophy
def calc_entropy(sample):
    if len(sample) == 0:
        return 0
    p = get_prior(sample)
    if p == 0 or p == 1:
        return 0
    return -(p * math.log(p, 2) + (1 - p) * math.log(1 - p, 2))

#function of get subset(split attribute,true of false)
def get_subset(dataset, fea_name, fea_value):
    subset = filter(lambda x: x[fea_name] == fea_value, dataset)
    return subset

#calculate information gain.
def calc_information_gain(sample, feature_name):
    sample_entropy = calc_entropy(sample)
    total = len(sample)
    subset_true = get_subset(sample, feature_name, 'true')
    subset_false = get_subset(sample, feature_name, 'false')
    h_true = calc_entropy(subset_true)
    h_false = calc_entropy(subset_false)
    ig = sample_entropy -\
         float(len(subset_true)) / total * h_true -\
         float(len(subset_false)) / total * h_false
    return ig

#form a dictionary(attributename,key:gain),find the biggest information gain
def choose_best_feature(sample, fea_names):
    igs = dict(zip(fea_names, [calc_information_gain(sample, f) for f in fea_names]))
#sorted from biggest to small
    sorted_igs = sorted(igs.items(), key=lambda x:x[1], reverse=True)
    return sorted_igs[0][0]

#corner case if all attribute has been used and left +1,-3,then we define them all as t of f
def majority_class(sample):
    p_t = get_prior(sample)
    if p_t >= 0.5:
        return 'true'
    else:
        return 'false'

#construct id3tree(dictionary)
def construct_dt_id3(sample, fea_names):
    classes = [x['CLASS'] for x in sample]
    #if all true or all false
    if classes.count(classes[0]) == len(classes):
        return classes[0]
    #consider corner case
    if len(fea_names) == 0:
        return majority_class(sample)
    feature = choose_best_feature(sample, fea_names)
    tree = {feature:{}}
    sub_true = get_subset(sample, feature, 'true')
    sub_false = get_subset(sample, feature, 'false')
    if len(sub_true) > 0:
        tree[feature]['true'] = construct_dt_id3(sub_true, [f for f in fea_names if f != feature])
    if len(sub_false) > 0:
        tree[feature]['false'] = construct_dt_id3(sub_false, [f for f in fea_names if f != feature])
    return tree

def classify_recursive(tree, test_case):
    if isinstance(tree, dict):
        #useup all the attributes
        key, value = tree.items()[0]
        return classify_recursive(value[test_case[key]], test_case)
    else:
        return tree

def perform_classify(tree, prior, test_set, verbose):
    c_t, c_p = 0, 0
    #test prior
    for test in test_set:
        p = random.random()
        if p < prior:
            c_p += test['CLASS'] == 'true'
        else:
            c_p += test['CLASS'] == 'false'
        result = classify_recursive(tree, test)
        c_t += (result == test['CLASS'])
    pt = 100 * c_t / len(test_set)
    pp = 100 * c_p / len(test_set)
    print 'Percent of test cases correctly classified by a decision tree built with ID3 = {}%'.format(pt)
    print 'Percent of test cases correctly classified by using prior probabilities from the training set = {}%'.format(pp)
    return pt, pp

# get node name/leaf
def get_node_name(node):
    if isinstance(node, dict):
        return node.keys()[0]
    else:
        return 'leaf'

# print tree
def print_tree(tree, parent):
    if isinstance(tree, dict):
        key, value = tree.items()[0]
        print 'parent: {} attribute: {} trueChild:{} falseChild:{}'\
        .format(parent, key, get_node_name(value['true']), get_node_name(value['false']))
        print_tree(value['true'], key)
        print_tree(value['false'], key)
    else:
        print 'parent: {} -'.format(parent)

# main method for input to output
def main(inputFileName, trainingSetSize, verbose):
    dataset = read_file(inputFileName)
    fea_names = dataset[0].keys()
    print fea_names
    fea_names.remove('CLASS')
    train_set, test_set = split_sample(dataset, trainingSetSize)
    tree = construct_dt_id3(dataset, fea_names)
    print 'DECISION TREE STRUCTURE:'
    print_tree(tree, 'root')
    pt, pp = perform_classify(tree, get_prior(train_set), test_set, verbose)
    return len(train_set), len(test_set), pt, pp
