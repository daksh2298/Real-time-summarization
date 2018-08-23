'''
NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
'''

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")

# sample_text=state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# tokenized=custom_sent_tokenizer.tokenize(sample_text)


def process_content(tweet):
    sample_text = tweet
    tokenized = custom_sent_tokenizer.tokenize(sample_text)
    try:
        tagged = []
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged += nltk.pos_tag(words)
            # namedEnt=nltk.ne_chunk(tagged)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            # print namedEnt
            L = str(namedEnt).strip('(').strip(')').split()
            # print L
            d = {}
            nn = []
            nnp = []
            for a in range(1, len(L)):
                inner = L[a].split('/')
                if inner[1] == 'NN' or inner[1] == 'NNS':
                    nn.append(inner[0])
                elif inner[1] == 'NNP' or inner[1] == 'NNPS':
                    nnp.append(inner[0])
            d['NN'] = nn
            d['NNP'] = nnp
            # print d
    except Exception as e:
        print 'abbriv', str(e)
    return d
#process_content("hello i am yash.")
