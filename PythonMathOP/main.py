import random
import functions 

a = random.randint(1,100)
devam = True

while devam:
    b = int(input("Bir sayı giriniz: "))
    if(a > b):
        print("Küçük bir sayı girdiniz")
    elif(b > a):
        print("Büyük bir sayı girdiniz")
    elif(b == a):
        print("Tebrikler kazandınız")
        devam = False
        break




#sayi = int(input("Bir sayı giriniz: "))
#sayi2 = int(input("Bir sayı daha giriniz: "))
#functions.addNumbers(sayi,sayi2)
#functions.divideNumbers(sayi,sayi2)
#functions.multiplyNumbers(sayi,sayi2)
#functions.subtractNumbers(sayi,sayi2)
#functions.modulusNumbers(sayi,sayi2)
#functions.factorialNumber(sayi)  
#functions.factorialNumber(sayi2)