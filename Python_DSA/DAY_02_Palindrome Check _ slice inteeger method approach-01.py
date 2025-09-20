n=int(input("Enteer the value:"))
a=str(n)
b=a[::-1]
if n==int(b):
    print("palindrome")
else:
    print("not palindrome")
