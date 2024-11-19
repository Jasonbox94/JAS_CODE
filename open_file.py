#open file
data = []
with open('reviews.txt', 'r') as f:
    for row in f:
        data.append(row)
print(len(data))
