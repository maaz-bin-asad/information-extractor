import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self, audioFile):
        self.audioFile = audioFile

    def recognize_speech(self):
        r = sr.Recognizer()
        with sr.AudioFile(self.audioFile) as source:
            audio_text = r.listen(source)
            text = r.recognize_google(audio_text)
            print('Converting to text...')
            return text