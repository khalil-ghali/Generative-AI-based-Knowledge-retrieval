from langchain.embeddings import HuggingFaceInstructEmbeddings

class EmbeddingGenerator:
    def __init__(self, model_name: str = "hkunlp/instructor-xl"):
        self.model_name = model_name
        self.embedding_model = HuggingFaceInstructEmbeddings(model_name=self.model_name)

    def embed_documents(self, texts):
        return self.embedding_model.embed_documents(texts)

    def embed_query(self, query):
        return self.embedding_model.embed_query(query)
