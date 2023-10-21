import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
import nltk
from src.exception import CustomException
from src.logger import logging
import sys

from src.logger import logging

from string import punctuation

p=punctuation

# Download the spaCy model
# spacy.cli.download('en_core_web_sm')

nlp=spacy.load('en_core_web_sm')

stopwords=list(STOP_WORDS)
def doc(text):
    try:
        doc=nlp(text)
        tokens=[i for i in doc]
        logging.info("Tokens Created Succesfully")
        punctuation=p + '\n'

        word_freq={}
        for i in tokens:
            if i.text.lower() not in stopwords:
                if i.text.lower() not in punctuation:
                    if i.text.lower() not in word_freq.keys():
                        word_freq[i.text.lower()]=1
                    else:
                        word_freq[i.text.lower()]+=1
        
        max_len=max(word_freq.values())

        

        for i in word_freq.keys():
            word_freq[i]=word_freq[i]/max_len
        
        logging.info("Word Frequency Created")

        sent_freq={}
        sent=[i for i in doc.sents]

        for i in sent:
            for j in i:
                if j.text.lower() in word_freq.keys():
                    if i not in sent_freq.keys():
                        sent_freq[i]=word_freq[j.text.lower()]
                    else:
                        sent_freq[i]+=word_freq[j.text.lower()]

        logging.info("Sentence Frequency Created")

        summary_length=int(len(sent)*0.3)

        summary=nlargest(summary_length,sent_freq,key=sent_freq.get)

        summary=' '.join([str(i) for i in summary])

        return summary
                    

    except Exception as e:
        raise CustomException(e,sys)


