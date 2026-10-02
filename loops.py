list1 = [1, 2, 3, 4, 5]

for item in list1:
    print(item)


i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
        print(i)
    if i == 4:
        break
else:
    print("i is now larger than 5")
