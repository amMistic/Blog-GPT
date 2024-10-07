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
        repo_id="HuggingFaceH4/zephyr-7b-beta",  # Zephyr 7B model
        task="text-generation",                  
        max_new_tokens=512,                      
        do_sample=True,                          
        temperature=0.7,                         
        repetition_penalty=1.03,  
        stop=["\n"]
    )
    
    retriever = vector_store.as_retriever()
    
    system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know."
    "\n\n"
    "{context}"
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
    
    print('The response',response)
    copy_response = [response['answer'].split(' ')]
    start = 0, end = len(copy_response)
    for ind, word in enumerate(copy_response):
        if word == 'Assistant:':
            start = ind
        if word == 'human':
            end = ind 
            break
    
    final_response = copy_response[start:end]
    # Return the response or a fallback answer
    
    return str(final_response)
    # return response.get("answer", "Sorry, I couldn't find an answer to your question.")

