import spacy
import pandas as pd
from spacy import displacy
from spacy.matcher import Matcher 
nlp = spacy.load("en_core_web_sm")

class InformationExtractor():

    def get_action_items(self, text, check):
        
        action_items = []
        
        doc = nlp(text)
        
        # initiatives
        items_list = ['task','complete',
                    'assign','plan']
        
        # pattern to match initiatives names 
        pattern = [{'POS':'DET'},
                {'POS':'PROPN','DEP':'compound'},
                {'POS':'PROPN','DEP':'compound'},
                {'POS':'PROPN','OP':'?'},
                {'POS':'PROPN','OP':'?'},
                {'POS':'PROPN','OP':'?'},
                {'LOWER':{'IN':items_list},'OP':'+'}
                ]
        
        if check == 0:
            # return blank list
            return action_items

        # Matcher class object 
        matcher = Matcher(nlp.vocab) 
        matcher.add("matching", [pattern]) 
        matches = matcher(doc)

        for i in range(0,len(matches)):
            
            # match: id, start, end
            start, end = matches[i][1], matches[i][2]
            
            if doc[start].pos_=='DET':
                start = start+1
            
            # matched string
            span = str(doc[start:end])
            
            if (len(action_items)!=0) and (action_items[-1] in span):
                action_items[-1] = span
            else:
                action_items.append(span)
            
        return action_items