import decimal

def dec_sum(x):
	total = 0
	x = decimal.Decimal(x)
	precision = decimal.Context(prec=102)
	x = x.sqrt(precision)
	x = str(x)
	try:
		i = x.index(".")
		x = x[0:i]+x[i+1:len(x)]
		x = x[0:100]
		for dig in x:
			total += int(dig)
		return total
	except ValueError as e:
		return 0

root_sum = 0
for n in range(1, 101):
	root_sum += dec_sum(n)
print(root_sum)
