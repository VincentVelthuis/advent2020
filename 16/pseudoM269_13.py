x=0
y=1
z=1
print(x)
print(y)
while(z<15):
	f=x + y
	x=y
	y=f
	if (f%2 == 0):
		print(f)
	z += 1