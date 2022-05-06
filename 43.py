import string
with open("files/43.txt",'w') as file:
    for i,j in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(i+j+"\n")