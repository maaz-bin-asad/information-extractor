import spacy
import pandas as pd
from spacy import displacy
from spacy.matcher import Matcher 
nlp = spacy.load("en_core_web_sm")

class InformationExtractor():

    def get_action_items(self, text):
        
        if(text == None):
            return 

        action_items = []
        
        doc = nlp(text)
        
        nouns_list = ['task','bug',
                    'issue','feature']
         
        pattern = [
                {'POS':'PROPN','OP':'?'},
                {'POS':'PROPN','OP':'?'},
                {'LOWER':{'IN':nouns_list},'OP':'+'},
                {'POS':'PROPN','OP':'?'},
                ]

        matcher = Matcher(nlp.vocab) 
        matcher.add("matching", [pattern]) 
        matches = matcher(doc)

        for match_id, start, end in matches:
            print(doc[start:end])