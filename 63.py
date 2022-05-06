from time import sleep
i=0
for t in range(4):
    print("hello")
    i=i+1
    if t!=3:
        sleep(i)
print("End of Loop")