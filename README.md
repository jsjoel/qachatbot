# QA Chatbot

This project implements a Question-Answering (QA) Chatbot using LangChain and Streamlit. It allows users to ask questions related to a specified text document, providing concise and accurate answers based on the content.

## Features

- Load and display document content.
- Interactive question-and-answer functionality.
- Memory to track conversation history.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jsjoel/qachatbot.git
   cd qachatbot
   ```
2. Install necessary libraries
   ```bash
   pip install transformers torch langchain langchain-community streamlit
   ```
   Additional libraries
   ```bash
   pip install torch torchvision torchaudio
   ```
### Explanation of Packages
- **langchain**: A framework for developing applications using language models.

- **langchain-community**: A community-driven extension of the LangChain library that provides additional tools and features.

- **streamlit**: A library for creating interactive web applications using Python.

- **transformers**: A library by Hugging Face that provides pre-trained models for Natural Language Processing (NLP) tasks, including language modeling and text classification.

- **torch**: The core library for PyTorch, a popular framework for deep learning.

##Sample Images

   ![The web application preview](https://github.com/jsjoel/qachatbot/blob/main/assets/Screenshot%202024-10-03%20224252.png)

   
   ![Web application preview](https://github.com/jsjoel/qachatbot/blob/main/assets/Screenshot%202024-10-03%20232359.png)


   
   

### Run
1. Run the Streamlit application in terminal using :
   ```bash
   streamlit run qabot_memory.py
   ```
2. Navigate to http://localhost:8501 in your web browser to access the chatbot.

3. Load your text document by modifying the file path in the code (D:/vs/chatbot/unseen_pasage.txt).


### How the prompt template improves the system's performance and accuracy 
- **Instructions**
     The instruction ensures that the system understands the information provided in the context and gives a concise answer, which is crucial for providing accurate and relevant answers.
     This makes the system be aware of the context all the time and not go out of context, thus improving the accuracy and relevancy

- **Examples**
     The provided examples serve as valuable demonstrations of how to follow the instructions and apply them to different types of questions. These examples help the system to understand the expected format and tone of the answers.

- **Structure**
     The clear structure of the prompt template, with separate sections for the context, question, and answer, helps to organize the information and make it easier for the system to process.

Overall, the prompt template effectively guides the system towards providing accurate, concise, and relevant answers to questions, improving its overall performance and accuracy.



### Explanation of code
Explanation of the code is given as comments in the code itself






