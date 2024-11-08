n = int(input("Enter a non-negative integer: "))


for i in range(1, n + 1):
    factorial = 1
    
for j in range(1, i + 1):
        factorial *= j
    # Printing the factorial of each number
    print(f"{i}: {factorial}")
