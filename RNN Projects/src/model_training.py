from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

def create_rnn_model(vocab_size, embedding_dim=10, rnn_units=10):
    # Define a simple RNN model
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=embedding_dim),
        SimpleRNN(units=rnn_units),
        Dense(units=1, activation='sigmoid')
    ])
    return model
