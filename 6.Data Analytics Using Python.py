
# Python Packages for Data Analysis

# numpy

import numpy as np

# A list of elements in variable 'x'

x = [10, 21, 3, 14, 15, 16]
print(x)
print(type(x))

# how to multiply the list values with 2
print(x * 2) # values of the list are repeated

# Numpy array will help access the values
y = np.array(x)
print(y)

print(type(y))

print(y * 2)

y > 10, y[y > 10]

from numpy import random

x = random.randint(3, 9)

print(x)

### Memory savers

# numpy arrays share the memory instead of allocating seperate memory

a = np.arange(10)
print(a)

b = a[::2]
print(b)

print(np.shares_memory(a, b)) # check whether a and b shares memory
a, b

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0, 1])
print(arr[0, 2])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:4]) # Slice elements from the begining to index 4 (not included)


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:6:2]) # Slice elements from the begining to index 1 to index 5


### Masking arrays

a = np.arange(10)
print(a)

mask = (a%2 == 0) # masking for even numbers
print(mask)
a[mask]

### numpy matrices

import numpy as np

# Numpy matrics 

a = np.matrix('1 2; 3 4')
print(a)

b = np.matrix([[1, 2], [3, 4]])
print(b)

### numpy broadcasting

# numpy broadcasting helps when working on different sized arrays

a = np.arange(0, 40, 10)
print(a)

b = np.array([0, 1, 2])
print(b)

a, a.shape, b, b.shape

a = a[:, np.newaxis] # adds one extra axis
a.shape

print(a)
print('********')
print(b, '\n')
print('*********')
a + b  # addition takes place between different dimensions

# Data Structures

## Arrays/Vectors

from array import *

array1 = array('i', [10, 20, 30, 40, 50])

for x in array1:
    print(x)

help(array)

# insert operation 
from array import *

array1 = array('i', [10, 20, 30, 40, 50])

array1.insert(1, 60) # inserting the data at specified location

for x in array1:
    print(x)

# Deletion operation 
from array import *

array1 = array('i', [10, 20, 30, 40, 50])

array1.remove(40) # Deleting data we want

for x in array1:
    print(x)

# Updat operation
from array import *

array1 = array('i', [10, 20, 30, 40, 50])

array1[2] = 80 # Updating

for x in array1:
    print(x)

## 2D Arrays

# Accessing values in a Two Dimensional Array.
# The data elemnts in two dimensional arrays can be accessed using two indices.
# One index referring to the main or parent array and another index referring tothe position of the data element in the inner array.
# If we mention only one index then the entire inner array is printed for that index position.

from array import *

T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]] # 2D array

print(T[0])

print(T[1][2])

# Inserting Values in Two Dimensional Array
from array import *
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
print(T)

T.insert(2, [0, 5, 11, 13, 6]) # inserting at index=2

T

# Updating Values in Two Dimensional Array
from array import *

T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
print(T)

T[2] = [11, 9] # updating element (row) at index=2
T[0][3] = 7 # updating element in first row, 4th column
T

# Deleting the Values in Two Dimensional Array
from array import *
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
print(T)

del T[3] # deleting at index=3
T

## Matrix
# Matrix is a special case of two dimensional array where each data element is of strictly same size. So every matrix is also a two dimensional array but not vice versa. Matrices are very important data structures for many mathematical and scientific calculations.

# Matrix Example
from numpy import * 
a = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])
    
m = reshape(a, (7, 5)) # dimensions of matrix aka rows*columns
print(m)

# Accessing Values in a Matrix
from numpy import * 
m = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])
    
# Print data for Wednesday
print(m[2])

# Print data for Friday evening
print(m[4][3])

m

# Adding the data
from numpy import * 
m = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])
print(m, '\n')
m_r = append(m, [['Avg', 12, 15, 13, 11]], 0) # adding by using append at the end .(0 -- row)
m_c = insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 0) # adding by using insert at required location .(1 -- column)

print(m_r)
print('***********')

# Delete from matrix
from numpy import * 
m = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])

print(m) # original matrix
print('********************')
    
n1 = delete(m, [2], 0) # deleting row at index = 2
print(n1)
print('***********')
n2 = delete(m, [2], 1) # deleting column at index = 2
n2

import numpy as np
z = np.diag(1 + np.arange(4))
print(z)
type(z)

z = np.zeros(10)
print(z)
z[4] = 1
print(z)

# Create a random vector of size 30 and find the mean value
z = np.random.random(30)
print(z)
m = z.mean()
print(m)

# Reverse a vector (first element becomes last)
z = np.arange(50) # till 50 but not 50 (only 49 numbers)
print(z)
z = z[::-1]
print(z)

# Python Packages for Analysing the DataPandas
####################### Pandas ############################################
# pip install pandas

import pandas as pd # importing pandas = > useful for creating dataframes

a1 = [1, 2, 3, 4,4] # list format 
a2 = [10, 11, 12,13,14]  # list format 

a3 = list(range(5))
a3
a1, a2,a3
# Creating a data frame using explicits lists
# it is a pandas object
#contains rows and columns 
df = pd.DataFrame(columns = ["X1","X2","X3"]) 
print(df)

df["X1"] = a1 # Converting list format into pandas series format
df["X2"] = a2 # Converting list format into pandas series format
df["X3"] = a3
print(df)
# series is a one dimensional pandas object
# Dataframe is a two dimensional pandas object
df["X1"] = pd.Series(a1) # Converting list format into pandas series format
df["X2"] = pd.Series(a2) # Converting list format into pandas series format
df["X3"] = pd.Series(a3)
print(df)

# Creating a data frame using explicits lists
#Index is row name
df_new = pd.DataFrame(columns= ['X1','X2','X3'],index = [101,102,103,104,105])
df_new

