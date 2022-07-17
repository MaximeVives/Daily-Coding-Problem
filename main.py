data = [10, 3]

a = max(data)
b = min(data)

sum = 0
quotient = 0

while sum < a:
    if sum + b > a:
        break
    else:
        sum += b
        quotient += 1

print(f"quotient: {quotient}")
print(f"reste : {a - sum}")