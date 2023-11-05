import datetime
year=datetime.datetime.now().year
name=input("Enter your Name:")
age=int(input("Enter your Age:"))
After_100_year=year+(100-age)
message="Hi"+name+"you will turn 100 year at the year"+str(year)+""
print(message)