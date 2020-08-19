#!/usr/bin/env python
# coding: utf-8

# # Desktop Notifier for COVID-19

# In[1]:


import requests
from bs4 import BeautifulSoup as bs


# In[2]:


req='https://www.worldometers.info/coronavirus/country/india/'


# In[3]:


page=requests.get(req)


# In[4]:


print(page.status_code)


# In[5]:


soup=bs(page.text,'html.parser')


# In[6]:


print(soup.prettify)


# In[7]:


new_cases=soup.find('li',class_='news_li').strong.text.split()[0]


# In[8]:


new_cases


# In[9]:


death=list(soup.find('li',class_='news_li').strong.next_siblings)[1].text.split()[0]


# In[10]:


# Notifier


# In[11]:


from win10toast import ToastNotifier


# In[12]:


message="New Cases : "+new_cases+"\nDeaths : "+death


# In[13]:


message


# In[14]:


notfier=ToastNotifier()


# In[15]:


notfier.show_toast(title="COVID-19 Update",msg=message,duration=5,icon_path='Icons8-Windows-8-Healthcare-Virus.ico')

