#!/usr/bin/env python
# coding: utf-8

# ## Case Study using Pandas

# #### Terror Attack city

# In[1]:


import pandas as pd
df = pd.read_csv('terrorismData.csv')

df = df[df.State=='Jammu and Kashmir']
df_list = df['City'].value_counts()
city = df_list.index[0]
count = df_list.values[0]

df = df[df['City']==city]
group = df['Group'].value_counts().index[1]

print(city,count,group)


# #### Terror Government

# In[2]:


import pandas as pd
import numpy as np
df = pd.read_csv('terrorismData.csv')

a = df[df.Day>=26]
b = a[a.Year==2014]
c = b[b.Country=='India']
ans1 = c[c.Month==5]

d = df[df.Year==2014]
e = d[d.Country=='India']
ans2 = e[e.Month>5]

f = df[df.Country=='India']
ans3 = f[f.Year>2014]

count = ans1.shape[0] + ans2.shape[0] + ans3.shape[0]

ans1=ans1[ans1.Group!='Unknown']
ans2=ans2[ans2.Group!='Unknown']
ans3=ans3[ans3.Group!='Unknown']

print(count,ans3.Group.describe().top)


# #### Terror Frequency

# In[3]:


import pandas as pd
import numpy as np
df = pd.read_csv('terrorismData.csv')

year = len(set(df['Year']))

df = df[df.Country == 'India']
df['Casualty'] = df['Killed'] + df['Wounded']

jk = df[df.State == 'Jammu and Kashmir']
rc = df[(df.State == 'Jharkhand') | (df.State == 'Odisha') | (df.State == 'Andhra Pradesh') | (df.State == 'Chhattisgarh')]

jkc = int(np.sum(jk['Casualty']))
rcc = int(np.sum(rc['Casualty']))

print(rcc//year,jkc//year)


# #### Terror Deadliest Attack

# In[4]:


import pandas as pd
df = pd.read_csv('terrorismData.csv')

df = df[df.Killed==df.Killed.max()]
mx_killed = df.Killed.iloc[0]
country = df.Country.iloc[0]
group = df.Group.iloc[0]
print(int(mx_killed), country, group)


# #### Terror Attack

# In[5]:


import pandas as pd
df = pd.read_csv('terrorismData.csv')

df_list = df['Country'].value_counts()
country = df_list.index[0]
attack = df_list.values[0]

df = df[df['Country']==country]
year = df['Year'].value_counts().index[0]

print(country,attack,year)


# In[ ]:




