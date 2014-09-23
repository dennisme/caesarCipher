#!/usr/bin/python

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
       help="Encrypt Alice's plaintext for Bob")
group.add_argument("-d", "--decrypt", action="store_true",
       help="Decrypt Alice's cyphertext" )
group.add_argument("-c", "--charlie", action="store_true", 
        help="Charlie's intercepted tampered cyphertext")
group.add_argument("-diff", "--difference", action="store_true",
      help="Decrypting Charlie's modified cyphertext")
parser.add_argument("string",help="String to be encrypted or decryped")


def encrypt_plaintext(args):
    message = args.string.lower() 
    ct = ""
    key = 3
    for i in message:
        ct += chr((((ord(i) - 97) + key)%26) + 97)
    print "Alice's encrypted message is: " + ct 

def decrypt_cyphertext(args):
    message = args.string.lower()
    pt = ""
    key = 3
    for i in message:
        pt += chr((((ord(i) -97) - key)%26) + 97)
    print "Bob's decrypted message is: " + pt

def decrypt_intercepted(args):
    #ascii to binary 
    #flip 10 bits (I chose first 10)
    #encript then print it
    message = args.string.lower()
    pt = ""
    key = 3
    flipped = ""
    binary_ct = "0" + bin(int(binascii.hexlify(message), 16))[2:]
    #hex is base 16 so we are taking the message -> then to binary
    #then we trim off the 0b and add 
    #add on 0 so it is even/divisible by 8
    #print binary_ct
    for i in binary_ct[:10]:
        tmp = int(i)
        tmp ^= 1
        flipped += str(tmp)
    print flipped
def compare_intercepted(args):
    print "diff works"
    print args.string

if __name__ == "__main__":
    args = parser.parse_args()
    if args.encrypt:
        encrypt_plaintext(args)
    elif args.decrypt:
        decrypt_cyphertext(args)
    elif args.charlie:
        decrypt_intercepted(args)
    elif args.difference:
        compare_intercepted(args)
    else:
        print "Error, please see usage or --help for assistance"
