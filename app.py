import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat With PDF", page_icon=":books:") ## Books emoji
    
    st.header("Chat With PDF :books:")
    st.text_input("Ask a question about your document.")
    
    with st.sidebar:
        st.subheader("Your documents")
        pdfs_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner('Processing..'):
                # get pdf text

                
                # get the text chunks
                
                
                # create vector store
        
    
    
if __name__ == '__main__':
    main()