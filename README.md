Caesar Cipher 
==============

This is a quick program that uses the Caesar Cipher.

In order to use simply download it and make it executable:

`sudo chmod +x caesarCipher.py `  
  

###Usage: 


```python
python caesarCipher.py --help
```
```python
python caesarCipher.py --h
```
```python
python caesarCipher.py -e test
```
```python
python caesarCipher.py -d test
```
```python
python caesarCipher.py -c whvw
```
```python
python caesarCipher.py -diff whvw
```

###Known Issues:

If you wanted to tamper with a ciphertext by running it through the 'decrypt_intercepted' 
function and then decrypt it using `decrypt_cyphertext` to see the letter shifts it can be
a pain to copy and paste it. 

Also the `decrypt_intercepted` takes the `string` argument, converts to binary with a 0b prefix.
We are decrypting and encrypting within the lower alphabet ASCII range. So when the 2nd to the
12th bit is flipped and then converted back it can produce an output that is not within the ASCII range. 

This can cause another issue if the tampered output is say ;, &, etc. This can cause issues with the command line. 
A workaround is to put the string you are passing in parenthesis. 


###Future Improvements:

I would like to add an argument for a custom key. This would require another propositional argument of type int.  

I would like to improve the command line use for -diff. It would be nice to run the `compare_intercepted` function 
without having to run the decrypt again. 

Breaking up the binary conversion into separate functions would make the program cleaner.

