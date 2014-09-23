#!/usr/bin/python

"""
Matthew Dennison
NCS 541
Assignment 1

"""
import argparse

parser = argparse.ArgumentParser(description="Caesar Cipher")
group = parser.add_mutually_exclusive_group()
group.add_argument("-e", "--encrypt", action="store_true",
       help="Encrypt Alice's plaintext for Bob")
group.add_argument("-d", "--decrypt", action="store_true",
       help="Decrypt Alice's cyphertext" )
group.add_argument("-c", "--charlie", action="store_true", 
        help="Charlie's intercepted cyphertext")
group.add_argument("-diff", "--difference", action="store_true",
      help="Decrypting Charlie's modified cyphertext")
parser.add_argument("-s","--string", 
        help="String to be encrypted or decryped")


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
    print "charlie works"
    print args.string

def compare_intercepted(args):
    print "diff works"
    print args.string

if __name__ == '__main__':
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
