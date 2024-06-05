from art3 import logo
#Calculator
def add(n1, n2):
      return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide
  }


def calculator():
  print(logo)
      
  number1 = float(input("What is the first number? "))
  for symbol in operations: #loop trough operations
    print(symbol)
    
  go_again = True

  while go_again:

    oop_symb = input("pick an operation ")
    number2 = float(input("whats the second number? "))
    calc_function = operations[oop_symb]
    answer = calc_function (number1 , number2)

    print(f"{number1} {oop_symb} {number2} Your answer is  {answer}")
    
    
    if input(f"type y to continue or n to start again ") == "y":
      number1 = answer
      
    else:
      go_again = False 
      calculator() 
      
calculator()
          

    