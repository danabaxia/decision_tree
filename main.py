import math 

def cal_I(m,n):

    return -m/(m+n)*math.log2(m/(m+n))-(n/(m+n)*math.log2(n/(m+n)))



training_data_num = 0
training_data_single = {}
training_data = {}
#read file 
with open("data.txt") as fp:
    training_data_num = int(fp.readline())
    for line in fp.readlines(): 
        for element in line.split():
            print(element)