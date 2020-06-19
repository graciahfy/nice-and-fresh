a = 999
b = 999
k = a * b
while b > 99:
	k = a * b
	print(k)
	l = str(k)
	print(l)
	m = list(l)
	print(m)
	m.reverse()
	print(m)
	if m == list(l) is True:
		print(k)
		break
	else:
		b = b - 1

print('done')
