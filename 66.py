d = dict(weather = "clima", earth = "terra", rain = "chuva")

def translate(input):
    return d[input]

str=input()
print(translate(str))