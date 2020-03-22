import os # operation system
#读取档案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '商品' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, price])
	return products


#让使用者输入
def user_input(products):
	while True:
		name = input('Please enter products name: ')
		if name == 'q':
			break
		price = input('Please enter the price of the product: ')
		products.append([name, price])
	print(products)
	return products

#印出购买记录
def print_products(products):
	for p in products:
		print('Price for', p[0], 'is',p[1])

#写入档案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,价钱\n')
		for p in products :
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah! Found it.')
		products = read_file(filename)
	else:
		print('Doesnot exist.')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()