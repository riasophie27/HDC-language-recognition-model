# imports
from riaHDC import *
import numpy as np
from functools import reduce

# MAIN
#print("\n")

# encoding short text chunks (max. 4 characters )

def code_short_word(short_word, char_to_shifted_vector, vector_dimension):
   vectors = [] # create empty list
   for i, char in enumerate(short_word):
      base = char_to_shifted_vector.get(char, np.zeros(vector_dimension, dtype=np.uint8))
      vectors.append(np.roll(base, i))
   if not vectors:
      return np.zeros(vector_dimension, dtype=np.uint8)
   # XOR all vectors together
   return reduce(bind, vectors) 


# encoding text
def code_text(text, char_to_shifted_vector, vector_dimension, n):
    #print(f"Length of text: {len(text)}, n: {n}")
    if len(text) < n:
       #print("Text too short, returning zeros")
       return np.zeros(vector_dimension, dtype=np.uint8)
    acc = np.zeros(vector_dimension, dtype=np.uint32) #list of 0s with same length as my vector 
    count = 0 # set count 0 
    for i in range(len(text) - n + 1): # as long as in vector 
       chunk = text[i:i + n] # get one ngram 
       code_vec = code_short_word(chunk, char_to_shifted_vector, vector_dimension) # encode n gram 
       #print(f"Chunk: {chunk} Code vec sum: {np.sum(code_vec)}")
       acc += code_vec # add values positino to position (zip function)
       count += 1 
    threshold = (count + 1) // 2 
    return (acc >= threshold).astype(np.uint8)
"""
example_text = "hello"
example_vector = code_text(example_text, char_to_shifted_vector, 100, 5)
print("Example vector sum:", np.sum(example_vector))
print("Example vector sample:", example_vector[:10])
"""
   

