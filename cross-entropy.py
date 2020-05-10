import numpy as np # necessary for mathematics 

#number of elements
n = int(input("Enter number of elements : "))

#read category from user 
Y = list(map(int,input('\nEnter the category numbers  : ').strip().split()))[:n]

#read probabilities from user
P = list(map(float,input('\nEnter the probabilities  : ').strip().split()))[:n]

def cross_entropy(Y, P):
  """takes as input two lists Y, P,
  and returns the float corresponding to their cross-entropy."""

  Y = np.float_(Y) 
  P = np.float_(P)

  return - np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


print(cross_entropy(Y, P))