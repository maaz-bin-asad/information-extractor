import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self, audioFile):
        self.audioFile = audioFile

    def recognize_speech(self):
        r = sr.Recognizer()
        with sr.AudioFile(self.audioFile) as source:
            audio_text = r.listen(source)
            print('Converting to text...')
            text = r.recognize_google(audio_text)
            return text