d = dict(weather = "clima", earth = "terra", rain = "chuva")

def translate(input):
    if input in d.keys():
        return d[input]
    else:
        return "Could not find"

str=input()
print(translate(str))