from string import ascii_lowercase

for i in ascii_lowercase:
    with open(f"files/{i}.txt",'w') as file:
        file.write(i)