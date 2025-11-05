# imports 
from ria_item_memory import * 
from riaHDC import * 
from ria_testing_data import* 
from ria_training_data import * 
from ria_ngrams import *
from ria_language_testing import * 



# define vector dimensions 
small_vector_dimensions = list(range(100,1001,100))
large_vector_dimensions = list(range(1000,10001,1000))
vector_dimensions = small_vector_dimensions + large_vector_dimensions

# (re-) define array length 
n = 4

results = []

np.random.seed(42)

for dim in vector_dimensions:
    #print(f"Testing vector dimension: {dim}")
    vector_dimension = dim

    # initialize item memory woith dimension 
    char_to_vector_np = initialize_item_memory(dim)

    char_to_shifted_vector = {
        char: cyclic_shift_right(vec) for char, vec in char_to_vector_np.items()
    }

    # clean texts
    #clean_train_text = clean_text(train_text, char_to_vector_np)
    #clean_test_text = clean_text(test_text, char_to_vector_np)

    # encode training vector 
    #train_vector = code_text(clean_train_text, char_to_shifted_vector, vector_dimension, n)
    language_vectors = {}
    for language, text in training_data.items():
        #print(f"{language} raw text (first 200 chars): {text[:200]!r}")
        clean_train_text = clean_text(text, char_to_vector_np)
        print(f"Sample cleaned text for {language}: {clean_train_text[:100]}")
      
        vec = code_text(clean_train_text, char_to_shifted_vector, vector_dimension, n)
        #print("Vector sum:", np.sum(vec))
        print(f"Vector sum for {language}: {np.sum(vec)}")  # check if vector is zero or not
        print(f"Vector sample (first 10 dims) for {language}: {vec[:10]}")


        language_vectors[language] = vec
    """
    print("\nVector sums of language representations:")
    for lang, vec in language_vectors.items():
        print(f"{lang}: sum={np.sum(vec)} sample={vec[:10]}")
    """

    correct = 0 
    total = 0 
    for language, text in testing_data.items():
        clean_test_text = clean_text(text, char_to_vector_np) 
        test_lines = clean_test_text.split("\n")

        for line in test_lines:
            if len(line) < n:
                continue
            test_vector = code_text(line, char_to_shifted_vector, vector_dimension, n)

            # compare with all languages 
            #sim = similarity(train_vector, test_vector)
            sims = {lang: similarity(test_vector, vec) for lang, vec in language_vectors.items()}
            predicted_lang = max(sims, key = sims.get)
            """
            if total < 5:
                print(f"Test line (len {len(line)}): {line[:50]!r}")
                print(f"Similarity scores: {sims}")
                print(f"Predicted: {predicted_lang}, Actual: {language}")
                print(f"Test vector sample: {test_vector[:10]}")
            """
            if predicted_lang == language:
                correct += 1
            total += 1 
        """
        total+=1

        if sim > 0.4:
           correct += 1 
        """
    """
    print(f"Similarity for line: {sim:.3f}")
    """
    accuracy  = correct / total if total > 0 else 0
    print(f"Accuracy at dimension {vector_dimension}: {accuracy:3f}")
    results.append((dim, accuracy))
    
