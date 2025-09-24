# https://platform.stratascratch.com/coding/10308-salaries-differences/solutions?code_type=2
# Calculates the difference between the highest salaries in the marketing and engineering departments. Output just the absolute difference in salaries.

# <db_employee>
# id			int64
# first_name	object
# last_name		object
# salary		int64
# department_id	int64

# <db_dept>
# id			int64
# department	object

# import libraries
import pandas as pd

# merge tables
merged_df = db_employee.merge(
    db_dept[db_dept['department'].isin(['engineering', 'marketing'])],
    left_on = 'department_id',
    right_on = 'id',
    suffixes = ['_engg', '_mark']
    )

# abs difference in salaries    
abs(
    merged_df[merged_df['department'] == 'engineering']['salary'].max() -
    merged_df[merged_df['department'] != 'engineering']['salary'].max()
    )
