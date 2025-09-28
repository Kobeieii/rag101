from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from helpers.database import get_connection, insert_document, fetch_similar_documents
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# 1. Load PDF
loader = PyPDFLoader("documents/resume.pdf")
docs = loader.load()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 3. Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")

# 4. Connect to PostgreSQL and insert chunks
with get_connection() as conn:
    for chunk in chunks:
        embedding = embeddings.embed_query(chunk.page_content)
        insert_document(chunk.page_content, embedding, conn)
logging.info("All documents have been inserted into the database.")

question = "Who is Thitiworada Khumpeng?"
query_embedding = embeddings.embed_query(question)

results = []
# 5. Fetch similar documents
with get_connection() as conn:
    similar_docs = fetch_similar_documents(query_embedding, 5, conn)
    results = [content for content, _ in similar_docs]
logging.info(f"Retrieved {len(results)} similar documents.")

# 6. Use retrieved documents to answer the question
# llm = ChatOllama(model="llama3.2")
llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that helps people find information."),
    ("user", "Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\n{context}"),
    ("user", "Question: {question}")
])

chain = prompt_template | llm
response = chain.invoke({
    "context": "\n\n".join(results),
    "question": question
})
logging.info(f"Response: {response.content}")