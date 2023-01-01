file = open("matrixPrime.csv", "a")
max = 20000
for num in range(max):
    count = 0
    for x in range(max):
        for y in range(max):
            if (x * y) % max == num:
                count += 1
    print(str(num) + "," + str(count))
    file.write(str(num) + "," + str(count) + "\n")
