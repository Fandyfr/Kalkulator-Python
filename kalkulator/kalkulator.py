import os
import time
os.system('CLS')
time.sleep(5)

print(" APP BUATAN FANDY FATHURROHMAN")
print("")
print("DIKEMBANGKAN MELALUI BAHASA PYTHON")
print("")
print("JANGAN LUPA FOLLOW INSTAGRAM SAYA: Fndy.Fr")

time.sleep(10)


os.system('CLS')

def calculator():
    while True:
        print("Enter '+' Untuk Menambahkan")
        print("Enter '-' Untuk Mengurangi")
        print("Enter '*' Untuk Mengkali")
        print("Enter '/' Untuk Membagi")
        print("Enter 'quit' Untuk keluar dari App")

        user_input = input(": ")
        if user_input == "quit":
            break
        elif user_input in ["+", "-", "*", "/"]:
            num1 = float(input("Angka Pertama: "))
            num2 = float(input("Angka Kedua: "))

        if user_input == "+":
            result = num1 + num2
            print (num1, "+", num2, "=", result)

        elif user_input == "-":
            result = num1 - num2
            print (num1, "-", num2, "=", result)

        elif user_input == "*":
            result = num1 * num2
            print (num1, "*", num2, "=", result)

        elif user_input == "/":
            result = num1 / num2
            print (num1, "/", num2, "=", result)
    else:
        print("Anda salah memasukan sebuah angka")
        print("")
        print("Coba Lagi!!!")
        os.system('CLS')
        

calculator()
            