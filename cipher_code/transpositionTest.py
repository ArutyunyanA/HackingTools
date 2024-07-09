import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42)

    for x in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        x += 1
        print(f'Test #{x}, {message[:50]}')

        for key in range(1, int(len(message) / 2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message) 
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if message != decrypted:
                print(f'Mistmatch with{key},{message}')
                print('Decrypted as: ' + decrypted)
                sys.exit()
    print('Transposition test passed')

if __name__ == '__main__':
    main()