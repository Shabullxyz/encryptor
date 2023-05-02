The encriptador is a command-line program that allows you to encrypt and decrypt files using a key. The program uses the cryptography Python library to generate keys and encrypt/decrypt files.

Requirements
The encriptador requires Python 3 and the cryptography library. You can install the latter using pip:

Copy code
pip install cryptography
Usage
The encriptador is run from the command line with the following format:

css
Copy code
encriptador archivo [-g] [-k KEYFILE] [-d]
Where:

archivo: The file to be encrypted or decrypted.
-g: Option to generate a new key and save it to a file. If this option is used, the program will only generate a key and not encrypt or decrypt any file.
-k KEYFILE: Specifies the file where the key is saved or read from. By default, the file is .encriptador.key in the current directory.
-d: Option to decrypt the file instead of encrypting it.
Examples
Generate a new key:

~~~ 
encriptador archivo -g 
~~~
Encrypt a file:
~~~
encriptador archivo
~~~
Decrypt a file:

~~~
encriptador archivo.enc -d
~~~
