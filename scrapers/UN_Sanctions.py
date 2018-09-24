
# coding: utf-8

# In[1]:

import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re


# In[2]:

def getUnResults(name):
    search_name1 = name.lower().replace(' ','%7C')
    search_name2= name.lower().replace(' ','+')
    name_lower = name.lower()
    sites= "https://scsanctions.un.org/en/?keywords=+%22" + search_name1+ "%22&per-page=2500&sections=s&sections=s&sort=id&includes=%22"+search_name2 + "%22&excludes=&committee=&nationality=&reference_from=&reference_to="

    page = urllib.request.urlopen(sites)
    soup = BeautifulSoup(page, 'html.parser')

    item_list = soup.findAll('tr', attrs={'class':'rowtext'})

    for item in item_list:
        text = item.text
        text = text.replace('\n', '')
        text = text.replace('\t', '')
        text = text.replace('\xa0',' ')
        text = text.replace('click here', '')
        name_index = text.find('Name: 1:')
        if name_index != -1:
            first_name = text[name_index + len('Name: 1:'): text.find('2:')]
            second_name = text[text.find('2:')+ 1: text.find('3:')]
            third_name = text[text.find('3:')+1: text.find('4:')]
            full_name = first_name + second_name + third_name
            full_name = full_name.replace(' na ','')
            full_name= full_name.replace(':', '')
            full_name = full_name.strip()
            full_name = ' '.join(full_name.split())
            if full_name.lower() == name_lower:
                #return name + ' FOUND in MAS Sanctions List' + " " + sites
                return text
        else: 
            full_name = text[text.find('Name:')+ len('Name:') : text.find('A.k.a.')]
            full_name = full_name.replace(' na ','')
            full_name= full_name.replace(':', '')
            full_name = full_name.strip()
            full_name = ' '.join(full_name.split())
            if full_name.lower() == name_lower:
                #return name + ' FOUND in MAS Sanctions List' + " " + sites
                return text
    return name + ' NOT FOUND in MAS Sanctions List'


# In[3]:

#getUnResults("Eric Badege")


# In[ ]:



