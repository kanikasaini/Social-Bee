from django.shortcuts import render
from django.http import HttpResponse
import json
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Create your views here.
def find(datastore, tags):
	size = len(datastore);
	selected = {};
	for i in range(size):
		for j in range(len(tags)):
			for k in range(len(datastore[i]['Tags'])):
				if(tags[j] == datastore[i]['Tags'][k]):
						selected[datastore[i]['Quote']] = datastore[i]['Popularity'];
				break;
	return selected;

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

def index(request):
	return render(request,'nlp/index.html',{})

def secondview(request):
	if request.method == "GET":
		get_text = request.GET["textfield"]
		with open('quotes.json', 'r') as f:
			datastore = json.load(f)
		tags = []
		tags.append(get_text)
		selected = find(datastore, tags);
		text = ""
		for i in selected:
			text = text + i + "\n"
		text = "<h3>" + text + "</h3>" 
	return HttpResponse(text)

def thirdview(request):
	if request.method == "GET":
		get_text = request.GET["sentence"]
		selected = getSynonyms(get_text)
		text = ""
		for i in selected.keys():
			text = "\n" + i + ": "
			for j in selected.get(i):
				text = text + j + "\n"
		text = "<h3>" + text + "</h3>" 
	return HttpResponse(text)


