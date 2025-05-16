import requests
from bs4 import BeautifulSoup
from langchain.schema import Document
from langchain.vectorstores import FAISS
from src.utils.embeddings import EmbeddingGenerator
from src.utils.text_processing import TextProcessor

class WebsiteChat:
    def __init__(self, url):
        self.url = url
        self.embedding = EmbeddingGenerator()
        self.text_processor = TextProcessor()

    def _get_visible_text(self):
        response = requests.get(self.url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script", "style", "header", "footer", "nav", "aside"]):
            script.decompose()

        visible_text = " ".join(soup.stripped_strings)
        return visible_text

    def get_index(self):
        text = self._get_visible_text()
        documents = [Document(page_content=text)]
        texts = self.text_processor.split_text(documents)
        return FAISS.from_documents(texts, self.embedding.embedding_model)
# 