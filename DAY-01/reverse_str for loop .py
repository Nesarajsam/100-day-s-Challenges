n = input("Enter the name: ")
b = len(n)
reverse_str = ""

for i in range(b - 1, -1, -1):
    reverse_str += n[i]

print(f"reverse_str: {reverse_str}")

