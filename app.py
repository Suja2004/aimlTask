import os
import nltk
from flask import Flask, render_template, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  

nltk.data.path.append(os.path.join(os.path.dirname(__file__), 'nltk_data'))

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    raise Exception("NLTK punkt data not found. Please ensure it's included in the project.")

def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return ' '.join(str(sentence) for sentence in summary)

@app.route('/')
def index():
    return render_template('index.html')

logging.basicConfig(level=logging.DEBUG)

@app.route('/summarize', methods=['POST'])
def summarize_route():
    logging.debug("Received request: %s", request.json)
    try:
        data = request.json
        text = data['text']
        sentence_count = int(data['sentence_count'])
        summary = summarize_text(text, sentence_count)
        logging.debug("Generated summary: %s", summary)
        return jsonify({'summary': summary})
    except Exception as e:
        logging.error("Error occurred: %s", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
