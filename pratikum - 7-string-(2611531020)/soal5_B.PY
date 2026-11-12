nim = input ("masukan NIM: ")

if len(nim) ==10 and nim.isdigit():
    print(f"valid, intake year: 20(nim[:2])")
else:
    print("invalid NIM")