s=raw_input("enter the string")
w=""
for i in s:
 if(i=='a' or i=='e' or i=='o' or i=='u' or i=='i'):
   continue
 else:
  w=w+i
print "after removing vowels",w
u=s.upper()
print "uppercase char",u
search=raw_input("enter the word to search")
tt=s.find(search)
if(tt==-1):
 print "the word is not there"
else:
 print " index value ",tt
t=raw_input(" substring to search")
ss=s.count(t)
print " occurences",ss


