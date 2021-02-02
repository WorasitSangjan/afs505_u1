def cal(a, b):
    print(f"Comnibe {a} and {b}: {round(a+b, 2)}")
    print(f"Subtract {a} from {b}: {round(a-b, 2)}")
    print(f"Multiply {a} and {b}: {round(a*b, 2)}")
    print(f"Divide {a} by {b}: {round(a/b, 2)}\n")

print("\nPut number in 'cal' function")
cal(6, 3)

print("Set variables for the input in 'cal' function")
a = 10
b = 15
cal(a, b)

print("Put math in 'cal' function")
cal(10+34, 70/5)

print("Put any number for calculation")
a = input("a: ")
b = input("b: ")
cal(float(a), float(b))
