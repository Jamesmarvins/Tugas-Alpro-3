try:
    sisi_1 = float(input("Masukkan sisi 1: "))
    sisi_2 = float(input("Masukkan sisi 2: "))
    sisi_3 = float(input("Masukkan sisi 3: "))

    if sisi_1 == sisi_2 == sisi_3:
        print("3 sisi sama")
    elif sisi_1 == sisi_2 or sisi_1 == sisi_3 or sisi_2 == sisi_3:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except ValueError:
    print("Masukkan harus berupa angka.")