# https://platform.stratascratch.com/coding/2004-number-of-comments-per-user-in-past-30-days?code_type=2
# Return the total number of comments received for each user in the 30-day period up to and including 2020-02-10. 
# Don't output users who haven't received any comment in the defined time period.

# <fb_comments_count>
# user_id				int64
# created_at			datetime64[ns]
# number_of_comments	int64

# import your libraries
import pandas as pd

# glimpse data
fb_comments_count.head()

# total num of comments between 2020-02-10
# and 30 days prior
(
    fb_comments_count[fb_comments_count['created_at']
        .between(pd.to_datetime('2020-02-10') - pd.Timedelta(days = 30), '2020-02-10')]
        .groupby('user_id')['number_of_comments']
        .sum()
        .reset_index()
)
