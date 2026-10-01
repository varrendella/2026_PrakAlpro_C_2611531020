batas_1020 = int(input("Masukkan nilai batas: "))
for line in range(1, batas_1020 + 1):
    for j_1020 in range(-1 * line + batas_1020 + 1):
        print(".", end=" ")
    print(line)