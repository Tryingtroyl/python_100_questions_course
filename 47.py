from string import ascii_lowercase

str='python'
result=[]
for i in ascii_lowercase:
    with open(f"files/{i}.txt",'r') as file:
        letter=file.read()
        if letter in list(str):
            result.append(letter)

print(result)