import streamlit as st
from dotenv import load_dotenv

from helper_functions import *

def main():
    # Loading the api key from env folder
    load_dotenv()
    st.set_page_config("Chat with Multiple PDFs")
    
    # Header of the Page.
    st.header("Chat with PDF :books:")
    
    # Taking the question of the user.
    user_question = st.text_input("Ask a Question from the PDF Files")
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
        
    if user_question:
        user_input(user_question)
        
    # Upload you pdf files.
    with st.sidebar:
        st.subheader("Upload your Documents")
        pdf_docs = st.file_uploader("Upload your PDF and Click on the Process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)
                st.success("Done")



if __name__ == "__main__":
    main()
         
            