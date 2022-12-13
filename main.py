from modules.speech_recognizer import SpeechRecognizer
from modules.information_extractor import InformationExtractor
from modules.text_processor import TextPreprocessor
from modules.transcript_generator import TranscriptGenerator
import constants
import re
import pandas as pd

"""
speech_recognizer = SpeechRecognizer(constants.AUDIO_FILE)
transcript = speech_recognizer.recognize_speech()
print(transcript)
"""

transcript = (open(constants.DATASET_FILE).read())

information_extractor = InformationExtractor()

text_processor = TextPreprocessor()

transcript_generator = TranscriptGenerator(transcript)

list_of_sentences = transcript_generator.generate_text()
print('Generated text is', list_of_sentences)

# list_of_sentences = text_processor.convert_to_sentences(transcript)

# reduced_sentences = list(map(text_processor.reduce_search_space, list_of_sentences))

# print('Reduced search space is', reduced_sentences)

action_items = list(map(information_extractor.get_action_items, list_of_sentences))

print('Action items are', action_items)

data = {'Transcript': list_of_sentences,
        'Action Items': action_items}

df = pd.DataFrame(data)

df.to_csv('transcript_data.csv')