with open("words2.txt",'r') as file:
    str=file.read()
    print(len(list(str.replace(',', ' ').split(' '))))