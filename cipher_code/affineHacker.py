

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main(
		myMessage=input(str('<::Please insert ecnrypted message::>\n'))
):
	hackedMessage = hackAffine(myMessage)

	if hackedMessage != None:
		print('Copying hacked message to clopboard:')
		print(hackedMessage)
		pyperclip.copy(hackedMessage)
	else:
		print('Faild to hacked encryption.')

def hackAffine(message):
	print('Hacking...')
	print('(Press Ctrl-C or Ctrl-D to quit at any time to terminate the programm)')

	for key in range(len(affineCipher.SYMBOLS) ** 2):
		keyA = affineCipher.getKeyParts(key)[0]
		if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:			
			continue
		decryptedText = affineCipher.decryptMessage(key, message)
		if not SILENT_MODE:
			print(f'Tried key {key}... ({decryptedText[:40]})')
		if detectEnglish.isEnglish(decryptedText):
			print()
			print('Possible encryption hack:')
			print(f'Key: {key}')
			print('Decrypted message:' + decryptedText[:200])
			print()
			print('Enter D for done, or just press Enter to continue hacking:')
			response = input('> ')

			if response.strip().upper().startswith('D'):
				return decryptedText
	return None


if __name__ == '__main__':
	main()
