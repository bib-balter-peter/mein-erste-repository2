print("Ungerade  |  Gerade")
print("---------------------")

for num in range(1, 10000000):
    if num % 2 == 1:

        print(f"{num:^9} |", end=" ")
    else:

        print(f"{num:^7} |", end=" ")

    if num % 2 == 0:
        print()
