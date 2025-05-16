# Generative AI Knowledge Retrieval

## Overview

The **Generative AI Knowledge Retrieval** project is a web application designed to use advanced Large Language Models (LLMs) for interacting with various types of text data. Users can upload documents, extract information from YouTube videos, and query websites to obtain precise answers, enhancing their research and learning experiences.

## Project Structure

The project is organized as follows:

```
generative-ai-knowledge-retrieval
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── document_chat.py
│   │   ├── youtube_chat.py
│   │   ├── website_chat.py
│   └── utils
│       ├── __init__.py
│       ├── file_operations.py
│       ├── text_processing.py
│       ├── embeddings.py
│       ├── translation.py
├── .env
├── requirements.txt
└── README.md
```

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd generative-ai-knowledge-retrieval
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys and other configuration settings as needed.

## Usage

To run the application, execute the following command:

```
streamlit run src/app.py
```

This will start the Streamlit server, and you can access the application in your web browser at `http://localhost:8501`.

## Features

- **Document Chat:** Upload PDF documents and interact with them by asking questions.
- **YouTube Chat:** Extract content from YouTube videos and query them for information.
- **Website Chat:** Load website content and ask questions about it.

PS: implement the loading of embedding model of your choice as well as setting env variables for your api keys
## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
