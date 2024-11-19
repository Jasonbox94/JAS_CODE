#open file
data = []
row_count = 0
row_len_sum = 0
with open('reviews.txt', 'r') as f:
    for row in f:
        row_count += 1
        row_len_sum += len(row)
        data.append(row)
        
print(row_count)
print(row_len_sum / row_count)
