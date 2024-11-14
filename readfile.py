#read file
data = []
with open('food.txt','r') as f:
    for row in f:
        data.append(row.strip())

        #print(row)
print(data)
#for txt in data:
#    print(txt)
