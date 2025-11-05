# imports 
from ria_training_data import *
from ria_testing_data import * 
from ria_ngrams import *
import numpy as np

# variables 
train_text  = eng
test_text   = eng_tst

# Subroutines
# use the hamming method 
"""
def similarity(vector_a, vector_b):
    same_values = 0 
    for i in range(len(vector_a)):
        if vector_a[i]     == vector_b[i]: # if same value
            same_values    += 1 # add 1 
    return same_values / len(vector_a)
"""

# replace to make it faster 
def similarity(vector_a, vector_b):
    return 1 - np.mean(np.bitwise_xor(vector_a, vector_b))

"""
# in case there are any non-printable characters (was the case in the polish text)
def clean_text(vector_a, item_memory):
    clean_text = ""
    for char in vector_a:
        if char in item_memory:
            clean_text += char 
    return clean_text
"""

def clean_text(text, item_memory):
    item_set = set(item_memory.keys())
    return '' .join([char for char in text if char in item_set])


# main 
"""
train_vector = code_text(clean_text(train_text, item_memory), item_memory) # langauge traning data vector (rn: english)
test_rows    = test_text.split("\n") # splits it into the lines
"""

clean_train_text = clean_text(train_text, char_to_vector_np)
clean_test_text = clean_text(test_text, char_to_vector_np)

train_vector = code_text(clean_train_text, char_to_shifted_vector, vector_dimension, n)

test_lines = clean_test_text.split("\n")

similarities = [] # creates the list where i will see the similarities of each line later 
for line in test_lines: # going through each line in the testing file 
    if len(line) < n:
        continue
    test_vector  = code_text(line, char_to_shifted_vector, vector_dimension, n) # genersates vector for that line
    sim          = similarity(train_vector, test_vector) # uses similarity function that we definened earlier 
    similarities.append(sim) # add similiarity score to the list for each line 


# test
"""
print("Similiarities between test data and training data for each line: ")
print("\n")
pretty_similarities = [round(float(x), 3) for x in similarities]
print(pretty_similarities)
"""

