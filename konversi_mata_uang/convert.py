def convert(before, after, total):
    if before == "dolar" and after == "rupiah":
        result = total * 15000
    elif before == "yen" and after == "rupiah":
        result = total * 13000
    else :
        result = print("sorry your currency undifine!!!")
    return result
def mulai():  
    before = input("Mata Uang Yang Akan di Konversi: ")
    after = input("Mata Uang Konversi: ")
    total = int(input("Jumlah Uang Yang Akan Dikonversi: "))
    final = convert(before, after, total)

    print("Jumlah uang setelah di konversi:", final)

while input("apakah anda mau mengkonversi mata uang y/n: ") == "y":
    mulai()
    