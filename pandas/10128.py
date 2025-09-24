# https://platform.stratascratch.com/coding/10128-count-the-number-of-movies-that-abigail-breslin-nominated-for-oscar?code_type=2
# Count the number of movies for which Abigail Breslin was nominated for an Oscar.

# <oscar_nominees>
# year				int64
# category			object
# nominee			object
# movie				object
# winner			bool
# id				int64

# import libraries
import pandas as pd

# glimpse data
oscar_nominees.head()

# num movies in which Abigail Breslin
# was nominated
oscar_nominees[oscar_nominees['nominee'] == 'Abigail Breslin']['id'].count()
