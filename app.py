import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS 
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from htmlTemplates import bot_template, user_template, css
from langchain_community.llms import HuggingFaceHub

def get_text_from_pdf(pdf_docs):
    raw_text = ""
    for pdf_doc in pdf_docs:
        pdf_reader = PdfReader(pdf_doc)
        for page in pdf_reader.pages:
            raw_text += page.extract_text()
    return raw_text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_splitter.split_text(raw_text)
    return text_chunks

def get_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(embedding = embeddings, texts = text_chunks)
    return vector_store

def get_conversation_chain(vector_store):
    llm = ChatOpenAI()
    # llm =  HuggingFaceHub(repo_id="EleutherAI/gpt-neo-2.7B",model_kwargs={"max_length": 512, "temperature": 0.7})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm = llm, retriever = vector_store.as_retriever(), memory = memory)
    return conversation_chain

def handler_user_query(user_query):
    response = st.session_state.conversation_chain({'question': user_query})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Super Context Chatbot", page_icon="🤖")

    # Load CSS
    st.write(css, unsafe_allow_html=True)

    if 'conversation_chain' not in st.session_state:
        st.session_state.conversation_chain = None
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = None

    st.header("Super Context Chatbot 🤖")
    
    user_query = st.text_input("Chat with the chatbot below:")
    if user_query:
        handler_user_query(user_query)

    st.write(user_template.replace("{{MSG}}", "Hello! Human"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello! Robot"), unsafe_allow_html=True)
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your documents here",accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing..."):
                # get text from pdf
                raw_text = get_text_from_pdf(pdf_docs)
                
                # get text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector embeddings
                vector_store = get_vector_store(text_chunks)
                st.success("Processing complete!")

                # conversation chain
                st.session_state.conversation_chain = get_conversation_chain(vector_store)
        
    




if __name__ == '__main__':
    main()