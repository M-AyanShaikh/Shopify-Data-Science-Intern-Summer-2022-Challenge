# Question 1

## Question 1.a
After examining the headers for each of the columns and the type of data that was present in their respective columns, I came to the conclusion that the AOV calculated was concluded by dividing the sum of the values in the "order_amount" column with the number of total orders (which was 5000). To confirm my prediction, I tested it out myself with the dataset and also ended up getting $3145.13. 

I believe a better way to calculate the average order value (AOV) of the data is by dividing the sum of the "order_amount" by that of the sum of "total_items". This approach makes sense, as there were some orders that were outliers (bulk purchases), which inflated the AOV, and since we're attempting to find the average price of a sneaker, it would make sense to compare it to the number of items rather than the number of orders.

I've written up a solution in Python, which can be accessed here.

## Question 1.b

I believe an appropriate metric for this dataset would be in dollars, and with the AOV = sum of order_amount / sum of total_items

## Question 1.c

The value of the AOC using my method is $357.92.

