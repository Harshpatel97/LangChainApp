# LangChainApp

# How to run?
### STEPS:
 
Clone the repository

```bash
https://github.com/Harshpatel97/LangChainApp.git
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


