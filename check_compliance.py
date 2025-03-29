import config as cfg

from langchain_community.vectorstores import FAISS
from langchain_together import Together, TogetherEmbeddings

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

class GenResults():
    def __init__(self, compliance):
        vector_store = FAISS.load_local(
            folder_path = cfg.vec_path + compliance + '_index',
            embeddings = TogetherEmbeddings(
                model = cfg.embedding_model,
                api_key = cfg.api_key
            ),
            allow_dangerous_deserialization = True
        )
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})

        model = Together(model = cfg.generation_model,     
                         temperature = 0.7,
                         max_tokens = 128,
                         top_k = 50,
                         api_key = cfg.api_key)
        prompt = ChatPromptTemplate.from_template(cfg.template)
        output_parser = StrOutputParser()
        setup_and_retrieval = RunnableParallel(
            {"context": retriever, "question": RunnablePassthrough()}
        )
        self.chain = setup_and_retrieval | prompt | model | output_parser

    def compliance_check(self, query):
        output = self.chain.invoke(query)
        return output
    
if __name__ == '__main__':
    obj = GenResults('ema')
    query = "[Product Name] contains [Ingredient], which supports normal immune function, as per EFSA-authorized health claims (Regulation (EC) No 1924/2006) and is compliant with FDA DSHEA and HSA guidelines."
    output = obj.compliance_check(query)
    print(output)