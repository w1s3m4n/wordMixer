"""
* Name: Word Mixer
* Description: WordMixer is a simple script to combine a list of words from a file with themselves N times. Being N the
* required depth of mixing. This script is intended to be used in order to create custom wordlists to perform brute force
* attacks.
*
* Author: Pablo Gómez Delgado (w1s3m4n)
"""
import argparse

def getUppers(word):

	"""
	This function creates a list of uppercase letter words from an lowercase word.
	:param word: The initial word
	:return: A list of words. They will be: [All_Upper, All_Lower, First_Upper, Last_Upper] (not in this order)
	"""
	upper_words = []

	listed_word = list(word.lower())

	upper_words.append(word.upper())
	upper_words.append(word.lower())
	listed_word[0] = listed_word[0].upper()
	upper_words.append("".join(listed_word))
	listed_word[0] = listed_word[0].lower()
	listed_word[-1] = listed_word[-1].upper()
	upper_words.append("".join(listed_word))

	return upper_words

def joinwords(words1, words2, depth):

	"""
	Recursive function to mix two wordlists in order to create permutations of their words. It will combine the first
	list with the second one and combine the result again with the second one until depth is reached.
	:param words1: First list to merge
	:param words2: Second list to merge. If you want to keep it simple, mantain this parameter with the initial values
	:param depth: Maximun depth of mixing
	:return: The generated wordlist
	"""

	wordlist =[]
	
	#print("[*] Generating words of depth {}".format(depth))
	if depth <= 0:
		return []

	for i in range(0, len(words1)):
		for j in range(0, len(words2)):
			if (words1[i].lower() != words2[j].lower()) and (words2[j].lower() not in words1[i].lower()):
				wordlist.append(words1[i] + words2[j])

	#print("[*] Generated {} words of depth {}".format(len(wordlist), depth))
	print("\n".join(wordlist))

	depth -= 1
	return wordlist + joinwords(wordlist, words2, depth)


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('inputfile', 'The input file. One word per line. Lowercase' ,default='words.txt')
	parser.add_argument('depth', 'Depth of concatenation. Default: 3 (The higher the depth, the higer the processing requirements)' ,default='words.txt')
	args = parser.parse_args()

	processed_words = []
	descriptor = open(args.inputfile, "r")
	try:
		initial_words = descriptor.read().splitlines()

		#print("[*] Loaded {} words from file '{}'".format(len(initial_words), file))

		# We get all uppercase combinations to include them in our initial list
		for word in initial_words:
			processed_words += getUppers(word)
		processed_words += initial_words

		#print("[*] Starting processing with max depth: {}".format(max_mixes))
		joinwords(processed_words, processed_words, args.depth)
	finally:
		print("[!] ERROR: An error were found. Aborting...")
		descriptor.close()

