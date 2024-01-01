def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def bagi(a, b):
    return a / b

def kali(a, b):
    return a * b

def kalkulator():
    print("Pilihlah Sistem Opersi yang akan digunakan")
    print("1. tambah")
    print("2. kurang")
    print("3. bagi")
    print("4. kali")
    
    pilihan = input("apa sistem operasi yang anda pilih 1/2/3/4: ")
    angka1 = int(input("angka pertama: "))
    angka2 = int(input("angka kedua: "))
    
    if pilihan == '1':
        print(angka1, "+", angka2, "=", tambah(angka1, angka2))
    elif pilihan == '2':
        print(angka1, "-", angka2, "=", kurang(angka1, angka2))
    elif pilihan == '3':
        print(angka1, "/", angka2, "=", bagi(angka1, angka2))
    elif pilihan == '4':
        print(angka1, "*", angka2, "=", kali(angka1, angka2))
    else:
        print("invalid number")
while input("apakah anda mau melakukan tperhitungan y/n: ") == "y":      
    kalkulator()
        
        
    