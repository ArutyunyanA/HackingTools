import base64

def bs64decode(text):
    decrypt = base64.b64decode(text)
    return decrypt
if __name__ == '__main__':
    print(bs64decode(input('Please insert text to decode:\n')))