"""

Matthew Dennison
NCS 541
Assignment 1

"""
import argparse
import binascii

parser = argparse.ArgumentParser(description="Caesar Cipher")
group = parser.add_mutually_exclusive_group()
group.add_argument("-e", "--encrypt", action="store_true",
        help="Encrypt plaintext")
group.add_argument("-d", "--decrypt", action="store_true",
       help="Decrypt cyphertext")
group.add_argument("-c", "--charlie", action="store_true",
        help="Charlie's intercepted tampered cyphertext")
group.add_argument("-diff", "--difference", action="store_true",
      help="Decrypting Charlie's modified cyphertext")
parser.add_argument("string", help="String to be encrypted or decryped")


def encrypt_plaintext(args):
    message = args.string.lower()
    ct = ""
    key = 3
    for i in message:
        ct += chr((((ord(i) - 97) + key) % 26) + 97)
    print "The encrypted message is: " + ct


def decrypt_cyphertext(args):
    message = args.string.lower()
    pt = ""
    key = 3
    for i in message:
        pt += chr((((ord(i) - 97) - key) % 26) + 97)
    print "The decrypted message is: " + pt


def decrypt_intercepted(args):
    message = args.string.lower()
    flipped = ""
    binary_ct = bin(int(binascii.hexlify(message), 16))
    print "Charlie's intercepted cyphertext in binary:" + "\n" + binary_ct 
     
    for i in binary_ct[-10:]:
        tmp = int(i)
        tmp ^= 1
        flipped += str(tmp)
    print "The last ten bits flipped" + "\n" + flipped 
    
    ctBinary = binary_ct[:-10] + flipped 
    print "Charlie's tampered cyphertext in binary:" + "\n" + ctBinary
    
    tampered_ct = binascii.unhexlify('%x' % (int(ctBinary, 2)))
    print repr("The tampered cyphertext after conversion:" + "\n" + tampered_ct)


def compare_intercepted(args):
    message = args.string.lower()
    pt = ""
    key = 3
    
    for i in message:
        pt += chr((((ord(i) - 97) - key) % 26) + 97)
    print "The  decrypted tampered message is: " + pt

if __name__ == "__main__":
    args = parser.parse_args()
    if str.isalpha(args.string) == False:
        raise ValueError('The string must be alphabetic characters')
    elif args.encrypt:
        encrypt_plaintext(args)
    elif args.decrypt:
        decrypt_cyphertext(args)
    elif args.charlie:
        decrypt_intercepted(args)
    elif args.difference:
        compare_intercepted(args)
    else:
        print "Error, please see usage or --help for assistance"
