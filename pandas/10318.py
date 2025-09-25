# https://platform.stratascratch.com/coding/10318-new-products?code_type=2
# Calculate the net change in the number of products launched by companies in 2020 compared to 2019. Your output should include the company names and the net difference.
# (Net difference = Number of products launched in 2020 - The number launched in 2019.)
# Difficulty: Medium

# <car_launches>
# year			object
# company_name	object
# product_name	object

# import your libraries
import pandas as pd

# preview the data
car_launches.head()

# number of products launched in 2020
num_products_2020 = (
    car_launches[car_launches['year'] == 2020]
    .groupby('company_name', as_index=False)['product_name']
    .count()
    .rename(columns={'product_name': '2020_count'})
)

# number of products launched in 2019
num_products_2019 = (
    car_launches[car_launches['year'] == 2019]
    .groupby('company_name', as_index=False)['product_name']
    .count()
    .rename(columns={'product_name': '2019_count'})
)

# merge the two DataFrames and calculate net difference
num_products_by_year = (
    num_products_2020
    .merge(
        num_products_2019,
        on = 'company_name',
        how = 'inner'
    )
    .assign(
        net_difference = lambda df_: df_['2020_count'] - df_['2019_count']
    )[['company_name', 'net_difference']]
)

# concise solution
(
    car_launches
    .groupby(['company_name', 'year'])['product_name']
    .count()
    # here unstack pivots index or multiindex columns
    .unstack(level = 'year', fill_value= 0)
    # use the lambda function to refer to the internal df returned
    .assign(net_difference = lambda df: df[2020] - df[2019])
    .reset_index()
    [['company_name', 'net_difference']]
)
