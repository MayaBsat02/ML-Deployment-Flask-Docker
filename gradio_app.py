from tensorflow.keras.models import model_from_json
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import gradio as gr

# Load the model architecture
with open('model/model2_architecture.json', 'r') as f:
    model2_architecture = f.read()

# Create the model from the loaded architecture
model2 = model_from_json(model2_architecture)

# Load the model weights
model2.load_weights('model/model2_weights.h5')

# Load the English tokenizer
with open('model/english_tokenizer.pkl', 'rb') as f:
    english_tokenizer = pickle.load(f)

# Load the French tokenizer
with open('model/french_tokenizer.pkl', 'rb') as f:
    french_tokenizer = pickle.load(f)


def predict(input_sentence):
    max_sequence_length = 14
    # Tokenize the input sentence
    input_sequence = english_tokenizer.texts_to_sequences([input_sentence])
    input_sequence = pad_sequences(input_sequence, maxlen=max_sequence_length, padding='post')

    # Predict the output sequence
    output_sequence = model2.predict(input_sequence)
    output_sequence = np.argmax(output_sequence, axis=-1)

    # Convert the output sequence to French sentence
    output_sentence = " ".join(french_tokenizer.index_word[token] for token in output_sequence[0] if token != 0)

    # Return the translated sentence
    return output_sentence.strip()


iface = gr.Interface(fn=predict, inputs="textbox", outputs="text")
iface.launch()
