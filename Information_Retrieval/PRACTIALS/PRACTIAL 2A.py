import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

print("Demonstration of Boolean Retrieval Model using Bitwise operations on Term Document Incidence Matrix of a corpus")

# Corpus / Documents
corpus = {
    'this is the first document.',
    'this document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
}

print("\nThe corpus is:")
print(corpus)

# Creating term-document matrix
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)

# Convert matrix to DataFrame
df = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names_out())
print("\nThis generated DataFrame is:")
print(df)

# Query processing
print("\nQuery processing on the term-document incidence matrix:")

# 1. this AND first
print("\n1. Find all document ids for query: 'this AND first'")
alldata = df[(df['this'] == 1) & (df['first'] == 1)]
print("Document ids where both 'this' and 'first' terms are present:", alldata.index.tolist())

# 2. this OR first
print("\n2. Find all document ids for query: 'this OR first'")
ordata = df[(df['this'] == 1) | (df['first'] == 1)]
print("Document ids where either 'this' or 'first' terms are present:", ordata.index.tolist())

# 3. NOT and
print("\n3. Find all document ids for query: 'NOT and'")
notdata = df[(df['and'] != 1)]
print("Document ids where 'and' term is not present:", notdata.index.tolist())
