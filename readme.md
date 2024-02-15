# GEN-AI Final Assignment

## Objective: Building a PDF question-and-answer application with LangChain, Google PaLM 2, and Chroma Vector Database.

### Project Structure:
main.py: Main script that need to be executed.
ai_models.py: Handles loading and managing the large language model (LLM) and embedding models.
mychromadb.py: Implements functionalities for interacting with the Chroma Vector Database.
myapi.py: Defines the FastAPI endpoints for the application.

### Installation:
Create a virtual environment and activate it.
Install the dependencies: pip install -r requirements.txt
Update the api_key variable in ai_models.py with your Google PaLM 2 API key.

### Usage:
Run the application: python main.py
Access the API documentation at: http://127.0.0.1:8000/docs

### API Endpoints:
/upload/{pdf_path}/{pdf_name}: Takes a pdf_path and pdf_name, then uploads that specific pdf to chromadb.
/answers/{pdf_name}/{question}: Takes a question and pdf_name, then retrieves related segments from chromadb and passes that to palm2 api and returns answer of the question.

### Technologies Used:
LangChain: An NLP library for building complex language pipelines.
Google PaLM 2: A powerful large language model for text generation and understanding.
Chroma Vector Database: A semantic search engine based on word embeddings.
FastAPI: A web framework for building APIs in Python.

### Resources followed:
for palmapi : https://www.youtube.com/watch?v=R6WNU28MgQ0, https://ai.google.dev/models/palm, https://ai.google.dev/palm_docs/, 

for langchain : langchain docs, https://www.youtube.com/playlist?list=PL8motc6AQftn-X1HkaGG9KjmKtWImCKJS

for chromadb: https://docs.trychroma.com/, https://python.langchain.com/docs/integrations/vectorstores/chroma, https://www.youtube.com/watch?v=3yPBVii7Ct0&t=11s