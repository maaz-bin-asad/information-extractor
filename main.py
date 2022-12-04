from modules.speech_recognizer import SpeechRecognizer
from modules.information_extractor import InformationExtractor
from modules.text_processor import TextPreprocessor
import constants
from nltk import tokenize
import re

speech_recognizer = SpeechRecognizer(constants.AUDIO_FILE)

information_extractor = InformationExtractor()

text_processor = TextPreprocessor()
transcript = speech_recognizer.recognize_speech()
print(transcript)

# transcript = "Can we aim to complete the notification task by today? Yes! Let's plan to complete it. Plan to complete the button task"

transcript = transcript.lower()

list_of_sentences = text_processor.convert_to_sentences(transcript)

reduced_sentences = list(map(text_processor.reduce_search_space, list_of_sentences))

print('Reduced search space is', reduced_sentences)

action_items = list(map(information_extractor.get_action_items, reduced_sentences))

print('Action items are')

num = 1
for i in range(len(action_items)):
    if(action_items[i]!= None):
        print('{}. {}'.format(num, action_items[i]))
        num += 1