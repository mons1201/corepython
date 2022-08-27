'''a={"aa","bb","cc","dd"}
print(a)
b={"aa","aa","cc","dd","ff"}
print(type(b))
print(len(b))
print(b)

#set constructor
c=set(("mm","nn",5,6,7))
print(c)
c.add("xx")
print(c)
c1={"ss","xx"}
c.update(c1)
print(c)
#interable
d={"yy","jj","hh",54}
d1=(1,2,3,4)
d.update(d1)
print(d)

f={1,2,3,"sam","pk"}
f.remove("sam")
f.discard(2)
print(f)'''
#pop method
s={"sam",3,4,5,6}
s1=s.pop()
print(s1)