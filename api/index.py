from flask import Flask, request
from sentence_transformers import SentenceTransformer
import faiss
import os
from utils import clean_line
import pickle

app = Flask(__name__)

# establish cache dir
cache_dir = './cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

# load dataset and cache it
passages = []
with open('dataset.txt', 'r') as file:
    for line in file.readlines():
        passages.extend(clean_line(line))

# initialize the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# load dense vectors
dense_vectors_path = os.path.join(cache_dir, 'dense_vectors.pkl')
faiss_index_path = os.path.join(cache_dir, 'faiss.index')

if os.path.exists(dense_vectors_path):
    with open(dense_vectors_path, 'rb') as file:
        embeddings = pickle.load(file)
else:
    embeddings = model.encode(passages)
    with open(dense_vectors_path, 'wb') as file:
        pickle.dump(embeddings, file)

# load faiss index
if os.path.exists(faiss_index_path):
    index = faiss.read_index(faiss_index_path)
else:
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, faiss_index_path)

print('Indexing complete')

def search(query, passages, k=10):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    results = []
    for i in range(k):
        results.append({
            'passage': passages[indices[0][i]],
            'distance': float(distances[0][i])
        })
    return results

@app.route("/api/query", methods=["GET"])
def query():
    try:
        query = request.args.get('query')
        results_df = search(query, passages, 10)
        return {
            'success': True,
            'results': results_df
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e)
        }

if __name__ == '__main__':
    app.run(debug=True)