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
    # split the cipher to match the lenght of the key
    # convert the message to index and add the key
