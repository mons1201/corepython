mons=input("enter your degree:")
mo=int(input("enter your percentage:"))
if(mons=='B.E'and mo>70):
    print("fist class")
elif(mons=='B.E'and mo>=50 and mo<=70):
    print("second class")
else:
    print("not eligible")