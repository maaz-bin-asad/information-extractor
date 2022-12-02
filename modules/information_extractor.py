import spacy
import pandas as pd
from spacy import displacy
from spacy.matcher import Matcher 
import re 

nlp = spacy.load("en_core_web_sm")

class InformationExtractor():

    def all_schemes(text,check):
        
        schemes = []
        
        doc = nlp(text)
        
        # initiatives
        prog_list = ['programme','scheme',
                    'initiative','campaign',
                    'agreement','conference',
                    'alliance','plan']
        
        # pattern to match initiatives names 
        pattern = [{'POS':'DET'},
                {'POS':'PROPN','DEP':'compound'},
                {'POS':'PROPN','DEP':'compound'},
                {'POS':'PROPN','OP':'?'},
                {'POS':'PROPN','OP':'?'},
                {'POS':'PROPN','OP':'?'},
                {'LOWER':{'IN':prog_list},'OP':'+'}
                ]
        
        if check == 0:
            # return blank list
            return schemes

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
            
            if (len(schemes)!=0) and (schemes[-1] in span):
                schemes[-1] = span
            else:
                schemes.append(span)
            
        return schemes

    def prog_sent(text):
        
        patterns = [r'\b(?i)'+'plan'+r'\b',
                r'\b(?i)'+'programme'+r'\b',
                r'\b(?i)'+'scheme'+r'\b',
                r'\b(?i)'+'campaign'+r'\b',
                r'\b(?i)'+'initiative'+r'\b',
                r'\b(?i)'+'conference'+r'\b',
                r'\b(?i)'+'agreement'+r'\b',
                r'\b(?i)'+'alliance'+r'\b']

        output = []
        flag = 0
        for pat in patterns:
            if re.search(pat, text) != None:
                flag = 1
                break
        return flag