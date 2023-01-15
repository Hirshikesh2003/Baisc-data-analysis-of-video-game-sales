#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv(r"C:\Users\WORKK\Downloads\vgsales.csv")


# In[11]:


df.head(10)


# In[12]:


df.info()  # no null objects


# In[25]:


dict(zip(df["Name"], df["Year"]))  # the year they have released


# In[24]:


dict(zip(df["Name"], df["Publisher"]))  # the publisher that released


# In[34]:


sns.countplot('Year', data = df)    # the years where the games are released the most
plt.xticks(rotation = 'vertical')
print("the years with the most number of games released are 2008-2009")


# In[32]:


sns.countplot('Genre', data = df)    # the genrein which the games are released the most
plt.xticks(rotation = 'vertical')
print("The games with action genre are released the most")


# In[66]:


sns.countplot('Publisher', data = df)  
plt.xticks(rotation = 'vertical')


# In[39]:


df['Publisher'].value_counts() # as we can see we can't visualize the top publisher, but from here we can say that Electronic Arts is the top publisher


# In[ ]:





# In[49]:


print(df["NA_Sales"].max())
df["NA_Sales"]


# In[51]:


df.loc[df['NA_Sales'] == 41.49] #we can infer that the Wii Sports has the maximum sales in 'NA_Sales'


# In[57]:


print(df["EU_Sales"].max())
df.loc[df['EU_Sales'] == 29.02]


# In[59]:


print(df["JP_Sales"].max())        #Pokemon Red/Pokemon Blue has the most number of sales in "JP_Sales"
df.loc[df['JP_Sales'] == 10.22] 


# In[61]:


print(df["Other_Sales"].max())     # Grand Theft Auto: San Andreas has the most number of sales from "Other sales column"
df.loc[df['Other_Sales'] == 10.57]


# In[65]:


print(df["Global_Sales"].max())      # Wii Sports  has the most number of global sales
df.loc[df['Global_Sales'] == 82.74]


# In[ ]:




