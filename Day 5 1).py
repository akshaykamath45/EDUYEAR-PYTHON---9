#DAY 5 ASSIGNMENT 1
#PRINTING NUMBERS DIVISBLE BY BOTH 5 & 7,USING FOR LOOP FROM RANGE N TO M
n=int(input("Enter starting number :" ))
m=int(input("Enter ending number :"))
for num in  range(n,m):
    if num % 5==0 and num % 7==0:
        print(str(num)+" ",end="")
    else:
        pass
