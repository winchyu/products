products = [] # 建立一個清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':    # quit 離開
		break
	price = input('請輸入商品價格: ')
	# price 是字串，因為('請輸入商品價格: ')是字串
	price = int(price) 
	# 把字串price 轉換成 int 數字
	# 往下的price, 所有提到price 價格的部份，就是數字
	products.append([name, price])
print(products)

print('----------------------', '\n')

# 05
for p in products: # p 是products大清單裏的小清單 
	print(p)    # 印出每一個小清單

for p in products:
	print(p[0]) # 印出每一個小清單的第0格

for p in products:
	print(p[0], '的價格是', p[1])

print('----------------------', '\n')


with open('products-1.txt','w') as f:
	f.write('商品, 價格\n')
	for p in products:
		# f.write(p[0] + ',' + p[1] + '\n')
		f.write(p[0] + ',' + str(p[1]) + '\n')

print('----------------------', '\n')

with open('products-1.csv','w', encoding= 'utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		# f.write(p[0] + ',' + p[1] + '\n')
		f.write(p[0] + ',' + str(p[1]) + '\n')
		# 這裏是字串的加法的組合，
		# P[1]價格是數字	, 要轉成字串
		# str(p[1])	