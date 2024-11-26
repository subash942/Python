#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


def temp():
    temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
    hotday = (temperatures > 35)
    hot_day_count = np.sum(hotday)
    coldday = (temperatures < 5)
    cold_day_count = np.sum(coldday)
    print("The No. of hot days  :", hot_day_count,"\n",hotday)
    print("\nThe No. of cold days :", cold_day_count,"\n",coldday)
    return hot_day_count, cold_day_count
    
res = temp()
print("\nReturned Results:", res)


# In[7]:


def sales():
    monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
    quarterly_report=monthly_sales.reshape(4,3)
    return quarterly_report
    
res=sales()
print(res)


# In[9]:


def customer():
    customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
    last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
    less_than_30_days = customer_ids[last_purchase_days_ago <= 30]
    more_than_30_days = customer_ids[last_purchase_days_ago > 30]
    return less_than_30_days, more_than_30_days
made_purchase, no_purchase = customer()
print(f'Customers who made a purchase in the last 30 days: \n{made_purchase}\n')
print(f"Customers who haven't made a purchase in the last 30 days:\n{no_purchase}")


# In[11]:


def emp_details():
    full_time_employees = np.array([    
        [101, 'John Doe', 'Full-Time', 55000],
        [102, 'Jane Smith', 'Full-Time', 60000],
        [103, 'Mike Johnson', 'Full-Time', 52000]
    ])
    part_time_employees = np.array([
        [201, 'Alice Brown', 'Part-Time', 25000],
        [202, 'Bob Wilson', 'Part-Time', 28000],
        [203, 'Emily Davis', 'Part-Time', 22000]
    ])
    res=np.concatenate([full_time_employees,part_time_employees])
    return res
emp=emp_details()
print(f"the list of all Employees is :\n\n {emp}")


# In[ ]:




