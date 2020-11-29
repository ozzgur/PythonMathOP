def addNumbers(a, b): 
    print("Girdiğiniz iki sayının toplamı :", a + b) 
  
def subtractNumbers(a, b): 
    print("Girdiğiniz iki sayının farkı :", a - b) 
  
def multiplyNumbers(a, b): 
    print("Girdiğiniz iki sayının çarpımı :", a * b) 
  
def divideNumbers(a, b): 
    print("Girdiğiniz iki sayının bölümü :", a / b) 
  
def modulusNumbers(a, b): 
    print("Girdiğiniz iki sayının kalanı :", a % b) 

def factorialNumber(a):
    total = 1
    for i in range(a):
        total = total * (i + 1)
    print(f"Girdiğiniz sayının faktoriyeli : {total}")

   
        