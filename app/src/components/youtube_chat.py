import requests
from urllib.parse import urlparse, parse_qs

class YouTubeChat:
    def __init__(self, api_key, llm, embedding_model):
        self.api_key = api_key
        self.llm = llm
        self.embedding_model = embedding_model
        self.transcript = ""

    def extract_video_id(self, youtube_url):
        try:
            parsed_url = urlparse(youtube_url)
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get('v', [None])[0]
            return video_id
        except Exception as e:
            print(f"Error extracting video ID: {e}")
            return None

    def load_video_content(self, video_id):
        try:
            # Use YouTube API to fetch video transcript
            url = f"https://www.googleapis.com/youtube/v3/captions?videoId={video_id}&key={self.api_key}"
            response = requests.get(url)
            response.raise_for_status()
            captions_data = response.json()

            # Assuming the transcript is available in the captions data
            self.transcript = " ".join([caption['text'] for caption in captions_data.get('items', [])])
        except requests.exceptions.RequestException as e:
            print(f"Error loading video content: {e}")
            self.transcript = ""

    def answer_question(self, question):
        if not self.transcript:
            return "No transcript available to answer the question."
        
        # Generate embeddings for the transcript and question
        transcript_embedding = self.embedding_model.embed(self.transcript)
        question_embedding = self.embedding_model.embed(question)
        
        # Use the LLM to generate a response based on the question and transcript
        response = self.llm.generate_response(question_embedding, transcript_embedding)
        return response

    def chat_with_video(self, youtube_url, question):
        video_id = self.extract_video_id(youtube_url)
        if video_id:
            self.load_video_content(video_id)
            return self.answer_question(question)
        else:
            return "Invalid YouTube URL."