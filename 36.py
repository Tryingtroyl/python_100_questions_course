with open('files/words1.txt', 'r') as file:
    str=file.read()
    print(len(list(str.split(' ')))) 