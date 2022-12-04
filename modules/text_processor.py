import re
import spacy
nlp = spacy.load('en_core_web_sm')

class TextPreprocessor:
    def convert_to_sentences(self, text):
        return [str(sentence) for sentence in nlp(text).sents]
    
    def reduce_search_space(self, text):
        list_of_keywords = ['plan', 'task', 'aim', 'target', 'take over', 'assign', 'bug']
        matched = re.findall('[^,]*(?:{}|{}|{}|{}|{}|{}|{})[^,]*'.format(list_of_keywords[0], list_of_keywords[1], list_of_keywords[2], list_of_keywords[3], list_of_keywords[4], list_of_keywords[5], list_of_keywords[6]), text)
        if(len(matched) != 0):
            return matched[0]