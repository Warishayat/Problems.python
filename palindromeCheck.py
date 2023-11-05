while True:
    num1=input("Enter the number to check:")
    reverse=num1[-1::-1]  #here will check the in the reverse form the number is same:
    if num1==reverse:
        print("The number/string is palindrome: ")
    else:
        print("The number is not palindrome: ")
    Num=input('wana stay or go bake to the exit (y/s):')
    if Num!= 'y':
        break
    