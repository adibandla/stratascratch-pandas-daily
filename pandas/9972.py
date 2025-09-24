# https://platform.stratascratch.com/coding/9972-find-the-base-pay-for-police-captains?code_type=2
# Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.

# <sf_public_salaries>
# id				int64
# employeename		object
# jobtitle			object
# basepay			float64
# overtimepay		float64
# otherpay			float64
# benefits			float64
# totalpay			float64
# totalpaybenefits	float64
# year				int64
# notes				datetime64[ns]
# agency			object
# status			object

# import your libraries
import pandas as pd

# glimpse data
sf_public_salaries.head()

# base pay of employee captains
(
    sf_public_salaries[sf_public_salaries['jobtitle']
        .str.contains('POLICE|CAPTAIN', case = False)]
	[['employeename', 'basepay']]
)
