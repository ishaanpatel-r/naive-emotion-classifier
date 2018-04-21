
import nltk, string, pickle, operator
from nltk import word_tokenize
from collections import Counter

def find_all_occurences_of(this_X_word, in_this_sentence):

	count = 0
	for each_word in tok(in_this_sentence):
		if this_X_word == each_word:
			count += 1

	return count

def emossify(sentence, seeds):

	overall_score = {"ecstasy" : 0, "admiration" : 0, "terror" : 0, 
	"amazement" : 0, "grief" : 0, "loathing" : 0, "rage" : 0, "vigilance" : 0}

	for k, v in seeds.items():
		for each_word in word_tokenize(sentence):
			if each_word in v:
				overall_score[k] += 1

	try:
		emo = max(overall_score, key=overall_score.get)
		confidence = overall_score[emo]/sum([v for k, v in overall_score.items() if v != 0])

		return (emo, confidence)
	except:
		return (emo, 0)

if __name__ == '__main__':

	with open('emotion_seeds.pkl', 'rb') as handle:
		seeds = pickle.load(handle)

	print(emossify("What a wonderful day this is man!", seeds))
	print(emossify("I am depressed.", seeds))
	print(emossify("Are you kidding me?", seeds))
	print(emossify("Shit.", seeds))