df_new["X1"] = a1 
df_new["X2"] = a2 
df_new["X3"] = a3
df_new
# accessing columns using "." (dot) operation
df.X1
# accessing columns alternative way
df["X1"]

# Accessing multiple columns : giving column names as input in list format
df[["X1","X2"]]

# Accessing elements using ".iloc" : accessing each cell by row and column 
# index values
df.iloc[0:3,1] #Column can be called with only index postion when we use iloc ,here 1 is column index position

df.iloc[:,:] #to get entire data frame 
df.loc[0:2,["X1","X2"]] #column can be called with only names when we use loc , here [X1,X2]

#Stattistics
df
df['X3'].mean()
df['X3'].median()
df['X3'].mode()

df.describe()

# Merge operation using pandas 
df1 = pd.DataFrame({"X1":[1,2,3],"X2":[4,8,12],})
df2 = pd.DataFrame({"X1":[1,2,3,4],"X3":[14,18,112,15],})
df1,df2
merge = pd.merge(df1,df2, on = "X1") # merge function
merge

# Replace index name
df = pd.DataFrame({"X1":[1,2,3],"X2":[4,8,12]})
df

df.set_index("X1", inplace = True)#Assiging index names using column names
df
# Change the column names 
df = pd.DataFrame({"X1":[1,2,3],"X2":[4,8,12]})

df  = df.rename(columns = {"X1":"X3","X2":"X4"}) #Change column names

print(df)

# Concatenation
df1 = pd.DataFrame({"X1":[1,2,3],"X2":[4,8,12]},index = (2000,2001,2002))
df2 = pd.DataFrame({"X1":[4,5,6],"X2":[14,16,18]},index = (2003,2004,2005))

Concatenate = pd.concat([df1,df2])

print(Concatenate)
##########################
# pip install numpy #module error
import numpy as np
import pandas as pd
x1 = [1, 2, 3, 4,5,np.nan] 
x2 = [np.nan, 11, 12,100,np.nan,200] 
df=pd.DataFrame()
df['grade1']=x1
df['grade2']=x2
print(df)

#finding null values
df.isna().sum()
df.dropna()
# another way to create dataframe
df = pd.DataFrame(
    {"a" : [4,5,6],
     "b" : [7,8,9],           ## Dictionary Key value pairs                                                          
     "c" : [10,11,12]},
    index = [1,2,3])
df
# another way to create dataframe
df = pd.DataFrame(
    [[4,7,10],
     [5,8,11],
     [6,9,12]],
    index = [1,2,3],
    columns = ['a','b','c'])
df

a = pd.Series([50,40,34,30,22,28,17,19,20,13,9,15,10,7,3])
len(a)
a.plot()
a.plot(figsize =(8,6),
       color = 'green',title = 'line plot',fontsize = 12)
b = pd.Series([45,22,12,9,20,34,28,19,26,38,41,24,14,32])
len(b)
c = pd.Series([25,38,33,38,23,12,30,37,34,22,16,24,12,9])
len(c)
d = pd.DataFrame({'a':a,'b':b,'c':c},index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
d
d.plot.area(figsize = (9,6),title = 'Area plot')
d.plot.area(alpha= 0.4, color = ['coral','purple','lightgreen'],figsize = (8,6),fontsize = 12)

##############3 reading extrnal file
import pandas as pd
help(pd.read_csv)
# Import data (.csv file) using pandas. We are using mba data set
mba = pd.read_csv("D:\Python\education.csv")

type(mba) # pandas data frame
mba

mba.groupby('gmat').count()

mba.groupby('gmat').count()['datasrno']

list(mba.groupby('gmat'))

mba.groupby('gmat').sum().sort_values(by='workex')

mba.groupby('gmat').sum().sort_values(by='workex',ascending=False)

###############################Descriptive Statistical Analytics / EDA ######################
# First Moment of Business Decision: Measure of Central Tendency
# Second Moment of Business Decision: Measure of Dispersion
# Third Moment of Business Decision: Measure of Asymmetry
# Fourth Moment of Business Decision: Measure of Peakedness

import pandas as pd

dir(pd)

# Read data into Python
education = pd.read_csv(r"D:\Python\education.csv")
# Education = pd.read_csv("D:\Python\education.csv")

A=10
a=10.1

education.info()

# C:\Users\education.csv - this is windows default file path with a '\'
# C:\\Users\\education.csv - change it to '\\' to make it work in Python

# Exploratory Data Analysis
# Measures of Central Tendency / First moment business decision
education.workex.mean() # '.' is used to refer to the variables within object
education.workex.median()
education.workex.mode()

# pip install numpy
from scipy import stats
stats.mode(education.workex)

# Measures of Dispersion / Second moment business decision
education.workex.var() # variance
education.workex.std() # standard deviation
range = max(education.workex) - min(education.workex) # range
range

# Third moment business decision
education.workex.skew()
education.gmat.skew()

# Fourth moment business decision
education.workex.kurt()

# Data Visualization using Python Libraries such as Matplotlib, Seaborn, Bokeh, Plotly
########################################### Matplotlib ##########################################
# Data Visualization
# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

education.shape

# barplot
plt.bar(height = education.gmat, x = np.arange(1, 774, 1)) # initializing the parameter

plt.hist(education.gmat) # histogram
plt.hist(education.workex, color='red')

help(plt.hist)

plt.figure()

plt.boxplot(education.gmat) # boxplot

help(plt.boxplot)

########################Seaborn###############################

import pandas as pd
import numpy as np
import seaborn as sns
# pip install seaborn
df = pd.read_csv("D:\Python\education.csv")
df.dtypes

# let's find outliers in Salaries
sns.boxplot(df.gmat)

sns.boxplot(df.workex)

#Bokeh
#Plotly
