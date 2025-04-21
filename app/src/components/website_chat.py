import requests
from bs4 import BeautifulSoup

class WebsiteChat:
    def __init__(self, url, llm, embedding_model):
        self.url = url
        self.llm = llm
        self.embedding_model = embedding_model
        self.documents = []

    def load_website_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract text content from the website
            self.documents = [p.get_text() for p in soup.find_all('p')]
        except requests.exceptions.RequestException as e:
            print(f"Error loading website content: {e}")
            self.documents = []

    def process_query(self, query):
        if not self.documents:
            return "No content available to process the query."
        
        # Combine website content into a single string
        content = " ".join(self.documents)
        
        # Generate embeddings for the content and query
        content_embedding = self.embedding_model.embed(content)
        query_embedding = self.embedding_model.embed(query)
        
        # Use the LLM to generate a response based on the query and content
        response = self.llm.generate_response(query_embedding, content_embedding)
        return response

    def get_response(self, query):
        self.load_website_content()
        response = self.process_query(query)
        return response

    def display_sources(self, sources):
        # Logic to display sources of the information
        for source in sources:
            print(f"Source: {source}")