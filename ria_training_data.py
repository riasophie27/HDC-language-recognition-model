# imports
from ria_item_memory import initialize_item_memory, save_item_memory_to_csv, vector_dimension
from ria_ngrams import * 
from riaHDC import *
from training_file_paths import *

import numpy as np

# set parameters
n = 4

# initialize item memory
char_to_vector_np = initialize_item_memory(vector_dimension)
char_to_shifted_vector = {c: np.roll(v, 1) for c, v in char_to_vector_np.items()}
save_item_memory_to_csv(char_to_vector_np, "Rias_item_memory.csv")

# create dictionary
training_data = {
    "danish": dan,
    "german": deu,
    "english": eng,
    "french": fra,
    "italian": ita,
    "dutch": nld,
    "polish": pol,
    "portuguese": por,
    "spanish": spa,
    "swedish": swe,
}

valid_chars = set(char_to_vector_np.keys())
language_given_example = {} # creates empty dictionary 


for language, text in training_data.items():
    clean_text = ''.join([char for char in text if char in valid_chars])
    language_given_example[language] = code_text(clean_text, char_to_shifted_vector, vector_dimension, n)

print("Training vectors created:")
for lang, vec in language_given_example.items():
    print(f"{lang:10s} → sum={np.sum(vec)}  first10={vec[:10]}")

