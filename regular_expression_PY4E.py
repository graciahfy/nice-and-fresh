import re
fh = open("regex_sum_678083.txt")

m = []
a = 0
c = 0
for line in fh: 
	t = line.split()
	for num in t: 
		try: 
			k = int(num)
			a = a + k
			c += 1
		except: 
			h = re.findall('\d', num) 
			if len(h) > 0: 
				for chac in h: 
					another_num = int(chac)
					a = a + another_num
					c += 1
				
print(a, c)
				
