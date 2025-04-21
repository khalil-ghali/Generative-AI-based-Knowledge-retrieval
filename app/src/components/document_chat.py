class DocumentChat:
    def __init__(self, api_key):
        self.api_key = api_key
        self.documents = []
        self.llm = self.initialize_llm()

    def initialize_llm(self):
        from langchain_openai import OpenAI
        return OpenAI(api_key=self.api_key)

    def upload_documents(self, uploaded_files):
        import os
        from utils.file_operations import save_uploaded_files

        pdfs_directory = "PDFs"
        if not os.path.exists(pdfs_directory):
            os.makedirs(pdfs_directory)

        save_uploaded_files(uploaded_files, pdfs_directory)

    def process_question(self, question):
        from langchain.chains import RetrievalQA
        from langchain.vectorstores import Chroma
        from langchain.document_loaders import DirectoryLoader
        from langchain.text_splitter import RecursiveCharacterTextSplitter

        loader = DirectoryLoader('./PDFs', glob="./*.pdf")
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
        texts = text_splitter.split_documents(documents)

        vectordb = Chroma.from_documents(documents=texts, embedding=self.llm)
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})

        qa_chain = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
        response = qa_chain(question)

        return response

    def generate_response(self, question):
        response = self.process_question(question)
        return response['result'], response['source_documents']