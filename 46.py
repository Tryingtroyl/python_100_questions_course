from string import ascii_lowercase
result=[]
for i in ascii_lowercase:
    with open(f"{i}.txt",'r') as file:
        result.append(file.read())
print(result)