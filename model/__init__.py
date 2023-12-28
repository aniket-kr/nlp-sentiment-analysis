import numpy as np

from keras.saving import load_model
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences

from .review_preprocessor import preprocess_text

def get_word_tokenizer():
    with open('model/tokenizer.json', 'r') as file:
        return tokenizer_from_json(file.read())


word_tokenizer = get_word_tokenizer()

lstm_model = load_model('model/lstm-model_acc-0.856.h5')


def predict(review: str) -> float:
    # preprocess the input
    review = preprocess_text(review)

    # tokenize the review
    tokenized_reviews = word_tokenizer.texts_to_sequences(np.array([review]))

    # pad the sequence
    padded_reviews = pad_sequences(tokenized_reviews, padding='post', maxlen=100)

    # predict with model
    return lstm_model.predict(padded_reviews)[0][0]
