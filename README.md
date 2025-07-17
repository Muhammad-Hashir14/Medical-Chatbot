# 🧠 Medical-Chatbot

This chatbot is powered by the **Gale Encyclopedia of Medicine, Second Edition**. It is designed to answer disease-related questions based on the content of this comprehensive medical reference.

---

## 🧪 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Muhammad-Hashir14/Medical-Chatbot.git
cd Medical-Chatbot
2. Create a Virtual Environment
bash
Copy
Edit
pip install virtualenv
virtualenv medibot
medibot\Scripts\activate  # For Windows
# OR
source medibot/bin/activate  # For macOS/Linux
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Create a .env File
Create a .env file in the project root and add your API keys:

env
Copy
Edit
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
5. Run store_index.py
bash
Copy
Edit
python store_index.py
6. Run the Flask App
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000 in your browser to interact with the chatbot.

💻 Tech Stack Used
Python

Flask

Langchain

Gemini (Google LLM)