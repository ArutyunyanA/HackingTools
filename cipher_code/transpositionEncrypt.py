import pyperclip


def main(
	myMessage='Hello world!',
	myKey=8
):

	ciphertext = encryptMessage(myKey, myMessage)
	print(ciphertext + '|')

	pyperclip.copy(ciphertext)

def encryptMessage(key, message):
	ciphertext = [''] * key

	for x in range(key):
		currentIndex = x
		
		while currentIndex < len(message):
			ciphertext[x] += message[currentIndex]
			currentIndex += key

	return ''.join(ciphertext)

if __name__ == '__main__':
	main()
