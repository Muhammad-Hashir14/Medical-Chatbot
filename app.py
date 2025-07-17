from flask import Flask, jsonify, request, session
from src.helper import textsplitter, download_HF_Embeddings, load_documents
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from flask import render_template
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from src.prompt import system_prompt


load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

index_name = "medicalbot"
embeddings = download_HF_Embeddings()

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.4,
    max_tokens=1000,
    timeout=None,
    max_retries=2,
    # other params...
)

retriever = docsearch.as_retriever(search_type = "similarity", search_keargs = {"k":3})

prompt = ChatPromptTemplate(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]
    )

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

app = Flask(__name__)
app.secret_key = SECRET_KEY  # Required for session

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods = ['GET', "POST"])
def chat():

   if "history" not in session:
       session["history"] = []
   message = request.form["msg"]
   input = message
   message = request.form.get("msg", "").strip()

   if not message:
        return render_template("chat.html", user_message="", bot_answer="⚠️ Please enter a message.")

   print("\nUser input:", message)  # 🔥 This will now print
   response = rag_chain.invoke({"input":message})
   answer = response["answer"]
   print(answer)
   session["history"].append({"user":message, "bot":answer})
   session.modified = True
   return render_template("chat.html", chat_history=session.get("history", []))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



