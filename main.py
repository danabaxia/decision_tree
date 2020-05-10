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
    


def cal_I(m,n):
    return -m/(m+n)*math.log2(m/(m+n))-(n/(m+n)*math.log2(n/(m+n)))


data = "data.txt"
training_data_num = 0
attribute_num = 0
label = []


training_data_num = get_train_data_num(data)
label = get_labels(data, training_data_num)
attribute_num = get_attribute_num(data, training_data_num)

attribute = []
for i in range(attribute_num):
    attribute.append(get_attribute_data(data, training_data_num, i))

print(training_data_num)
print(label)
print(attribute_num)
for item in attribute:
    print(item)

