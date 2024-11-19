#open file
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for row in f:
        count += 1
        data.append(row)
        if count % 100000 == 0: 
            print(len(data))
            print(row)
