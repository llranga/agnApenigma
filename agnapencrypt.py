import string
from random import shuffle,seed

special_char=string.punctuation
numbers=string.digits
alphabet=string.ascii_letters
wspaces=string.whitespace
#adding space char 
alpha_numaric=special_char+numbers+alphabet+" "+wspaces
#covert to a list
values=list(alpha_numaric)

# if seed value is same, it will always generate same list after shuffling

def encrypt(plain_text:str,seed_value='4'):
    '''énter text to be encrypted and seed value. same seed value must be used to decrypt the message.
    if not provided, seed value default is 4'''
    # copying values to keys
    keys=values.copy()
    #setting the seed value
    seed(seed_value)
    #shuffle the keys
    shuffle(keys)
    #print(values)
    #print(keys)
    encrypted_text=""
    for ele in plain_text:
        num=values.index(ele)
        encrypted_text+=keys[num]
    #print(encrypted_text)   
    return encrypted_text


def decrypt(encrypted_text:str,seed_value='4'):
    '''énter text to be decrypted and seed value. same seed value must be used to decrypt the message.
    if not provided, seed value default is 4'''
    keys=values.copy()
    seed(seed_value)
    shuffle(keys)
    #print(values)
    #print(keys)
    decrypted_text=""
    for ele in encrypted_text:
        num=keys.index(ele)
        decrypted_text+=values[num]
    #print(decrypted_text)
    return decrypted_text

'''def main():

    
    plain_text=input("Type the message to encrypt ")
    print(encrypt(plain_text))
    encrypted_text=input("Enter the encypted message to decrypt ")
    print(decrypt(encrypted_text))

if __name__=="__main__":
    main()'''
