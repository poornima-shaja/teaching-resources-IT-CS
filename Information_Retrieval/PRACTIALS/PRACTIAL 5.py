# Practical-5: Text Categorization using Naive Bayes
# Program: 5(a)

import numpy as np
import re

class NaiveBayesClassifier:
    def __init__(self):
        self.vocab = []
        self.positive_counts = None
        self.negative_counts = None
        self.positive_prior = 0.0
        self.negative_prior = 0.0

    # Step 1: Preprocess text (tokenization + lowercase)
    def preprocess_review(self, review):
        tokens = re.findall(r"\b\w+\b", review.lower())
        return tokens

    # Step 2: Convert text into a vector (Bag of Words)
    def vectorize_review(self, tokens):
        vector = np.zeros(len(self.vocab))
        for word in tokens:
            if word in self.vocab:
                vector[self.vocab.index(word)] += 1
        return vector

    # Step 3: Train the classifier
    def train(self, X_train, y_train):
        # Build vocabulary
        for review in X_train:
            tokens = self.preprocess_review(review)
            self.vocab.extend(tokens)
        self.vocab = list(set(self.vocab))

        # Initialize word counts
        self.positive_counts = np.zeros(len(self.vocab))
        self.negative_counts = np.zeros(len(self.vocab))

        # Vectorize training data
        X_train_vectorized = [
            self.vectorize_review(self.preprocess_review(review))
            for review in X_train
        ]

        positive_count = 0

        # Count word frequencies per class
        for i in range(len(X_train_vectorized)):
            if y_train[i] == 'positive':
                self.positive_counts += X_train_vectorized[i]
                positive_count += 1
            else:
                self.negative_counts += X_train_vectorized[i]

        # Calculate priors
        self.positive_prior = positive_count / len(y_train)
        self.negative_prior = 1 - self.positive_prior

    # Step 4: Predict class for test data
    def predict(self, X_test):
        predictions = []
        for review in X_test:
            review_vectorized = self.vectorize_review(
                self.preprocess_review(review)
            )

            # Likelihood calculation
            positive_likelihood = np.prod(
                (self.positive_counts / sum(self.positive_counts)) ** review_vectorized
            ) * self.positive_prior

            negative_likelihood = np.prod(
                (self.negative_counts / sum(self.negative_counts)) ** review_vectorized
            ) * self.negative_prior

            if positive_likelihood > negative_likelihood:
                predictions.append('positive')
            else:
                predictions.append('negative')
        return predictions


# ------------------- Training Data -------------------
positive_reviews = [
    "The movie was amazing, I like great acting and an engaging plot."
]

negative_reviews = [
    "Terrible! Would not recommend it to anyone."
]

X_train = positive_reviews + negative_reviews
y_train = ['positive'] * len(positive_reviews) + ['negative'] * len(negative_reviews)

# ------------------- Testing Data -------------------
X_test = [
    "The acting was superb!"
]

y_test = ['positive']

# ------------------- Model Execution -------------------
classifier = NaiveBayesClassifier()
classifier.train(X_train, y_train)

predictions = classifier.predict(X_test)
print("Predicted class for the new review:", predictions[0])

accuracy = sum(
    1 for true_label, predicted_label in zip(y_test, predictions)
    if true_label == predicted_label
) / len(y_test)

print("Accuracy:", accuracy)
