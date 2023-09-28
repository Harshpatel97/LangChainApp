from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import GooglePalm
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

import streamlit as st

load_dotenv()

def get_pdf_text(pdf_docs):
    """
    Loading the pdf and converting them into texts.
    """
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

def get_text_chunks(text):
    
    """
    Getting the texts and converting into chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    """
    Storing the embeddings and text chunks into vector store.
    """
    embeddings = GooglePalmEmbeddings()
    vector_store = FAISS.from_texts(text_chunks,
                                    embedding=embeddings)
    return vector_store

def get_conversational_chain(vector_store):
    """
    Using PaLM model for having conversations with pdf file.
    """
    llm = GooglePalm()
    memory = ConversationBufferMemory(memory_key='chat_history',
                                      return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm,
                                                               retriever=vector_store.as_retriever(),
                                                               memory=memory)
    return conversation_chain

def user_input(user_question):
    """
    Taking the user input and showing messages.
    """
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write(":boy:   ", message.content)
        else:
            st.write(":robot_face:  ", message.content)
            