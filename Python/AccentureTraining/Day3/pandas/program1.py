import pandas as pd
import numpy as np

# 1st way of creating data frame
data = np.array([['','col1','col2'],['row1',1,2],['row2',3,4]])

my_df = pd.DataFrame(data = data[1:,1:], index = data[1:,0], columns = data[0,1:])

print(my_df)

#2nd way of creating data frame

my_2d_array = np.array([[1,2,3], [4,5,6]])
print(pd.DataFrame(my_2d_array))

#3rd way of creating data frame

print("3rd way of creating data frame")
my_dict = {1:[1,3], 2:[1,2],3:[2,4]}
print(pd.DataFrame(my_dict))

#4

my_df = pd.DataFrame(data = [4,5,6,7], index = range(0,4), columns = ['A'])

#Access of data
print("Access of data")

print(my_df.iloc[0][0])
print(my_df.loc[0]['A'])

print(my_df.at[0,'A'])

my_df=pd.DataFrame(data=[[1,2,3],[4,5,6],[7,8,9]],index=range(3),columns=['A','B','C'])

print(pd.DataFrame(my_df))
