## Que->8) WAP to find the sum of the digits of a user inputted number.
no = int(input("Enter no. : "))
sum = 0
rem = 0
for i in range(no):
     rem = no%10
     sum += rem
     no //= 10
print(sum)
