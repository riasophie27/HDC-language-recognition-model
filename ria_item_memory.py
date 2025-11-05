
# imports
from riaHDC import * 
import numpy as np
import string
import csv
import random


random.seed(27) # for same results
np.random.seed(27)

vector_dimension = 10000                   
# Subroutines
"""
def vector_initialize(vector_dimension):
   vector = []
   for i in range(vector_dimension):
       vector.append(random.randint(beg,end))
   return vector
"""

# speed up version 
def vector_initialize(vector_dimension):
    return np.random.randint(0, 2, size=vector_dimension, dtype=np.uint8)


def print_random_vector():
   print("Here is a random vector: ")
   print("\n")
   lst = vector_initialize(vector_dimension)
   print(lst)
   return lst

def initialize_item_memory(vector_dimension):
   letters     = list(string.ascii_letters)
   digits      = list(string.digits)
   punctuation = list(string.punctuation)
   whitespace  = list(string.whitespace)

   all_symbols = letters + digits + punctuation + whitespace

   # initlaize vectors for each symbol 
   all_vectors = np.random.randint(0, 2, size=(len(all_symbols), vector_dimension), dtype=np.uint8)

   #assign each character to a vector
   #char_to_vector = {char: tuple(all_vectors[i]) for i, char in enumerate(all_symbols)}
   char_to_vector = {char: all_vectors[i] for i, char in enumerate (all_symbols)}
   return char_to_vector

# save to csv
def save_item_memory_to_csv(item_memory, filename="Rias_item_memory.csv"):
   with open(filename, mode = "w", newline = "") as file:
       writer = csv.writer(file)
       writer.writerow(["character"] + [f"dim{i}" for i in range(vector_dimension)])
       for char, vec in item_memory.items():
           writer.writerow([char] + list(vec)) 

def load_item_memory_from_csv(filename="Rias_item_memory.csv"):
    item_memory= {} 
    with open(filename, mode = "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            char = row[0]
            vec = np.array([int(bit) for bit in row[1:]], dtype=np.uint8)
            item_memory[char] = vec
    return item_memory 

# example usage 
if __name__ == "__main__":
    char_to_vector = initialize_item_memory(vector_dimension)
    save_item_memory_to_csv(char_to_vector)

    vec = char_to_vector["a"]
    print("Sample vector for 'a':", vec[:10], "Sum:", np.sum(vec))
    
