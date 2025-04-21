from streamlit import st
from components.document_chat import DocumentChat
from components.youtube_chat import YouTubeChat
from components.website_chat import WebsiteChat

def main():
    st.title("TextGenius: Your Favorite Chat Buddy 📄🤖")
    
    page_names_to_funcs = {
        "Chat with Documents": DocumentChat,
        "Chat with YouTube Videos": YouTubeChat,
        "Chat with a Website": WebsiteChat,
    }

    demo_name = st.sidebar.selectbox("Please choose your tool 😊", page_names_to_funcs.keys())
    page = page_names_to_funcs[demo_name]()
    page.run()

if __name__ == "__main__":
    main()