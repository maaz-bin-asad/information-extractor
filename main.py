import warnings
from modules.speech_recognizer import SpeechRecognizer
from modules.information_extractor import InformationExtractor
import constants


warnings.filterwarnings("ignore")

speechRecognizer = SpeechRecognizer(constants.AUDIO_FILE)
transcript = speechRecognizer.recognize_speech()
print(transcript)
# transcript = "Thank you so much, Chair, and good morning to everyone. It's wonderful to be invited to talk to you. Welcome to the 100th session of the Committee on Regional Trade Agreements. I am pleased to be able to say a few words to you today and to commend the Committee for its work over the past 25 years in scrutinizing RTAs and considering their systemic implications for the multilateral trading system. Let me start by recalling a few key points and dates: First, the CRTA was established by a Decision of the General Council on 6 February 1996. Its first session was on 21 May 1996, with Ambassador John Weekes of Canada as Chair."

informationExtractor = InformationExtractor()
check_scheme = informationExtractor.prog_sent(transcript)
schemes = informationExtractor.all_schemes(transcript, check_scheme)
print(schemes)