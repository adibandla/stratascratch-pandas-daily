# https://platform.stratascratch.com/coding/2081-recommendation-system?code_type=2
# Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.

# Difficulty: Medium

# <users_friends>
# user_id		int64
# friend_id		int64

# <users_pages>
# user_id		int64
# page_id		int64

# import your libraries
import pandas as pd

# start writing code
users_friends.head()

# create table with pages that the users
# friends follow
friends_pages = users_friends.merge(
        users_pages,
        left_on = 'friend_id',
        right_on = 'user_id',
        how = 'inner',
        suffixes = ['_l', '_r']
        ) \
        [['user_id_l', 'page_id']] \
        .drop_duplicates()
    
# pages in the friends_pages
# not in users_pages grouped by user_id
friends_pages.merge(
        users_pages,
        left_on = ['user_id_l', 'page_id'],
        right_on = ['user_id', 'page_id'],
        how = 'left',
        ) \
    .query('user_id.isna()', engine = 'python') \
    .drop('user_id', axis = 1) \
    .rename(columns = {'user_id_l': 'user_id'})
