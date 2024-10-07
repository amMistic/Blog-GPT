import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from src.Process_URL import Process
from src.Handle_userquery import get_response

# app config
st.set_page_config(page_title="BlogGPT", page_icon="🤖")

# set the header to the website
st.markdown('# Ask me anything🤖')

# Initialized all session state variables
if 'visible' not in st.session_state:
    st.session_state.visible = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content='Hi! I am BlogGPT. Your Personal Blog Assistant. How can I assist you today?')
    ]
if 'url' not in st.session_state:
    st.session_state.url = None

# allow user to first drop the website url to chat 
with st.sidebar:
    st.markdown('# BlogGPT [o _ o]')
    url = st.text_input('URL')
    
    if url:
        st.session_state.url = url
        if 'vector_store' not in st.session_state:
            if st.button('Process'):
                st.session_state.visible = True
                with st.spinner('Processing Website...'):
                    st.session_state.vector_store = Process().get_vector_store(url)

# Chat area
if st.session_state.visible:
    
    # take the query from the user 
    user_query = st.chat_input('Drop your query here')
    
    if user_query:
        if user_query == 'exit':
            exit()
        response = get_response(user_query, st.session_state.vector_store)
        
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

        # Optionally clear the input field after sending the message
        user_query = ''
    
        # Display chat messages
        for message in st.session_state.chat_history:
            if isinstance(message, AIMessage):
                with st.chat_message("AI"):
                    st.write(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message("Human"):
                    st.write(message.content)

