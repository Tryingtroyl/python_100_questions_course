import string
letters=string.ascii_lowercase+" "
with open("files/44.txt",'w') as file:
    for i,j,k in zip(letters[0::3], letters[1::3], letters[2::3]):
        file.write(i+j+k+"\n")