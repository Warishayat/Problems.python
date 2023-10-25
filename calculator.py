while True:
    print("WELCOME TO CACULATOR")
    number1=float(input("Enter the first number: "))
    number2=float(input("Enter the second number: "))
    userinput=str(input("What function do you want to perform : +,/,-,*  "))
    if  userinput == "+":
        p=number1+number2
        print(f"you addition result is {p}")
    #here we make a temoprary vriable with p who will store the result value of number 1 & 2.
    
    elif userinput=="/":
        d=number1/number2
        print(f"you division result is {d}")
    #here we make a temoprary vriable with d who will store the result value of number 1 & 2.
    
    elif userinput=="*":
        m=number1*number2;
        print(f"your multiplication resut is {m}")
    #here we make a temoprary vriable with m who will store the result value of number 1 & 2.
        
        
    elif userinput=="-":
        s=number1-number2;
        print(f"your multiplication resut is {s}")
     #here we make a temoprary vriable with S who will store the result value of number 1 & 2.
    else:
         print("you enterd some invalid option:")
         
    again=input("Do you want to continue  (y/n):")
    if again != "y":
        break;
    #here for to do the same thing again we make a variabe with "again" name which take input from the 
    #user that what opreation perform next?

    