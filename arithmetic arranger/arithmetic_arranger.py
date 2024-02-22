'''
  DISCLAIMER: The test enviroment doesn't work like it shoud and this code can't be tested properly. The other exercises are function all right. I've searched the solution in online forums but nothing worked.
'''

def arithmetic_arranger(problems, show = False):
    if len(problems) > 5:
        print("Error: Too many problems.")
        quit()
    problems_lenght = len(problems)

    #Lists to organize the output
    superior_numbers = []
    inferior_numbers = []
    simbols = []
    num_digits = []

    #Receive the math expression
    for expression in problems:

        #Break down into numbers and symbol
        items = expression.split()
        if items[1] != '+' and items[1] != '-':
            print("Error: Operator must be '+' or '-'.")
            quit()
        if not items[0].isnumeric() or not items[2].isnumeric():
            print("Error: Numbers must only contain digits.")
            quit()

        superior_numbers.append(items[0])
        simbols.append(items[1])
        inferior_numbers.append(items[2])
        lenght = 0

        #Determine the lenght of the highest number
        for number in items:
            len_number = len(number)
            if len_number > 4:
                print("Error: Numbers cannot be more than four digits")
                quit()
            if len_number > lenght:
                lenght = len_number
        num_digits.append(lenght + 2)
    
    #Print the first line with the first number of the expressions
    for i in range(problems_lenght):
        spaces = int(num_digits[i]) - len(superior_numbers[i])
        print(" " * spaces + superior_numbers[i]+ " " * 4, end='')
    print()
    
    #Print the second line with the simbol second number of the expressions
    for i in range(problems_lenght):
        spaces = int(num_digits[i]) - 1 - len(inferior_numbers[i])
        print(simbols[i] + " " * spaces + inferior_numbers[i] + " " * 4, end='')
    print()

    #Print the lines
    for i in range(problems_lenght):
        print("-" * int(num_digits[i]) + " " * 4, end='')
    print()

    #Print the results
    if show == True:
        for i in range(problems_lenght):
            if simbols[i] == '+':
                result = int(superior_numbers[i]) + int(inferior_numbers[i])
            elif simbols[i] == '-':
                result = int(superior_numbers[i]) - int(inferior_numbers[i])
            result = str(result)
            spaces = int(num_digits[i]) - len(result)
            print(" " * spaces + result + " " * 4, end='')
        print()