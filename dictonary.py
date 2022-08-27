'''a={"name":"aa","age":23,"name":"bb"}
print(a)
print(a["age"])
print(len(a))
#methods 1get 2 keys 3 value 4add
b={"name":"jj","age":32,"frds":["sam","ip","mons"]}
print(b)
print(b["age"])
c=b.get("name")
print(c)
c=b.keys()
print(c)
b["bike"]="yy"
print(b)
c=b.values()
print(c)
b.update({"name":"rr"})
print(b)'''
#remove
x={"name":"mm","age":23,"game":"chess","frds":["sam","ip","anu"]}
print(x)
x.pop("name")
x.popitem()
print(x)
del x["age"]
print(x)
x.clear()
print(x)