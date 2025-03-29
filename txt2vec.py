import config as cfg

import os

import glob

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_together import TogetherEmbeddings
from langchain_community.vectorstores import FAISS

if os.path.exists('./vec_db') == False:
    os.mkdir('./vec_db')

def vectorize(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = cfg.chunk_size, chunk_overlap = cfg.chunk_overlap)
    chunks = text_splitter.split_text(text)
    print(len(chunks)) # Debugging
    vector_store = FAISS.from_texts(
        chunks,
        TogetherEmbeddings(
            model = cfg.embedding_model,
            api_key = cfg.api_key
        )
    )
    return vector_store

def txt2vec(txt_directory = './src/txt', save_path = cfg.vec_path):
    documents = glob.glob(txt_directory + '/*.txt')
    for document in documents:
        if '\\' in document:
            document = document.replace('\\', '/')
        filename = document.split('/')[-1].split('.')[0]
        with open(document, "r", encoding="utf-8") as f:
            text = f.read()
        vector_store = vectorize(text)
        vector_store.save_local(save_path + filename + '_index')

if __name__ == "__main__":
    txt2vec()