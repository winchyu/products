# 讀取檔案，除去標題
products = [] # 建立一個清單
# with open('products-2.csv', 'r', encoding= 'utf-8') as f:
# 	for line in f:
# 		s = line.strip().split(',')
# 		# split 切割完的結果是清單
# 		# 所以print(s) 出來就是清單
# 		print(s)

with open('products-2.csv', 'r', encoding= 'utf-8') as f:
	for line in f:
		if '商品, 價格' in line:
			continue # 繼續
			# 只能在迴圈，表繼續跳到下一迴
			# 不往下走，直接回到if 的下一迴
		name, price = line.strip().split(',')
		# split 切割完的結果是清單
		products.append([name, price])
print(products)


# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':    # quit 離開
		break
	price = input('請輸入商品價格: ')
	price = int(price) 
	products.append([name, price])
print(products)


# 印出所有購買紀錄
for p in products: 
	print(p)    

for p in products:
	print(p[0]) 

for p in products:
	print(p[0], '的價格是', p[1])


# 寫入檔案
with open('products-2.csv','w', encoding= 'utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')