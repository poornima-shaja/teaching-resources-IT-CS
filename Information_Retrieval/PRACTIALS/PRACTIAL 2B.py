# Practical 2b: Vector Space Model using TF-IDF and Cosine Similarity

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "this is the first document",
    "this document is the second document",
    "and this is the third one",
    "is this the first document"
]

# Vectorize using TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())

# Example query similarity
query = ["this is the document"]
query_vector = tfidf_vectorizer.transform(query)

# Calculate cosine similarity
cos_sim = cosine_similarity(query_vector, tfidf_matrix)

print("\nCosine similarity scores for each document:")
print(cos_sim)
