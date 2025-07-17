# Medical-Chatbot

This chatbot is powered by the Gale Encyclopedia of Medicine, Second Edition. It is designed to answer disease-related questions based on the content of this comprehensive medical reference.

## 🧪 How to Run Locally

1- Clone the Repo
```bash
https://github.com/Muhammad-Hashir14/Medical-Chatbot.git

2- Create Virtual Enviornment
```bash
pip install virtualenv
virtualenv medibot
medibot\Scripts\activate

3- Install Requirements.txt
```bash
pip install -r requirements.txt

4- Create .env
store Pinecone and Gemini API

PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

5- Run store_index.py
```bash
python store_index.py

6- Run app.py
```bash
python app.py

## Tech Stack Used:
- Python
- Langchain
- Flask
- Gemini
- Pinecone