s=raw_input("Enter the word \n")
c1=0
c2=0
c3=0
c4=0
v=0
for c in s:
	if(c=='?'):
		c1=c1+1
print c1
w=s.split()
for c in w:
	c2+=1
print c2
for c in s:
	if(c=="1" or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9' or c=='O' ):
		c3=c3+1
print c3
for c in s:
	if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
		v=v+1
	else:
		c4=c4+1
print c4

