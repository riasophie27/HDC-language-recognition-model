# imports
from ria_item_memory import load_item_memory_from_csv, vector_dimension
from testing_file_paths import *
import numpy as np
from ria_ngrams import *
from training_file_paths import * 

# set parameters
n = 3

# initialize item memory
char_to_vector_np = load_item_memory_from_csv("Rias_item_memory.csv")
char_to_shifted_vector = {c: np.roll(v, 1) for c, v in char_to_vector_np.items()}
valid_chars = set(char_to_vector_np.keys())

def clean_text(txt):
    return ''.join([ch for ch in txt if ch in valid_chars])

def similarity(v1, v2):
    return 1.0 - np.mean(np.bitwise_xor(v1, v2))
    
    
    
    
# create dictionaries
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

language_vectors = {
    lang: code_text(clean_text(txt), char_to_shifted_vector, vector_dimension, n)
    for lang, txt in training_data.items()
}

testing_data = {
    "danish":      dan_tst,
    "german":      deu_tst,
    "english":     eng_tst,
    "french":      fra_tst,
    "italian":     ita_tst,
    "dutch":       nld_tst,
    "polish":      pol_tst,
    "portuguese":  por_tst,
    "spanish":     spa_tst,
    "swedish":     swe_tst,
}

correct = 0 
total = 0 
for gold_lang, txt in testing_data.items():
    for line in clean_text(txt).split("\n"):
        if len(line) < n:
            continue
        v = code_text(line, char_to_shifted_vector, vector_dimension, n)
        sims = {lang: similarity(v, vec) for lang, vec in language_vectors.items()}
        pred = max(sims, key = sims.get)
        correct += int(pred == gold_lang)
        total += 1

acc = correct / total if total else 0.0
print(f"Accuracy: {acc:.3f} ({correct}/{total})")
