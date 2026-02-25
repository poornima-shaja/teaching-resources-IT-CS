import re
from collections import defaultdict

class DocumentRetrievalSystem:
    def __init__(self):
        self.index = defaultdict(set)
        self.documents = {}

    def tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

    def index_document(self, doc_id, text):
        tokens = self.tokenize(text)
        for token in tokens:
            self.index[token].add(doc_id)
        self.documents[doc_id] = text

    def retrieve_documents(self, query):
        tokens = self.tokenize(query)
        relevant_doc_ids = set()

        for token in tokens:
            if token in self.index:
                if not relevant_doc_ids:
                    relevant_doc_ids.update(self.index[token])
                else:
                    relevant_doc_ids.intersection_update(self.index[token])

        return [(doc_id, self.documents[doc_id]) for doc_id in relevant_doc_ids]

# Example usage
doc_retrieval = DocumentRetrievalSystem()
doc_retrieval.index_document(1, "This is the first Document")
doc_retrieval.index_document(2, "This is the second Document")
doc_retrieval.index_document(3, "Another document is here")

query = input("Enter your query: ")
results = doc_retrieval.retrieve_documents(query)

print("Query:", query)
for doc_id, text in results:
    print(f"Document {doc_id}: {text}")
