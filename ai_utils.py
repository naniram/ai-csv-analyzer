from langchain.docstore.document import Document
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

def create_documents(insight_texts):
    return [Document(page_content=text) for text in insight_texts]

def create_vector_db(documents, embedding_model):
    embeddings = OllamaEmbeddings(model=embedding_model)
    return FAISS.from_documents(documents, embeddings)

def setup_qa_chain(db, model_name):
    retriever = db.as_retriever(search_kwargs={"k": 5})
    llm = Ollama(model=model_name)
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
