from modules.speech_recognizer import SpeechRecognizer
from modules.information_extractor import InformationExtractor
from modules.text_processor import TextPreprocessor
import constants
from nltk import tokenize
import re

speech_recognizer = SpeechRecognizer(constants.AUDIO_FILE)
information_extractor = InformationExtractor()
text_processor = TextPreprocessor()
# transcript = speech_recognizer.recognize_speech()
# print(transcript)
transcript = "Can we aim to complete it by today. Yes sure? Lets plan to complete it"

list_of_sentences = text_processor.convert_to_sentences(transcript)
fixed_matched_phrases = list(map(text_processor.collect_fixed_patterns, list_of_sentences))
print(fixed_matched_phrases)
action_items = information_extractor.get_action_items(transcript, fixed_matched_phrases)
print(action_items)