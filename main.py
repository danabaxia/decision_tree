import math 

def createDataSet(input):
    lines = []
    f = open(input)
    line_num = int(f.readline())
    for i in range(line_num):
        line = f.readline().strip()#remove first line
        lines.append(line)
        
    return lines

def retrieve_testVec(input):
    lines = []
    f = open(input)
    for i, line in enumerate(f):
        if i == 0:
            train_line_num = int(line)
            #print(train_line_num)
        if i == train_line_num + 1:
            test_line_num = int(line)
            #print(test_line_num)
        if i > train_line_num + 1:
            lines.append(line.strip())
    return lines


def get_train_data_num(input):
    fp = open(input)
    return int(fp.readline())

def get_labels(data):
    labels = []
    for x in range(len(data)):
        line = data[x].split()
        labels.append(line[0])
    return labels

def get_attribute_num(data):
    return len(data[0].split()) - 1

def get_attribute_label(data, pos):
    line = data[0].split()
    return line[pos+1].split(':')[0]

def get_attribute_data(data, order):
    attributes = [] # key is the feature
    for x in range(len(data)):
        line = data[x].split()
        attributes.append(line[order + 1].split(':')[1])
    return attributes

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
    label = get_labels(data) # label list 
    attribute_num = get_attribute_num(data) # attribute number 
    #print(attribute_num)
    attributes = []
    for i in range(attribute_num):
        attributes.append(get_attribute_data(data,i)) # nested list of attributes and its values in training data
    #print("attribute:")
    #print("\n".join([str(x) for x in attribute]))
    #print(attributes)
    bestGain = 0
    bestFeature = -1
    baseEntropy = cal_entropy(label)
    #print("length attributes", len(attributes))
    #print("length data", len(data))
    #print("Data",data)
    for i in range(len(attributes)):
        values = [] # all the values in one feature 
        newEntropy = 0
        #print(feature)
        for value in attributes[i]:
            if value not in values:
               values.append(value)
        #print("values")
        #print(values)
        
        feature = attributes[i]
        #print("feature")
        #print(feature)
        for value in values: #count labels for different values
            table = []
            #print(len(data))
            for m in range(len(data)):
                if feature[m] == value:
                    table.append(label[m])
            prob = len(table)/len(label)  
            newEntropy += prob * cal_entropy(table) # cal info for one feature 
        Gain = baseEntropy - newEntropy # cal info 
        #print(Gain)
        #print(i)
        if (Gain > bestGain):
            bestGain = Gain
            bestFeature = i
    return bestFeature

def createTree(data):
    label = get_labels(data) # label list 
    #print(label)
    if label.count(label[0]) == len(label):
        return label[0]  # only one label 
    if len(data) == 1:
        return label[0]  #only one line
    attribute_num = get_attribute_num(data) # attribute number 
    #print("attribute_num", attribute_num)
    attributes = []
    for i in range(attribute_num):
        attributes.append(get_attribute_data(data,i)) # nested list of attributes and its values in training data
    #print("attribute length",len(attributes))
    featureList = [] 
    for i in range(attribute_num):
        featureList.append(get_attribute_label(data, i)) # create feature label list 
    #print("featureList", featureList)
    axis= cal_best_feature(data)
    #print("axis", axis)
    bestFeature = featureList[axis]
    myTree = {bestFeature:{}} 
    #print(myTree)
    del featureList[axis]
    
    valueList = set(attributes[axis])

    #print("\n".join([str(x) for x in data]))
    #print("best feature",bestFeature)
    #print('value',valueList)
    #subdata = mySplit(data,axis,'1')
    #print("\n".join([str(x) for x in subdata]))
    #myTree[bestFeature] = createTree(mySplit(data,axis,2))
    for value in valueList:
        #print("value ", value)
        myTree[bestFeature][value] = createTree(mySplit(data,axis,value))
    
    #print(myTree)
    return myTree

def mySplit(data, feature, value):
    dataset_new = []
    attribute_num = get_attribute_num(data) # attribute number 
    attributes = []
    attribute = []
    for i in range(attribute_num):
        attributes.append(get_attribute_data(data,i)) # nested list of attributes and its values in training data
    attribute = attributes[feature]
    #print(len(attribute))
    for i in range(len(data)):
        line = data[i].split()
        del line[feature+1]
        if attribute[i] == value:
            new_line = ' '.join([str(elem) for elem in line])
            dataset_new.append(new_line)
    #print("nee dataset")
    #print("\n".join([str(x) for x in dataset_new]))
    return dataset_new

#def classify(inputTree, labels, testVec):


input = "data.txt"
training_data_num = get_train_data_num(input) # training data sample number
data = createDataSet(input) 
#print(cal_best_feature(data))
#createTree(data)
#for line in data:
#    print(line)
#data_new = mySplit(data,10,'2')
#for line in data_new:
#    print(line)
#print(createTree(data))
test = retrieve_testVec(input)
for line in test:
    print(line)
