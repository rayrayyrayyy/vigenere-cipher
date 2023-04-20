import pyfiglet
from termcolor import colored, cprint
print_green = lambda x: cprint(x, 'green')
print_blue = lambda x: cprint(x, 'blue')

# create a dictionary
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_length = dict(zip(alphabet, range(len(alphabet))))
index_lenght = dict(zip(range(len(alphabet)), alphabet))

# define encryption
def encryption(message, key):
    encrypt = ''

  # split the message to match the lenght of the key
    _split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))] # start, end, step
  # convert the message to index and add the key
    for each_split in _split_message:
        i = 0
        for letter in each_split:
            number_text = (letter_length[letter] + letter_length[key[i]]) % len(alphabet)
            encrypt += index_lenght[number_text]
            i += 1
    return encrypt

# define decryption
def decryption(cipher, key):
    decrypt = ''
    # split the cipher to match the lenght of the key
    _split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))] # start, end, step
    # convert the message to index and add the key
    for each_split in _split_cipher:
        i = 0
        for letter in each_split:
            number_text = (letter_length[letter] - letter_length[key[i]]) % len(alphabet)
            decrypt += index_lenght[number_text]
            i += 1

    return decrypt
