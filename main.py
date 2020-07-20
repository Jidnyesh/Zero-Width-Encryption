import binascii
import pyperclip
#To encode
def encode(string_toencode):
    res = bin(int(binascii.hexlify(string_toencode), 16))
    res = res[2:]
    encoded_output = res.replace('0','\u200b').replace('1','\u200c')
    return encoded_output

#To decode
def decode(string_todecode):
    decoded_output = string_todecode.replace('\u200b','0').replace('\u200c','1')
    res = '0b'+decoded_output
    n = int(res, 2)
    decoded_output = binascii.unhexlify('%x' % n)
    return decoded_output


a = int(input("What you want to do?\n1.Encode\n2.Decode\n--> "))

if a==1:
    string = input("Enter the text to encode\n--> ")
    print()
    string = bytes(string,'utf-8')
    encoded_output = encode(string)
    pyperclip.copy("You cannot read "+encoded_output+"this")
    print("Encoded Text is copied to clipboard --> "+"You cannot read "+encoded_output+"this")
    


elif a==2:
    encoded_output = input("Enter the encoded output\n --> ")
    encoded_output = encoded_output[16:-4]
    decoded_output = decode(encoded_output)
    decoded_output = decoded_output.decode("utf-8") 

    print("Decoded output --> "+ decoded_output)