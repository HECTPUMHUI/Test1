fizz = int(input("fizz: "))
buzz = int(input("buzz: "))
num = int(input("num: "))
for i in range(1, num + 1):
    if i % fizz == 0 and i % buzz == 0:
        print("FB")
    elif i % fizz == 0:
        print("F")
    elif i % buzz == 0:
        print("B")
    else:
        print(i)

