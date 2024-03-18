import string
  

def secret_msg():
    keys = string.printable
    values = keys[-5:-1] + keys[0:-5]

    dict_e = dict(zip(keys, values))
    dict_d = dict(zip(values, keys))

    msg = input('Enter you message: ')
    mode = input('Crypto mode: endode (e) OR decrypt as default: ')

    if(mode.lower() == 'e'):
        new_msg = ''.join([dict_e[letter] for letter in msg])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg])
    
    return new_msg

print(secret_msg())