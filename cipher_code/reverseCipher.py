
def reverseCipher(message, reverse):
	words = len(message) - 1

	while words >= 0:
		reverse += message[words]
		words -= 1
	print(reverse)

reverseCipher(input('<::Please type the text::>\n'), '')



