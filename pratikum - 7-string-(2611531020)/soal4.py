phone = input("Masukkan nomor HP: ")

masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]

print("Nomor HP setelah disamarkan:", masked)