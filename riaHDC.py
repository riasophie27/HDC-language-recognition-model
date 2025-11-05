
#imports
import random
import numpy as np 

# Configuration Variables
#beg, end         = 0, 1 # random integer between those two integers
vector_dimension = 10000 # length of vector

"""
# Subroutines
def vector_initialize(vector_dimension): # define vector
   vector = [] # create empty list
   for i in range(vector_dimension): # as long as integer i is not larger than the vector range
       vector.append(random.randint(beg,end)) # add random integer to end of vector
   return vector
"""


def clean_text(text, item_memory):
    # Keep only characters that are keys in item_memory
    return ''.join([char for char in text if char in item_memory])

# speed up version 
def vector_initialize(vector_dimension):
    return np.random.randint(0, 2, size=vector_dimension, dtype=np.uint8)

# permutation: cyclic shift: first number becomes sencond,..., last number becomes first
"""
def cyclic_shift_right(lst):
   lst  = lst.copy()
   last = lst.pop()     #removes last element
   lst.insert(0, last)  #inserts it at the beginning
   return lst
"""
# speed up version 
def cyclic_shift_right(vector):
    return np.roll(vector,1)

# binding: multiply first value of v1 and v2, multiply second value of v1 and v2,...
"""
def bind(lst1, lst2):
   result = [] # creates empty list
   for i in range(len(lst1)): # as long as is not larger than list length
       result.append(lst1[i] ^ lst2[i]) # ^ for XOR
   return result
"""
# speed up version 
def bind(vec1, vec2):
    return np.bitwise_xor(vec1, vec2)

# bundle and binarizing
"""
def bundle(vectors):
   vector_length = len(vectors[0]) # find length of vector
   result        = [] # create empty list
   threshold     = (len(vectors) + 1) // 2   #majority gate

   for i in range(vector_length): # as long as is not larger than list length
       summm     = sum(vec[i] for vec in vectors) # sum of the first, second,... of the two vectors
       if summm >= threshold: # if the sum is larger than the threshold
           result.append(1) # then add 1 to end of vector
       else:
           result.append(0) # otherwise add 0 to end of vector
   return result
"""
# speed up version 
def bundle(vectors):
    summed = np.sum(vectors, axis=0)
    threshold = (vectors.shape[0] + 1) // 2 
    return (summed >= threshold).astype(np.uint8)
  

# Main

random_integer = np.random.randint(0, 1+1)
random_list = vector_initialize(vector_dimension)
import numpy as np

if __name__ == "__main__":
    a = np.array([1,0,1,0,1], dtype=np.uint8)
    b = np.array([0,0,1,1,0], dtype=np.uint8)

    print(bind(a,b))  # should print [1 0 0 1 1]