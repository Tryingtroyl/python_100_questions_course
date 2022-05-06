from string import ascii_lowercase


with open('files/alpha.txt','w') as file:
    for i in ascii_lowercase:
        file.write(i+'\n')

