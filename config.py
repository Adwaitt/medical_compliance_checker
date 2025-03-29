embedding_model = 'togethercomputer/m2-bert-80M-8k-retrieval'
generation_model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
chunk_size = 300
chunk_overlap = 50
api_key = ''
vec_path = './vec_db/'
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