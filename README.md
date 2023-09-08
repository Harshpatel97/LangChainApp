# LangChainApp
The Langchain PDF Chatbot is an open-source application designed to enable natural language interactions with personal PDF documents. It leverages the power of natural language processing (NLP) and machine learning to extract, understand, and provide information from PDF files through a chat interface.

## Features
1. Load PDF documents from a specified directory.
2. Split text from PDFs into chunks for efficient processing.
3. Convert text chunks into embeddings for similarity-based retrieval.
4. Utilize Pre-trained Hugging Face embeddings model.
5. Perform Retrieval-based question-answering using a Language Model(LLM).
6. Command-line interface for user interaction.
7. Exit the chatbot by typing 'exit'.

# How to run?
### STEPS:
 
Clone the repository

```bash
git clone https://github.com/Harshpatel97/LangChainApp.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create --name langchain python=3.9 -y
```

```bash
conda activate langchain
```
### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 3- Create a models folder and download Quantised version of Llama 2 which can run on CPU and save it into models folder
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin

### STEP 4- You can add your PDF files into Data folder 
```bash
# Finally run the following command
python app.py
```
### Now you can chat with you pdfs


