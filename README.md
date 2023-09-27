# LangChainApp
LANGCHAIN is a powerful tool designed to streamline the process of extracting information from PDF documents through natural language interactions. This project leverages the Langchain library and integrates Google's PaLM (Language Model) to enable seamless interactions with PDF files. It also provides a user-friendly interface developed using Streamlit for easy access and utilization.

## Features
### Natural Language Interaction
You can ask questions or request specific information, and the integrated Google PaLM model will provide relevant answers based on the content of the PDF.

### PDF Information Retrieval
You can quickly find specific information within PDF documents without the need to manually search through lengthy files. Whether you need to extract data, quotes, statistics, or any other content, LANGCHAIN can assist you efficiently.

### Streamlit Interface
The user interface is designed with Streamlit, a popular Python library for creating web applications with minimal effort. The Streamlit interface ensures a smooth and intuitive user experience, making it accessible to users of all technical backgrounds.


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

# Finally run the following command
```bash
streamlit run app.py
```
### Now you can chat with you pdfs


