import time, os, sys
import transpositionEncrypt 
import transpositionDecrypt

def main(
		file_name='example.txt',
		output_filename='example_file_name.txt',
		my_key=10,
		my_mode='encrypt'):

	if not os.path.exists(file_name):
		print(f'The file {file_name} does not exist. Quitting process...')
		sys.exit()

	if os.path.exists(output_filename):
		print(f'This will overwritte the file {output_filename}. (C)ontinue or (Q)uit')
		response = input('> ')
		if not response.lower().startswith('c'):
			sys.exit()

	file_obj = open(file_name)
	content = file_obj.read()
	file_obj.close()

	print(f'{my_mode.title()}sing...')

	start_time = time.time()
	if my_mode == 'encrypt':
		translated = transpositionEncrypt.encryptMessage(my_key, content)
	elif my_mode == 'decrypt':
		translated = transpositionDecrypt.decryptMessage(my_key, content)
	totalTime = round(time.time() - start_time, 2)
	print(f'{my_mode.title()}sion time: {totalTime} seconds')

	output_file_obj = open(output_filename, 'w')
	output_file_obj.write(translated)
	output_file_obj.close()

	print(f'Done {my_mode}sing {file_name} ({len(content)} characters).')
	print(f'{my_mode}ed file is {output_filename}.')


if __name__ == '__main__':
	main()
