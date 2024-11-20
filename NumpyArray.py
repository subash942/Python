#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Create a NumPy  array containing the first 10 positive integers (1D array)
array_1d = np.arange(1, 11)
print(array_1d)


# In[3]:


# Create an array with all even numbers between 10 and 50
even_numbers = np.arange(10, 51, 2)
print(even_numbers)


# In[5]:


# Create a 2D array of shape (3, 4) filled with zeros
zeros_array = np.zeros((3, 4))
print("Zeros Array:")
print(zeros_array)


# In[7]:


# Create a 2D array of shape (3, 4) filled with ones
ones_array = np.ones((3, 4))
print("Ones Array:")
print(ones_array)


# In[9]:


# Create a 2D NumPy array with specified values
custom_array = np.array([[1, 2, 3], 
                          [4, 5, 6], 
                          [7, 8, 9]])
print("Custom Array:")
print(custom_array)


# In[11]:


arr = np.array([10,20,30,40,50,60])
subarray = arr[1:4]
print("slice a subset")
print(subarray)


# In[13]:


arr = np.array([[1, 2, 3], 

                [4, 5, 6], 

                [7, 8, 9]])
rows_extracted = arr[[0, 2]]
print("Extracted Rows:")
print(rows_extracted)
columns_extracted = arr[:, [0, 1]]
print("Extracted Columns:")
print(columns_extracted)


# In[15]:


arr = [5, 10, 15, 20, 25]
reversed_arr = arr[::-1]
print("Reversed Array using Python List:")
print(reversed_arr)


# In[17]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = arr[1::2]
print("Every second element starting from index 1:")
print(result)


# In[19]:


arr = np.array([[10, 20, 30, 40], 
                [50, 60, 70, 80], 
                [90, 100, 110, 120]])
result=arr[2:3:]
print("Extract the four corner elements")
print(result)


# In[21]:


arr11 = np.array([[10, 20, 30, 40], 
                [50, 60, 70, 80], 
                [90, 100, 110, 120]])

print("All rows but only the last column")
print(arr11[:, -1])
print("\nfirst two rows")
print(arr11[ :2])
print("\nfirst two Columns")
print(arr11[:, :2])


# In[ ]:




