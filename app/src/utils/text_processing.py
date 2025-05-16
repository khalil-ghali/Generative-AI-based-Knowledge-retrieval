from langchain.text_splitter import CharacterTextSplitter

class TextProcessor:
    def __init__(self, chunk_size=1000, chunk_overlap=100):
        self.splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def split_text(self, documents):
        return self.splitter.split_documents(documents)
