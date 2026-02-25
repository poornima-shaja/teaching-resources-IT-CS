# Practical 3: Spelling Correction and Integration with IR System

# ------------------ Part A: Levenshtein Distance ------------------

def levenshtein_distance(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    
    # Initialize matrix
    matrix = [[0 for _ in range(len_str2)] for _ in range(len_str1)]
    
    # Initialize first row and first column
    for i in range(len_str1):
        matrix[i][0] = i
    for j in range(len_str2):
        matrix[0][j] = j
    
    # Fill the matrix
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            cost = 0 if str1[i-1] == str2[j-1] else 1
            matrix[i][j] = min(
                matrix[i-1][j] + 1,      # Deletion
                matrix[i][j-1] + 1,      # Insertion
                matrix[i-1][j-1] + cost  # Substitution
            )
    
    return matrix[len_str1 - 1][len_str2 - 1]


def suggest_correction(word, word_list):
    # Compute distance for each word in dictionary
    distances = [(w, levenshtein_distance(word, w)) for w in word_list]
    
    # Sort by distance
    distances.sort(key=lambda x: x[1])
    
    # Return the word with minimum distance
    return distances[0][0]


# ------------------ Part B: Integration with IR System ------------------

def retrieve_information(query, dictionary):
    query_words = query.split()
    corrected_words = [suggest_correction(word, dictionary) for word in query_words]
    
    corrected_query = ' '.join(corrected_words)
    
    # Simulated retrieval stage
    print(f"Retrieving information for corrected query: '{corrected_query}'")


# ------------------ Main Program ------------------

if __name__ == "__main__":
    
    # Test for spelling correction (3a demonstration)
    input_word = "poonimo"
    word_list = ["hello", "world", "python", "spell", "correct", "algorithm", "poornima", "poohnima"]
    
    suggested_correction = suggest_correction(input_word, word_list)
    print(f"Suggested correction for '{input_word}': {suggested_correction}")
    
    print("\n-----------------------------\n")
    
    # Demo for IR Integration (3b demonstration)
    user_query = "speling correctin algorithm"
    dictionary = ["spelling", "correction", "algorithm", "information", "retrieval", "system"]
    
    retrieve_information(user_query, dictionary)
