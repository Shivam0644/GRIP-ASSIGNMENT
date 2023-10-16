#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("/Users/shivamthakur/Downloads/data set/SampleSuperstore.csv")


# In[3]:


print(df.head())
print(df.info())
print(df.describe())


# In[4]:


numeric_cols = df.select_dtypes(include=[np.number])
numeric_cols.hist(bins=20, figsize=(12, 8))


# In[5]:


plt.show()
plt.figure(figsize=(12, 8))
sns.boxplot(data=numeric_cols)
plt.xticks(rotation=90)
plt.show()
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Sales", y="Profit")
plt.title("Profit vs. Sales")
plt.show()


# In[ ]:




