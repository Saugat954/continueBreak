
# Break and continue in python

for i in range (12):
    if(i==10):
        print(" we are using continue so it skips i= 10 and continue to 11")
        continue

    print("5 x",i,"=", 5*i)

for num in range(5):
    if(num==3):
        print("this number is three it will not print because we are using continue")
        continue
    print(num)
print("loop has been ended")


# using break statemnt

name = "saugat"
for char in name:
    if(char=="u"):
        break
    #whole loop will be ended
    print(char)
print("loop has been ended because char(u) is true")

