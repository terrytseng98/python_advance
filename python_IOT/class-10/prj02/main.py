import json

d = {}
n = int(input("number?"))
for i in range(n):
    print(f'第{i}個元素')
    k = input("請輸入名稱")
    v = input("請輸入編號")
    d[k] = v
    print(d)
p = input("輸入想刪除的元素")
d.pop(p)
print(d)
json_str = json.dumps(d)
d = json.loads(json_str)
print(d)
