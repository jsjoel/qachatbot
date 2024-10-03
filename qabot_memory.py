import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub
from langchain.memory import ConversationBufferMemory
import streamlit as st
# Set environment variable 
os.environ['HUGGINGFACE_API_TOKEN'] ='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'


# Streamlit title for web application
st.title("QA Chatbot")


# Load the document using TextLoader
loader = TextLoader("D:/vs/chatbot/unseen_pasage.txt")
raw_documents = loader.load()
# Splitting into smaller chunks for beter processing
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
#Initialize the embedding model
embeddingmodel = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#Create vector store from documents and embedding model
vectorstore    = FAISS.from_documents(documents, embeddingmodel)
#Function to retrieve relevant document
def retreive_relevant_document(question):
    return vectorstore.similarity_search(question)


# Display the entire document content
st.subheader("Document Content:")
document_content = "\n".join([doc.page_content for doc in raw_documents])
# st.text_area("Scroll through the document content:", value=document_content, height=300, disabled=True)
st.markdown(
    f'<div style="height: 300px; overflow-y: scroll; color: white; background-color: black; padding: 10px;">{document_content}</div>',
    unsafe_allow_html=True
)


#User input for asking question
question = st.text_input("Please ask your question!!")


#template for tje model
prompt_template = """
You are a knowledgeable assistant who provides accurate and concise answers to questions based on the given context. Your goal is to assist users by clearly addressing their inquiries without unnecessary elaboration.

### Instructions:
1. **Read the Context Carefully**: Understand the information provided in the context before answering the question.
2. **Provide a Concise Answer**: Your answer should directly respond to the question, incorporating relevant information from the context.
3. **Clarify When Necessary**: If the question is unclear or cannot be answered based on the context, ask for clarification or provide the best possible alternatives.
---
## Example 1:

Context: "Deep within the heart of the Amazon rainforest, hidden beneath a dense canopy of ancient trees, lay a forgotten temple."
Question: What is the primary setting of the story?
Answer: The story is set deep within the Amazon rainforest, where a forgotten temple is hidden beneath the dense canopy of ancient trees.

---

**Context:** {context}

**Question:** {question}

---

**Answer(in English):**
"""
qa_prompt= PromptTemplate(template=prompt_template, input_variables=["context", "question"])


#memory 
qa_memory = ConversationBufferMemory(input_key='question', memory_key='chat_history')

# Initialize the llm using huggingfacehub
llm = HuggingFaceHub(repo_id= "google/flan-t5-small", model_kwargs= {"temperature":0.9, "max_length":512}, huggingfacehub_api_token = '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')
#Create a chain to handle question answering  usinf llm and prompt
qa_chain = LLMChain(llm=llm, prompt= qa_prompt, verbose=True, output_key='answer', memory=qa_memory )

if question:
    #retrieve the relevant documents based on user's question
    relevant_docs = retreive_relevant_document(question)    
    context = "\n".join([relevant_docs[0].page_content])
    
    try:
        answer = qa_chain.run(context=context, question =question)

    except Exception as e:
        st.write(f"Error: {e}")
    

    st.write("Answer:")
    st.write(answer)

    with st.expander('Question History'):
        st.info(qa_memory.buffer)


