import csv

# Opening CSV File
with open('data.csv') as csv_file:
    rows = csv.reader(csv_file, delimiter=",")
    data = []
    for row in rows:
        data.append(row)

# Creating two lists to append data of columns 3 and 4 to
order_amount_lst = []
total_items_lst = []

for item in data:
    order_amount_lst.append(item[3])

for item in data:
    total_items_lst.append(item[4])

# Pop headers of columns and create two int variables to add data to
order_amount_lst.pop(0)
total_items_lst.pop(0)
order_amount = 0
num_of_items = 0

# Loop through each item and add to variables
for item in range(len(order_amount_lst)):
    order_amount += int(order_amount_lst[item])

for item in range(len(total_items_lst)):
    num_of_items += int(total_items_lst[item])

# Print the AOV which is the order amount / the total number of items purchased
print(order_amount/num_of_items)
