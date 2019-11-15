from pandas import DataFrame

import pandas as pd
import csv

# Reading through csv file in read-text mode 'rt'
with open('pima-indians-diabetes.csv', 'rt') as f:
    reader = csv.reader(f)
    # Storing CSV file in a list of dictionary (list of key:values)
    mylist = list(reader)

# Using DataFrame which is a data structure in pandas (DataFrame creates structure like relational databases)
frame = DataFrame(mylist)

print(frame)
print("Printing frame[0] entry: ")
print(frame[0])

# frame['tz'][:10] Retrieves # column 'tz' with 10 first rows of it
# frame['tz'].value_counts() # Counts number of appearances of certain value in 'tz' column
# clean_tz = frame['tz'].fillna('Missing') # fillna() function fills in NA fields with our string
# clean_tz[clean_tz == ''] = 'Unknown'
