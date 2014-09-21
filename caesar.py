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
       help="Encrypt plaintext")
group.add_argument("-d", "--decrypt", action="store_true",
       help="Decrypt cyphertext" )
parser.add_argument("-s","--string", 
        help="String to be encrypted or decryped")


if __name__ == '__main__':
    args = parser.parse_args()
    if args.encrypt:
        encrypt_plaintext(args)
    elif args.decrypt:
        decrypt_plaintext(args)
    else:
        print "Error, please see usage or --help for assistance"
