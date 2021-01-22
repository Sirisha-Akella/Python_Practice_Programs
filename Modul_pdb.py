#import pdb

def add_modul(x,y):
    sum1 = x + y
    return sum1

if __name__== "__main__":
    num1 = input("Enter the first number")
    num2 = input("Enter the second number")
  #  pdb.set_trace()
    result = add_modul(num1, num2)
    print(result)

