# https://platform.stratascratch.com/coding/10026-find-all-wineries-which-produce-wines-by-possessing-aromas-of-plum-cherry-rose-or-hazelnut?code_type=2
# Find wineries producing wines with aromas of plum, cherry, rose, or hazelnut (singular form only). To make things simpler, exclude any wine descriptions that contain the plural forms (ex. cherries).

# <winemag_p1>
# id			int64
# country		object
# description	object
# designation	object
# points		int64
# price			float64
# province		object
# region_1		object
# region_2		object
# variety		object
# winery		object

# import your libraries
import pandas as pd

# glimpse data
winemag_p1.head()

# description contains plum, rose, cherry or hazelnut
# but does not contain plural forms
winemag_p1[
    (
        winemag_p1['description']
        .str.lower()
        .str.contains(r'\b(cherry|rose|hazelnet|plum)\b')
    )
    & ~(
        winemag_p1['description']
        .str.lower()
        .str.contains(r'\b(cherries|roses|hazelnets|plums)\b')
    )
]['winery'].drop_duplicates()
