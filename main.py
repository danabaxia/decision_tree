import math 

def get_train_data_num(data):
    fp = open(data)
    return int(fp.readline())

def get_labels(data, num):
    label = []
    fp = open(data)
    fp.readline()
    for x in range(num):
        line = fp.readline().split()
        label.append(line[0])
    return label

def get_attribute_num(data, num):
    fp = open(data)
    fp.readline()
    return len(fp.readline().split()) - 1

def get_attribute_data(data, num, order):
    attribute = []
    fp = open(data)
    fp.readline()
    for x in range(num):
        line = fp.readline().split()
        attribute.append(line[order + 1].split(':')[1])
    return attribute

def cal_I(m,n,l):
    t = m + n + l
    return -(m/t)*math.log2(m/t) - (n/t)*math.log2(n/t) - (l/t)*math.log2(l/t)
    
def cal_entropy(label):
    table = {}
    label_value = []
    entropy = 0
    total = len(label)
    for item in label:
        if item not in label_value:
            label_value.append(item)

    for item in label_value:
        table[item] = label.count(item)
    #print(table)    
    for key in table:
        entropy += -(table[key]/total)*math.log2(table[key]/total)
        #print(key, table[key], total)
    return entropy

def cal_best_feature(data):
    training_data_num = get_train_data_num(data) # training data sample number
    label = get_labels(data, training_data_num) # label list 
    attribute_num = get_attribute_num(data, training_data_num) # attribute number 
    attribute = []
    for i in range(attribute_num):
        attribute.append(get_attribute_data(data, training_data_num, i)) # nested list of attributes and its values in training data

    bestGain = 0
    bestFeature = -1
    baseEntropy = cal_entropy(label)
    for i in range(len(attribute)):
        values = [] # all the values in one feature 
        newEntropy = 0
        #print(feature)
        for value in attribute[i]:
            if value not in values:
                values.append(value)
        #print(values)
        
        feature = attribute[i]
        for value in values: #count labels for different values
            table = []
            for i in range(training_data_num):
                if feature[i] == value:
                    table.append(label[i])
            prob = len(table)/len(label)  
            newEntropy += prob * cal_entropy(table) # cal info for one feature 
        Gain = baseEntropy - newEntropy # cal info 
        #print(Gain)
        if (Gain > bestGain):
            bestGain = Gain
            bestFeature = i
    return bestFeature
"""
def createTree(label, attribute, training_data_num):
    if label.count(label[0]) == len(label):
        return label[0]  # only one label 

    bestFeature = cal_best_feature(label, attribute, training_data_num)
    bestFeat = tuple(attribute[bestFeature])
    print(bestFeat)
    myTree = {bestFeat:{}} 
    print(myTree)
    del attribute[bestFeature]
    valueList = set(attribute[bestFeature])
    print(valueList)
    for value in valueList: 
        myTree[bestFeat][value] = createTree()

"""



data = "data.txt"
#training_data_num = 0
#attribute_num = 0
#label = []
#entropy = 0
bestFeature = cal_best_feature(data)


"""
bestFeature = cal_best_feature(data)
bestFeat = tuple(attribute[bestFeature])
print(bestFeat)
myTree = {bestFeat:{}} 
print(myTree)
del attribute[bestFeature]
valueList = set(attribute[bestFeature])
print(valueList)
for value in valueList:
"""

