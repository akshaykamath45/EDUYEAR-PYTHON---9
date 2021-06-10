#DAY 2 ASSIGNMENT

#TAKING VARIABLE FROM DIFFERENT DATA TYPES
name="Akshay Kamath" #string 
age=18               #int
per=91.33            #float
std=12               #int
div='A'              #char
print(name,age,per,std,div,sep='\n')


#FORMATTING

#METHOD 1
st="My name is {}.My age is {}.I am studying in {} std.".format(name,age,std)
print(st)


#METHOD 2
st=f"My name is {name}.My age is {18}.I am studying in{std} std."
print(st)


#DATA TYPE CONVERSION
print(type(age),age)
print(type(per),per)
age=float(per)
print(type(age),age)

