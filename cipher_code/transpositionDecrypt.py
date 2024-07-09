

import math, pyperclip

def main(
	myMessage='Cenoonommstmme oo snnio. s s c',
	myKey=8
):
	
	plaintext = decryptMessage(myKey, myMessage)
	print(plaintext + '|')
	pyperclip.copy(plaintext)


def decryptMessage(key, message):

	num0fColumns = int(math.ceil(len(message) / float(key)))
	num0fRows = key
	num0fShadedBoxes = (num0fColumns * num0fRows) - len(message)

	plaintext = [''] * num0fColumns

	column = 0
	row = 0

	for x in message:
		plaintext[column] += x
		column += 1

		if column == num0fColumns or column == num0fColumns - 1 and row >= num0fRows - num0fShadedBoxes:
			column = 0
			row += 1

	return ''.join(plaintext)


if __name__ == '__main__':
	print(main())
