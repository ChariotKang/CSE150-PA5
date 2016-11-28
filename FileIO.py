f = open("prob_east.txt")
a = []
for line in f:
	a.append(line)
	print (line.split())
print (a)
f.close()