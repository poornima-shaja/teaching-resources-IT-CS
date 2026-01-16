# Practical 4a: Evaluation Metrics (Precision, Recall, F-measure)

def calculate_metrics(retrieved_set, relevant_set):
    true_positive = len(retrieved_set.intersection(relevant_set))
    false_positive = len(retrieved_set.difference(relevant_set))
    false_negative = len(relevant_set.difference(retrieved_set))

    print("True Positive:", true_positive)
    print("False Positive:", false_positive)
    print("False Negative:", false_negative)

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    f_measure = (2 * precision * recall) / (precision + recall)

    return precision, recall, f_measure


# Example sets
retrieved_set = set(["doc1", "doc2", "doc3"])
relevant_set = set(["doc1", "doc4"])

precision, recall, f_measure = calculate_metrics(retrieved_set, relevant_set)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F-measure: {f_measure}")
