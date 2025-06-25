import json
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_reddit_data(file_path="reddit_data.json"):
    with open(file_path, "r") as f:
        raw = json.load(f)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = []
    for entry in raw:
        combined = f"{entry['title']}\n\n{entry['selftext']}\n\n" + "\n".join(entry['comments'])
        docs.extend(text_splitter.split_text(combined))
    return docs