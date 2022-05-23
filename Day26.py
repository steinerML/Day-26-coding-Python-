#Small program that returns all ODD numbers inside a given range.

numb = int(input("Enter the maximum of the range (x). i.e: 1-x :"))

for i in range(numb+1):
    if i % 2 != 0:
        print(i, "Odd")
    else:
        print(i, "//This is an even number//")