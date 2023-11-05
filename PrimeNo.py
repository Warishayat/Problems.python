#weather check the number is prime or not
while True:
    a=int(input("Enter the first number: "))
    if a%2==0:
        print("number is not prime: ")
    
    else:
        print(f"number is prime: {a} ")
        
    num=input("do you want to stay or leave(y/s)")
    if num.lower() !='y':
        break
    