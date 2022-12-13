import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import RNN
from keras.utils import np_utils
import keras

# dataset reference https://www.kaggle.com/datasets/gogogaurav95/conversation-meetings

class TranscriptGenerator:
    def __init__(self, text):
        self.text = text

    def createModel(self, X_modified, Y_modified):

        model = Sequential()
        model.add(LSTM(100, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(100, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(100))
        model.add(Dropout(0.2))
        model.add(Dense(Y_modified.shape[1], activation='softmax'))

        model.compile(loss='categorical_crossentropy', optimizer='adam')


        model.fit(X_modified, Y_modified, epochs = 50, batch_size = 50)
        return model
    
    def generate_text(self):
        text = self.text.lower()
        characters = sorted(list(set(text)))

        int_to_char = {n:char for n, char in enumerate(characters)}
        char_to_int = {char:n for n, char in enumerate(characters)}


        X = []
        Y = []
        length = len(text)
        seq_length = 100

        for i in range(0, length-seq_length, 1):
            sequence = text[i:i + seq_length]
            label = text[i + seq_length]
            X.append([char_to_int[char] for char in sequence])
            Y.append(char_to_int[label])


        X_modified = np.reshape(X, (len(X), seq_length, 1))
        X_modified = X_modified / float(len(characters))
        Y_modified = np_utils.to_categorical(Y)


        # already trained model
        # model = keras.models.load_model('model_network.h5')

        model = self.createModel(X_modified, Y_modified)
        

        transcripts_list = []

        for i in range(100):
            start = np.random.randint(0, len(X)-1)
            pattern = X[start]
            full_string = [int_to_char[value] for value in pattern]
            for i in range(100):
                x = np.reshape(pattern,(1,len(pattern), 1))
                x = x / float(len(characters))

                pred_index = np.argmax(model.predict(x, verbose=0))
                seq = [int_to_char[value] for value in pattern]
                full_string.append(int_to_char[pred_index])

                pattern.append(pred_index)
                pattern = pattern[1:len(pattern)]
            
            generated_text = ""

            for char in full_string:
                generated_text = generated_text + char
            
            generated_text
            
            transcripts_list.append(generated_text)
        
        return transcripts_list