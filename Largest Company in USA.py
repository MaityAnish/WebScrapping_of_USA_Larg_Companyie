#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"


# In[60]:


Headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}


# In[6]:


webpage=requests.get(url,headers=Headers)


# In[7]:


webpage


# In[9]:


soup=BeautifulSoup(webpage.text,'html')


# In[10]:


print(soup)


# In[11]:


soup.find_all('table')


# In[12]:


soup.find('table',class_='wikitable sortable')


# In[26]:


table=soup.find_all('table'[1])


# In[27]:


print(table)


# In[64]:


world_title=soup.find('th')
table.find_all('th')


# In[63]:


world_table_title=[title.text.strip() for title in world_title]
print(world_table_title)


# In[58]:


#table.find_all('th')


# In[31]:


tables = soup.find_all('table')
for table in tables:
    headers = table.find_all('th')
    for header in headers:
        print(header.text)


# In[33]:


soup.find('table',class_='wikitable sortable')


# In[34]:


table=soup.find_all('table')[1]


# In[35]:


print(table)


# In[37]:


world_titles=soup.find_all("th")


# In[38]:


world_titles


# In[40]:


world_table_titles=[title.text.strip() for title in world_titles]
print(world_table_titles)


# In[41]:


table.find_all('th')


# In[42]:


world_titles=table.find_all('th')


# In[44]:


world_titles


# In[45]:


world_table_titles=[title.text.strip() for title in world_titles]
print(world_table_titles)


# In[46]:


df=pd.DataFrame(columns=world_table_titles)
df


# In[49]:


column_data=table.find_all('tr')


# In[50]:


for row in column_data:
    print(row.find_all('td'))


# In[52]:


for row in column_data:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    print(individual_row_data)


# In[53]:


print(individual_row_data)


# In[54]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    #print(individual_row_data)
    length=len(df)
    df.loc[length]=individual_row_data


# In[55]:


df


# In[57]:


df.to_csv(r'D:\Data Analyst\Project\USA large Company\large_company_Usa.csv',index=False)


# In[ ]:




