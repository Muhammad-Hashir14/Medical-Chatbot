# 🧠 Medical-Chatbot

This chatbot is powered by the **Gale Encyclopedia of Medicine, Second Edition**. It is designed to answer disease-related questions based on the content of this comprehensive medical reference.

---

## 🧪 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Muhammad-Hashir14/Medical-Chatbot.git
cd Medical-Chatbot
```

## 2. Create a Virtual Environment
```bash 
pip install virtualenv
virtualenv medibot
medibot\Scripts\activate  # For Windows
# OR
source medibot/bin/activate  # For macOS/Linux
```

## 3. Install Dependencies
```bash 
pip install -r requirements.txt
```

## 4. Create a .env File
```bash 
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## 5. Run store_index.py
```
bash python store_index.py
```

## 6. Run the Flask App
```
python app.py
```

## 💻 Tech Stack Used
- Python
- Flask
- Langchain
- Gemini (Google LLM)
- Pinecone (Vector Database)

___
🙋‍♂️ Author:

- Developed by Muhammad Hashir

