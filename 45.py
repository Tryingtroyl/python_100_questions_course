from string import ascii_lowercase

for i in ascii_lowercase:
    with open(f"{i}.txt",'w') as file:
        file.write(i)