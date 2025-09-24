# https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=2
# Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.

# <facebook_reactions>
# poster			int64
# friend			int64
# reaction			object
# date_day			int64
# post_id			int64

# <facebook_posts>
# post_id			int64
# poster			int64
# post_text			object
# post_keywords		object
# post_date			datetime64[ns]

# import libraries
import pandas as pd

# code
facebook_posts[
    facebook_posts['post_id'].isin(
        facebook_reactions[
            facebook_reactions['reaction'] == 'heart']['post_id'].unique()
            )
]
