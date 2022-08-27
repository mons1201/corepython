file=open("sasifirstfile.txt","w")
print(file.mode)
print(file.closed)
print(file.name)
file.close()
print(file.closed)


file=open("sasiseconndfile.txt","a")
file.write(input("tell us now content to be written in file: "))
file.close()
print("content written in",file.name)



