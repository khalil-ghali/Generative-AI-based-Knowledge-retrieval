from youtube_transcript_api import YouTubeTranscriptApi
from langchain.vectorstores import FAISS
from langchain.schema import Document
from src.utils.embeddings import EmbeddingGenerator
from src.utils.text_processing import TextProcessor

class YouTubeChat:
    def __init__(self, video_url):
        self.video_url = video_url
        self.embedding = EmbeddingGenerator()
        self.text_processor = TextProcessor()

    def _extract_video_id(self):
        return self.video_url.split("v=")[-1]

    def get_index(self):
        video_id = self._extract_video_id()
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([t["text"] for t in transcript])
        documents = [Document(page_content=transcript_text)]
        texts = self.text_processor.split_text(documents)
        return FAISS.from_documents(texts, self.embedding.embedding_model)
