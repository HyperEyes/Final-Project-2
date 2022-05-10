# The job of this program is to use the strong password you have made from the first program to encrypt it.
# After running the program, you notice two lines, the first line is a long string of random numbers and letters--that is your encrypted pass, the next line is 
# your password decrypted.

from cryptography.fernet import Fernet

keygen = Fernet.generate_key()
        # generates a random key
        # same key won't repeat
        # same key must be used to encrpyt/decrypt

encrypter = Fernet(keygen)
        # this is what hides the key

pwe = input("Enter the password here: ")
        # saves our input

pwa = bytes(pwe, "utf8")
        # converting our input into bytes

prec = encrypter.encrypt(pwa)
        # where our input gets encrypted

decryptString = encrypter.decrypt(prec)

print(prec)
            # where our strong pass gets encoded
print(decryptString)
            # where our strong pass gets decoded

