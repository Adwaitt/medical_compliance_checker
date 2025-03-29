embedding_model = 'togethercomputer/m2-bert-80M-8k-retrieval'
generation_model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
chunk_size = 300
chunk_overlap = 50
api_key = '858b33d427ffa45005f77c92be897c982163308764ad0b2e8b3c89f7700c60bd'
vec_path = './vec_db/'
# template = """Answer the question in "compliant" or "non-compliant" based only on the following context:
#     {context}

#     Question: {question}
#     If the answer is non-compliant, provide a brief explanation.
#     """
template = """You are a compliance checker for medical claims based on regulatory guidelines. Evaluate the claim based only on the given context.

    Context:
    {context}

    Claim:
    {question}

    Answer with either:
    - "Compliant."
    - "Non-Compliant. Reason: <explanation>."

    Ensure your response is fair, unbiased, and based strictly on the provided context.
    """