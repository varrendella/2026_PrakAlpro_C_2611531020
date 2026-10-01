# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_1020 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1020 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1020 = tinggi_1020
    c_1020 = a_1020
    lebar_1020 = (2 * tinggi_1020) - 2

    for i_1020 in range(1, tinggi_1020 + 1):
        b_1020 = c_1020 + 1

        for j_1020 in range(1, lebar_1020 + 1):

            # Baris atas dan bawah
            if i_1020 == 1 or i_1020 == tinggi_1020:
                if j_1020 == 1 or j_1020 == lebar_1020:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_1020 == 1 or j_1020 == lebar_1020:
                    print("|", end="")
                elif j_1020 == c_1020:
                    print("<", end="")
                elif j_1020 == b_1020:
                    print(">", end="")
                elif j_1020 == (lebar_1020 - c_1020):
                    print("<", end="")
                elif j_1020 == (lebar_1020 - c_1020 + 1):
                    print(">", end="")
                elif b_1020 < j_1020 < (lebar_1020 - c_1020):
                    print(".", end="")
                else:
                    print(" ", end="")

        print()  # pindah baris setelah satu baris selesai

        # Logika asli Java (update nilai untuk baris berikutnya)
        a_1020 -= 2
        if a_1020 <= 0:
            c_1020 = (-a_1020) + 2
        else:
            c_1020 = a_1020                
            
    