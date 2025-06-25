from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from data_loader import load_reddit_data

def create_vector_store():
    docs = load_reddit_data()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_texts(docs, embedding=embeddings, persist_directory="chroma_db")
    vectorstore.persist()

if __name__ == "__main__":
    create_vector_store()