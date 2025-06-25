from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def load_chatbot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    llm = Ollama(model="deepseek-r1", temperature=0.3)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
    return qa_chain

if __name__ == "__main__":
    chatbot = load_chatbot()
    while True:
        query = input("Ask about startups: ")
        if query.lower() in ['exit', 'quit']: break
        answer = chatbot.run(query)
        print(f"\n🧠 {answer}\n")
