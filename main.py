import string

def crypt_char(char, key) -> str:

    if char!=" " and key!=" ":
        pos = string.ascii_lowercase.index(char)+string.ascii_lowercase.index(key)
        if pos > len(string.ascii_lowercase)-1:
            pos = pos-len(string.ascii_lowercase)
            #print(char)
            #print(string.ascii_lowercase[pos])
        return string.ascii_lowercase[pos]
    else:
        return " "

def crypt_vigenere(text, key) -> str:

    i = 0
    crypt = ""
    for a in text:

        if i > len(key)-1:i = 0

        #print(a,':',key[i])
        crChar = crypt_char(a, key[i])
        crypt += crChar
        if crChar==" ":i -= 1
        i += 1
    return crypt
