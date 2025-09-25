# https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=2
# Find the customers with the highest daily total order cost between 2019-02-01 and 2019-05-01. If a customer had more than one order on a certain day, 
# sum the order costs on a daily basis. Output each customer's first name, total cost of their items, and the date.

# For simplicity, you can assume that every first name in the dataset is unique.
# Difficulty: Medium

# <customers>
# id				int64
# first_name		object
# last_name			object
# city				object
# address			object
# phone_number		object

# <orders>
# id				int64
# cust_id			int64
# order_date		datetime64[ns]
# order_details		object
# total_order_cost	int64

# import your libraries
import pandas as pd

# glimse data
customers.head()

# merge tables and filter dates
customers.merge(
    orders[orders['order_date'].between('2019-02-01', '2019-05-01')],
    left_on = 'id',
    right_on = 'cust_id'
    ) \
    .groupby(['first_name', 'order_date'])['total_order_cost'] \
    .sum() \
    .reset_index() \
    .groupby('order_date') \
    .apply(lambda df: df[df['total_order_cost'] == df['total_order_cost'].max()]) \
    .reset_index(drop=True)

# alternate solution 
customers.merge(
    orders[orders['order_date'].between('2019-02-01', '2019-05-01')] \
    left_on = 'id',
    right_on = 'cust_id'
    ) \
    .groupby(['first_name', 'order_date'], as_index = False)['total_order_cost'] \
    .sum() \
    .assign(max_cost_per_date = lambda df: df.groupby('order_date')['total_order_cost'].transform('max')) \
    .query('total_order_cost == max_cost_per_date', engine = 'python') \
    [['first_name', 'order_date', 'total_order_cost']]
