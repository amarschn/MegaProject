# Author: Drew Marschner
# Date: 1/17/2014

# Enter a string and the program counts the number of vowels in the text. For
# added complexity have it report a sum of each vowel found.

from collections import Counter

'''
Given a string, return the vowel count of each vowel in that string
'''
def vowel_count(string):
	vowels = 'aeiou'
	vowel_dict = {}
	# count the number of each vowel in the string
	for v in vowels:
		vowel_dict[v] = string.count(v)
	return vowel_dict