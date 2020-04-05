# GitHub 建立專案
# 基本程式碼
# 二維清單介紹
# 寫進程式碼
# 練習存取二維清單
# 建立版本上傳
# for loop 搞清楚每個東西是什麼
# 建立版本上傳
# 01
products = [] # 建立一個清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':    # quit 離開
		break
	products.append(name) 
	# 把輸入的商品name, 加入products 清單裏
print(products)

print('----------------------', '\n')

# 02
products = [] # 建立一個清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':    # quit 離開
		break
	price = input('請輸入商品價格: ')
	# 如果輸入q, 就不用問價格, 所以放在break 後面
	# 有商品名，又有價格, 做二維清單，清單中還有清單
	p = []
	p.append(name)
	p.append(price)
	products.append(p) 
	# 把輸入的商品name, 加入products 清單裏
print(products)

print('----------------------', '\n')

# products[0][0] 
#  第一[0]是大清單的第一個，第二個[0]是小清單的第一個
# products[1][1] 
#  第一[1]是大清單的第二個，第二個[1]是小清單的第二個


print('----------------------', '\n')


# 03
products = [] # 建立一個清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':    # quit 離開
		break
	price = input('請輸入商品價格: ')
	# 如果輸入q, 就不用問價格, 所以放在break 後面
	# 有商品名，又有價格, 做二維清單，清單中還有清單
	# p = []
	# p.append(name)
	# p.append(price), 可簡捷成:
	p = [name, price]
	products.append(p) 
	# 把輸入的商品name, 加入products 清單裏
print(products)

print('----------------------', '\n')

# 04
products = [] # 建立一個清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':    # quit 離開
		break
	price = input('請輸入商品價格: ')
	# p = [name, price]
	# products.append(p) 
	# 可簡捷成:
	products.append([name, price])
	# 把輸入的商品name, 加入products 清單裏
print(products)

print('----------------------', '\n')

# 05
for p in products: # p 是products大清單裏的小清單 
	print(p)    # 印出每一個小清單

for p in products:
	print(p[0]) # 印出每一個小清單的第0格

for p in products:
	print(p[0], '的價格是', p[1])