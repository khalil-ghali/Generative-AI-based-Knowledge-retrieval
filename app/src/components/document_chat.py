from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from src.utils.embeddings import EmbeddingGenerator
from src.utils.text_processing import TextProcessor

class DocumentChat:
    def __init__(self, file_path):
        self.file_path = file_path
        self.loader = PyPDFLoader(file_path)
        self.embedding = EmbeddingGenerator()
        self.text_processor = TextProcessor()

    def get_index(self):
        documents = self.loader.load()
        texts = self.text_processor.split_text(documents)
        index = VectorstoreIndexCreator(embedding=self.embedding.embedding_model).from_documents(texts)
        return index
