from flask import Flask, render_template, request

app = Flask(__name__)

# Sample documents
documents = {
    1: "This is the first document",
    2: "Flask is a micro web framework",
    3: "Document search engine using Flask",
    # Add more documents as needed
}

# Inverted index
index = {}
for doc_id, content in documents.items():
    words = content.lower().split()
    for word in words:
        if word in index:
            index[word].append(doc_id)
        else:
            index[word] = [doc_id]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query').lower()
    results = set()
    
    if query in index:
        results.update(index[query])
    
    return render_template('result.html', results=results, query=query, documents=documents)

if __name__ == '__main__':
    app.run(debug=True)
