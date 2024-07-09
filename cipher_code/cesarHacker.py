


def decode_cipher(SYMBOLS, encryption):

        for key in range(len(SYMBOLS)):
                decrypt = ''
                for i in encryption:
                        if i in SYMBOLS:
                                symbolInd = SYMBOLS.find(i)
                                decryptInd = symbolInd - key

                                if decryptInd < 0:
                                        decryptInd += len(SYMBOLS)
                                decrypt += SYMBOLS[decryptInd]
                        else:
                                decrypt += i
                                
                print(f'Key: {key}, {decrypt}')

decode_cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.', input('<::Please type the encrypted message::>\n'))
