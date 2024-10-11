# Your Personal Blog Assistant – BlogGPT 🤖 !

<img src="https://github.com/user-attachments/assets/8476cc59-b74a-44bb-8a09-e6e9b7ba14cf" alt="example image" height=500 width="350"/>

### 🚀 **Overview**
BlogGPT is an AI-powered app that answers your questions by processing and analyzing blog content from any URL. With a simple interface and intelligent backend, it delivers accurate responses based on the content it retrieves.

### 💡 **Key Features**
- **Conversational QA**: Chat with BlogGPT about any blog's content.
- **Automated Content Processing**: Fetches, splits, and stores blog data for efficient querying.
- **Real-time Interaction**: Instant responses powered by advanced language models.
- **Easy-to-Use Interface**: Streamlit-based for seamless user experience.

### 🛠️ **How It Works**
<img src="https://github.com/user-attachments/assets/970537fc-23d0-418e-bae8-caff8bf37d1c" alt="image description" width="600" height="500">

BlogGPT enables users to query website content by following these steps:

1. **Content Extraction:** The user provides a URL, and the tool fetches the website’s text.
2. **Text Chunking:** The content is split into smaller sections for better processing.
3. **Embedding Creation:** Each chunk is converted into numerical vectors (embeddings) using the HuggingFaceEmbeddings model.
4. **Vector Store:** The embeddings are stored in a Chroma Vector Store for fast retrieval.
5. **Query & Response:** User queries are matched to relevant chunks via semantic search, and answers are generated using the Zephyr 7B language model.
---

### 🏗️ **Tech Stack**
- **Streamlit**: Front-end interface.
- **LangChain**: Backend logic for retrieval-augmented generation (RAG).
- **Hugging Face**: Utilizes `zephyr-7b` model for language generation.
- **Chroma**: Vector store for document retrieval.
- **Sentence Transformers**: For creating embeddings.

---

### 📦 **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/amMistic/Blog-GPT.git
   cd Blog-GPT
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Hugging Face API credentials.

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

### 📚 **Usage**

1. **Run the App**: Start BlogGPT through Streamlit.
2. **Enter URL**: Provide a blog URL.
3. **Ask Questions**: Engage with BlogGPT to get insights about the blog content.

---

### 🔧 **Future Enhancements**
- Support for additional document formats (PDF, text).
- Enhanced multi-turn conversations.
- Improved UI for smoother experience.

---
