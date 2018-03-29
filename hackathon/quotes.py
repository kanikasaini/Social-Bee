import json;
import sys;

def find(datastore, tags):
	size = len(datastore);
	selected = {};
	for i in range(size):
		for j in range(len(tags)):
			for k in range(len(datastore[i]['Tags'])):
				if(tags[j] == datastore[i]['Tags'][k]):
						selected[datastore[i]['Quote']] = datastore[i]['Popularity'];
				break;
	



if __name__=="__main__":
	with open('quotes.json', 'r') as f:
		datastore = json.load(f)
		tags = ['kiss'];
		find(datastore, tags);
