# Super Context Chat

## Summary

You're developing an advanced chatbot leveraging LangChain and the ChatGPT API to enable users to interact with and query information across multiple PDFs. The chatbot is designed to handle complex queries and provide accurate responses by analyzing the content of the PDFs. In addition to its PDF querying capabilities, the chatbot includes several advanced AI features that enhance its functionality and user experience.

## How It Works
------------

![MultiPDF Chat App Diagram](./docs/PDF-LangChain.jpg)

The application follows these steps to provide responses to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## List of Features

1. **Multi-PDF Querying**:
   - Ability to upload and manage multiple PDF documents.
   - Efficient indexing of PDFs to facilitate quick and accurate searches.
   - Natural language understanding to interpret user queries and extract relevant information from PDFs.

2. **Advanced Natural Language Processing (NLP)**:
   - Utilizes the latest advancements in NLP to understand and process user queries.
   - Supports context-aware querying, allowing for follow-up questions and maintaining conversation context.
   - Handles complex queries involving multiple layers of information extraction.

3. **Document Summarization**:
   - Generates concise summaries of lengthy PDF documents.
   - Provides section-wise summaries to give users an overview of specific parts of a document.

4. **Contextual Analysis**:
   - Analyzes the context of queries to provide more relevant and precise answers.
   - Capable of understanding and resolving ambiguous questions by considering the context within the PDFs.

5. **Integration with LangChain**:
   - Utilizes LangChain to manage and manipulate document chains.
   - Supports complex workflows and interactions between different documents.

6. **User-Friendly Interface**:
   - Intuitive and easy-to-use interface for uploading and managing PDFs.
   - Chat-based interaction model for querying documents and receiving responses.

7. **AI-Powered Insights**:
   - Provides insights and analyses based on the content of the PDFs.
   - Capable of generating reports and visualizations from document data.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)
- LangChain library
- OpenAI API key

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/shashankyadav03/super-context-chat.git
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   ```sh
   export OPENAI_API_KEY='your-openai-api-key'  # On Windows, use `set OPENAI_API_KEY=your-openai-api-key`
   ```

### Usage

1. Run the application:
   ```sh
   streamlit run app.py
   ```

2. Access the application in your browser at `http://localhost:5000`.

### Contributing

We welcome contributions to improve Super Context Chat! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://openai.com)
