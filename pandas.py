#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = [5, 10, 15, 20]
index = ['a', 'b', 'c', 'd']
series = pd.Series(data, index=index)
print(series)


# In[5]:


data = {'India': 1400, 'USA': 331, 'China': 1441, 'Brazil': 213}
series = pd.Series(data)
print(series)


# In[7]:


data = 100
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)
print(series)


# In[9]:


data = [10, 20, 30, 40, 50]
index = ['A', 'B', 'C', 'D', 'E']
series = pd.Series(data, index=index)
filtered_series = series[series <= 25]
print(filtered_series)


# In[11]:


series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])
addition_result = series1 + series2
multiplication_result = series1 * series2
print("Addition Result:")
print(addition_result)
print("\nMultiplication Result:")
print(multiplication_result)


# In[13]:


data = [4, 5, 6]
index = ['A', 'l', 'i'] 
series = pd.Series(data, index=index)
print(series)


# In[ ]:




