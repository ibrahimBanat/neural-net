import numpy as np # necessary for mathematics 

#number of elements
n = int(input('Enter number of elements : '))

#read inputs from user
inplist = list(map(int,input('\nEnter the numbers : ').strip().split()))[:n]

def softmax(list):
    """Takes as input list of numbers, and returns the list 
    of values given by the softmax function.
    """ 
    expl = np.exp(list)
    segmal = sum(expl)
    result = []

    for item in expl:
        result.append(item*1 / (segmal))

    return result 
    
print(softmax(inplist))