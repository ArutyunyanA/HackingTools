import pyperclip


def cesar_cipher(msg, key, mode, SYMBOLS):
        
        
        translated = ''

        for x in msg:
                if x in SYMBOLS:
                        symbol = SYMBOLS.find(x)
                        if mode == 'encrypt':
                                translate = symbol + key
                        elif mode == 'decrypt':
                                translate = symbol - key
                
                        if translate >= len(SYMBOLS):
                                translate -= len(SYMBOLS)
                        elif translate < 0:
                                translate += len(SYMBOLS)

                        translated += SYMBOLS[translate]
                else:
                        translated += x

        return translated
        pyperclip.copy(translated)
        

print(cesar_cipher(input('<<::Please type the key-word::>>\n'), 13, 'encrypt', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'))
