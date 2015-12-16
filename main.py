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

def decrypt_char(char, key) -> str:

     if char!=" " and key!=" ":
        pos = string.ascii_lowercase.index(char)-string.ascii_lowercase.index(key)
        pos += 1
        print(string.ascii_lowercase[pos])
        return string.ascii_lowercase[pos]
     else:
        return " "
