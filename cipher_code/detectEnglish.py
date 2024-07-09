
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + '\t\n'

def loadDictionary(
	dict_file=open('dictionary.txt'),
	englishWords={}
):

	for word in dict_file.read().split('\n'):
		englishWords[word] = None
	dict_file.close()
	return englishWords

ENGLISH_WORDS = loadDictionary()


def getEnglishCount(message):
	message = message.upper()
	message = removeNonLetters(message)
	possibleWords = message.split()

	if possibleWords == []:
		return 0.0

	matches = 0
	for word in possibleWords:
		if word in ENGLISH_WORDS:
			matches += 1
	return float(matches) / len(possibleWords)

def removeNonLetters(message):
	lettersOnly = []
	for symbol in message:
		if symbol in LETTERS_AND_SPACE:
			lettersOnly.append(symbol)
	return ''.join(lettersOnly)

def isEnglish(message, wordsPercentage=20, letterPercentage=85):
	wordsMatch = getEnglishCount(message) * 100 >= wordsPercentage
	numletters = len(removeNonLetters(message))
	messageLettersPercentage = float(numletters) / len(message) * 100
	lettersMatch = messageLettersPercentage >= letterPercentage
	return wordsMatch and lettersMatch

