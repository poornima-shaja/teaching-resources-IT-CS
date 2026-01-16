# Practical 4b: Evaluation using Toolkit (Average Precision Score)

from sklearn.metrics import average_precision_score

# Ground truth relevance values
y_true = [0, 1, 1, 0, 1, 1]

# System-generated scores / ranking scores
y_scores = [0.1, 0.4, 0.35, 0.8, 0.65, 0.9]

average_precision = average_precision_score(y_true, y_scores)

print(f"Average precision-recall score: {average_precision}")
