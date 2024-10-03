# QA Chatbot

This project implements a Question-Answering (QA) Chatbot using LangChain and Streamlit. It allows users to ask questions related to a specified text document, providing concise and accurate answers based on the content.

## Features

- Load and display document content.
- Interactive question-and-answer functionality.
- Memory to track conversation history.

## Installation
1.Clone the repository:
   ```bash
   git clone https://github.com/jsjoel/qachatbot.git
   cd qachatbot
   ```
2.Install necessary libraries
   ```bash
   pip install transformers torch langchain
   ```
   Additional libraries
   ```bash
   pip install torch torchvision torchaudio
   pip install langchain-community
   pip install -U sentence-transformers
   ```
### Explanation of Packages
transformers: A library by Hugging Face that provides pre-trained models for Natural Language Processing (NLP) tasks, including language modeling and text classification.
torch: The core library for PyTorch, a popular framework for deep learning.
langchain: A framework for developing applications using language models.
torchvision: A package that provides datasets, model architectures, and image transformations for computer vision tasks.
torchaudio: A package for audio processing tasks with PyTorch.
langchain-community: A community-driven extension of the LangChain library that provides additional tools and features.
sentence-transformers: A library that makes it easy to use pre-trained models for sentence and text embedding tasks.



