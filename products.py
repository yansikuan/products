products = []
while True:
	name = input('Please enter products name: ')
	if name == 'q':
		break
	price = input('Please enter the price of the product: ')
	p = []
	p.append(name)
	p.append(price)
	# equiv to p = [name,price]
	products.append(p)
print(products)