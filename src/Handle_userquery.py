from langchain.chains import create_retrieval_chain
from langchain_community.chat_models.huggingface import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create the conversational QA chain using history-aware retriever
def RAG_conversation_chain(vector_store):
    llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation",
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    repetition_penalty=1.03,
)
    
    retriever = vector_store.as_retriever()
    
    system_prompt = (
    "You are an intelligent and helpful assistant tasked with answering user queries based on the following retrieved context. "
    "If the context provides the answer, respond clearly and concisely. If the context does not cover the question, "
    "admit that you don't know the answer, but offer suggestions for where the user might find the information. "
    "Ensure that your responses are informative, polite, and relevant to the user's query. Be mindful of avoiding unnecessary details."
    "\n\n"
    "Context: {context}\n\n"
    "Answer the user's query based on the provided context."
    )

    
    prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
    )
    
    # Create the retrieval chain for Conversational QA
    qa_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt
    )
    rag_chain = create_retrieval_chain(retriever, qa_chain)
    return rag_chain

# Handle user query and manage chat history
def get_response(user_query: str, session_vector_store=None):
    
    # Build the RAG conversation chain with history
    conversation_rag_chain = RAG_conversation_chain(session_vector_store)
    
    # Process the user query
    response = conversation_rag_chain.invoke({
        "input": user_query
    })
    
    return response.get("answer", "Sorry, I couldn't find an answer to your question.").replace('Assistant:','').replace('assistant:','')

