import streamlit as st
from src.components.document_chat import DocumentChat
from src.components.youtube_chat import YouTubeChat
from src.components.website_chat import WebsiteChat

st.set_page_config(page_title="Generative AI Knowledge Retrieval", layout="wide")
st.title("📚 Generative AI Knowledge Chatbot")

chat_type = st.sidebar.selectbox("Select Chat Type", ["Document", "YouTube", "Website"])

if chat_type == "Document":
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        doc_chat = DocumentChat(file_path)
        index = doc_chat.get_index()

        query = st.text_input("Ask a question about the document:")
        if query:
            response = index.query(query)
            st.write(response)

elif chat_type == "YouTube":
    url = st.text_input("Enter YouTube Video URL:")
    if url:
        yt_chat = YouTubeChat(url)
        index = yt_chat.get_index()

        query = st.text_input("Ask a question about the video:")
        if query:
            response = index.similarity_search(query)
            for i, doc in enumerate(response):
                st.markdown(f"**Answer {i+1}:** {doc.page_content}")

elif chat_type == "Website":
    url = st.text_input("Enter Website URL:")
    if url:
        web_chat = WebsiteChat(url)
        index = web_chat.get_index()

        query = st.text_input("Ask a question about the website content:")
        if query:
            response = index.similarity_search(query)
            for i, doc in enumerate(response):
                st.markdown(f"**Answer {i+1}:** {doc.page_content}")
