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

for p in products:
	print('Price for', p[0], 'is',p[1])

with open('Products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,价钱\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')