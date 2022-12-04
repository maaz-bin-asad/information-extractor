import spacy
import pandas as pd
from spacy import displacy
from spacy.matcher import Matcher 
nlp = spacy.load("en_core_web_sm")

class InformationExtractor():

    def get_action_items(self, text):
        
        if(text == None):
            return 
        
        doc = nlp(text)
        
        # (optional)create a dependancy graph of the sentence for understanding the pattern in words
        # displacy.serve(doc, style="dep")
         
        pattern = [
                {'POS':'AUX','OP':'*'},
                {'POS':'PRON','OP':'*'},
                {'POS':'VERB','OP':'+'},
                {'POS':'PART','OP':'+'},
                {'POS':'VERB','OP':'+'},
                {'POS':'DET','OP':'*'},
                {'POS':'NOUN','OP':'+'},
                {'POS':'ADP','OP':'*'},
                {'POS':'NOUN','OP':'*'},
                ]

        matcher = Matcher(nlp.vocab) 
        matcher.add("matching", [pattern]) 
        matches = matcher(doc)

        if(len(matches) == 0):
            return

        possibles_matches = []
        for match_id, start, end in matches:
            possibles_matches.append(doc[start:end])
        
        return possibles_matches[-1]