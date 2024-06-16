import os
import time
from flask import Flask, render_template, jsonify, request
from langchain.llms import Replicate
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from embed import download_hugging_face_embeddings

app = Flask(__name__)

# Load API key from environment variable
load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
REPLICATE_API_KEY = os.getenv('REPLICATE_API_TOKEN')

#set replicate llm model
llm = Replicate(
    model="a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea",
    config={
        'max_new_tokens': 100,  
        'temperature': 0.7,     
        'top_k': 50             
    }
)

embeddings = download_hugging_face_embeddings()
#check downloaded embeddings
if embeddings is None:
    raise ValueError("No Embeddings Found.")
print(f"Embeddings: {embeddings}")

# Initialize Pinecone
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    try:
        msg = request.form["msg"]
        input_text = msg
        print(f"Received message: {input_text}")

        # Display spinner
        result = {"generated_text": "Thinking..."}

       
        time.sleep(1)

        # Retrieve response from the model
        result = llm.generate([input_text])
        print(f"LLMResult: {result}")

        # Access the generated text from the result object
        if result.generations and result.generations[0]:
            generated_text = result.generations[0][0].text
        else:
            generated_text = "No response generated."

        print(f"Response: {generated_text}")

        return str(generated_text)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)