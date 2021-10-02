book={'書名':'海邊的卡夫卡','作者':'春上春樹'}
# print(book['書名'])
# print(book['作者'])

book['書名']='多拉a夢'
book['作者']='藤子不二雄'

# print(book['書名'])
# print(book['作者'])


for key in book.keys():
    print(key)
    print(book[key])

for value in book.values():
    print(value)

