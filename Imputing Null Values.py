# -*- coding: utf-8 -*-
"""
Created on Fri May 12 09:00:45 2023

@author: SumeetPatokar
"""

s1 = "hello" 
s2 = "world" 
print(s1 + " " + s2)

my_list = [1, 6, 3, 8, 2] 
print(min(my_list))

s = "hello world" 
s = s.replace("world", "python") 
print(s)

# Question 3
from datetime import datetime
date = datetime(1992, 8 , 26)
formatted_date = date.strftime("%Y %m")
print(formatted_date)

from datetime import datetime
date = datetime(1992, 8 , 26)
formatted_date = date.strftime("%Y %d")
print(formatted_date)

from datetime import datetime
date = datetime(1992, 8 , 26)
formatted_date = date.strftime("%B %Y")
print(formatted_date)


pip install scikit-learn
import pandas as pd
from sklearn.impute import *
# sklearn.impute for imputing missing values in a dataset


import pandas as pd
from sklearn.impute import SimpleImputer
 

df = pd.read_csv(r"C:\Users\SumeetPatokar\Desktop\Data Science\360digitmg\DataSets\Data sets/Data.csv")
missing_values = data.isnull().sum()
print(missing_values)
#imputer = SimpleImputer(strategy='mean')
imr = SimpleImputer(missing_values='NaN', strategy='mean')


# 4)	For the dataset “Indian_cities”, 
# a)	Find out top 10 states in female-male sex ratio

import pandas as pd
data = pd.read_csv(r"C:\Users\SumeetPatokar\Desktop\Data Science\360digitmg\DataSets\Data sets\Indian_cities.csv")
state_ratio = data.groupby("state_name")["sex_ratio"].mean()

sorted_states = state_ratio.sort_values(ascending=False)
top_10_states = sorted_states.head(10)
print(top_10_states)

# b)	Find out top 10 cities in total number of graduates
import pandas as pd
data = pd.read_csv(r"C:\Users\SumeetPatokar\Desktop\Data Science\360digitmg\DataSets\Data sets\Indian_cities.csv")

graduates = data.groupby("name_of_city")["total_graduates"].mean()

sorted_graduates = graduates.sort_values(ascending=False)
top_10_cities = sorted_graduates.head(10)
print(top_10_cities)

# c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.
import pandas as pd
data = pd.read_csv(r"C:\Users\SumeetPatokar\Desktop\Data Science\360digitmg\DataSets\Data sets\Indian_cities.csv")

literacy = data.groupby("name_of_city")["effective_literacy_rate_total"].mean()
sorted_literacy = literacy.sort_values(ascending=False)
top_10_cities_literacy = sorted_literacy.head(10)
print(top_10_cities_literacy)

# 5)	 For the data set “Indian_cities”
# a)	Construct histogram on literates_total and comment about the inferences
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dir(pd)
literates = pd.read_csv(r"C:\Users\SumeetPatokar\Desktop\Data Science\360digitmg\DataSets\Data sets\Indian_cities.csv")
plt.hist(literates.literates_total)
plt.xlabel("Literates")
plt.ylabel("Occurence")

plt.title("Literates Total")


# b)	Construct scatter  plot between  male graduates and female graduates



my_list = [4, 1, 6, 2, 7, 3]
my_list.sort()
print(my_list)

x = 3.14
print(type(x))

my_list = []
if not my_list:
    print(""List is empty"")










