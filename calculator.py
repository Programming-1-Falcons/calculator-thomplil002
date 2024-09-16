while True:
    equation_type = input("which of the following do you want to perform? addition, subtraction, division, multiplication, or exponent: ")
    

    if(equation_type) == ("addition"):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))

        print( num1, "+", num2, "=", str(int(num1 + num2)))


    elif(equation_type) == ("subtraction"):
        num1 = int(input ("Enter number 1:"))
        num2 = int(input ("Enter number 2:"))

        print( num1, "+", num2, "=",  str(int(num1 - num2)))


    elif(equation_type) == ("division"):
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        while denominator == (0):
            print("denominator cannot equal 0")
            denominator = int(input("Enter denominator: "))
    
        answer = float(numerator/denominator)
        true_answer = round(answer, 3 )
        print( numerator, "/", denominator, "=", str(true_answer))   

    elif(equation_type) == ("multiplication"):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))

        print ( num1, "*", num2 , "=" , str(int(num1 * num2 )))
    
    elif(equation_type) == ("exponent"):
        base_num = int(input("Enter base number: "))
        power = int(input("Enter power: "))

        print( base_num , "**", power , " = " , ( base_num ** power ))
    
    else:
        print("Invalid equation type")


    
    



    



