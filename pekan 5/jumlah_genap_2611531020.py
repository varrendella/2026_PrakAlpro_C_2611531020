ulang_1020= int(input("Masukkan nilai batas: "))

jumlah_1020 = 0
for i_1020 in range(1, ulang_1020 + 1):
    if i_1020 % 2 == 0:
        print(i_1020, end=" ")
        jumlah_1020 = jumlah_1020 + i_1020

    if i_1020 < ulang_1020:
        print("+", end=" ")
    else:
        print("=", jumlah_1020, end=" ")

print()
print("jumlah =", jumlah_1020)