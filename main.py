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
# transcript = "Can we aim to complete it by today. yes sure? lets plan to complete it"
transcript = transcript.lower()
list_of_sentences = text_processor.convert_to_sentences(transcript)
fixed_matched_phrases = list(map(text_processor.collect_fixed_patterns, list_of_sentences))
action_items = list(map(information_extractor.get_action_items, fixed_matched_phrases))