#voter id apply
nationality=input("enter the nationality:")
age=int(input("enter the age:"))
if(nationality=="indian"):
    print("you are selected indian")
    if(age>=18):
        print("you are apply for voter id")
    else:
        print("you ae not apply for voter id")
else:
     print("you are not a indian")

