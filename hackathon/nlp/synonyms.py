import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
def getSynonyms(sentence):
    words = nltk.word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    #print(stop_words)
    filtered_sentence = [w for w in words if not w in stop_words and len(w)>3 ]
    dictionary = {}
    for word in filtered_sentence:
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if not lemma.name() in synonyms and lemma.name()!=word:
                    synonyms.append(lemma.name())
        dictionary[word] = synonyms
    return dictionary
    #print(filtered_sentence)
    #print(dictionary)
