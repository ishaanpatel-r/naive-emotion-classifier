
#  importies!
import pickle
from pprint import pprint
from gensim.models import KeyedVectors
from collections import Counter
from itertools import chain
import nltk
model = KeyedVectors.load_word2vec_format('word_embs.pkl')
how_many = 1000

def unique_for(list_to_filter, *lists_from):

	# flatten all compound lists and set
	flatten = lambda l: [item for sublist in l for item in sublist]

	# unique list composition
	new_unique = [i for i in list_to_filter if i not in set(flatten(lists_from[0]))]	
	return new_unique

list_of_emotions = ["ecstasy", "admiration", "terror", "amazement", "grief", "loathing", "rage", "vigilance"]

filtered_seeds = {k: [] for k in list_of_emotions}

# needs to refill everytime
seed_dict = {k: [] for k, v in filtered_seeds.items()}

# loop to get most frequently existing words
for x in range(10):

	for e in model.most_similar(positive=['excited', 'sensuous', 'energetic',
		'cheerful', 'creative', 'hopeful'], topn=how_many):
		seed_dict['ecstasy'] += [e[0]]

	for e in model.most_similar(positive=['content', 'thoughtful', 'intimate',
		'loving', 'trusting', 'nurturing'], topn=how_many):
		seed_dict['admiration'] += [e[0]]

	for e in model.most_similar(positive=['confused', 'rejected', 'helpless',
		'submissive', 'insecure', 'anxious'], topn=how_many):
		seed_dict['terror'] += [e[0]]

	for e in model.most_similar(positive=['faithful', 'important', 'appreciated',
		'respected', 'proud', 'aware'], topn=how_many):
		seed_dict['amazement'] += [e[0]]

	for e in model.most_similar(positive=['guilty', 'ashamed', 'depressed',
		'lonely', 'bored', 'tired'], topn=how_many):
		seed_dict['grief'] += [e[0]]

	for e in model.most_similar(positive=["distaste", "hatred", "antipathy",
		"disdain", "hostility", "revulsion"], topn=how_many):
		seed_dict['loathing'] += [e[0]]

	for e in model.most_similar(positive=['critical', 'hateful', 'selfish',
		'angry', 'hurt', 'hostile'], topn=how_many):
		seed_dict['rage'] += [e[0]]

	for e in model.most_similar(positive=['alert', 'diligence', 'precautious',
		'prudence', 'watchful', 'hostile'], topn=how_many):
		seed_dict['vigilance'] += [e[0]]


seeds = {}

for emotion, respective_correspondence in seed_dict.items():
	seeds[emotion] = unique_for(set(respective_correspondence), [v for k, v in seed_dict.items() if v != respective_correspondence])

# store cognitive seeds
with open('emotion_seeds.pkl', 'wb') as handle:
	pickle.dump(seeds, handle, protocol=pickle.HIGHEST_PROTOCOL)