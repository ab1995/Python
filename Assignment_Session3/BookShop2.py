from functools import reduce

orders = [ [1, ("5464", 4, 10), ("8274",18,13), ("9744", 9, 45)],
	       [2, ("5464", 9, 10), ("9744", 9, 45)],
	       [3, ("5464", 9, 10), ("88112", 11, 25)],
           [4, ("8732", 1, 12), ("7733",1,19), ("88112", 1, 40)] ]


invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
invoice_totals = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], invoice_totals))
invoice_totals = list(map(lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), invoice_totals))
print(invoice_totals)