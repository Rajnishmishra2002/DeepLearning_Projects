import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

def preprocess_text(docs, oov_token='unknown'):
    # Initialize the tokenizer with an out-of-vocabulary token
    tokenizer = Tokenizer(oov_token=oov_token)
    # Fit the tokenizer on the documents
    tokenizer.fit_on_texts(docs)
    # Get the integer encoded representation of the texts
    sequences = tokenizer.texts_to_sequences(docs)
    return tokenizer, sequences
