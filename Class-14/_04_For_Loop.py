num = int(input())
for value in range(1, 11):
    if value == 2:
        continue
    if value < 5:

        print(num, "X", value, "=", (num * value))
    else:
        break
