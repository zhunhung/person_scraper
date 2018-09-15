
# coding: utf-8

# In[1]:

import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re


# In[77]:

def getStateCourtResults(name):
    
    name_lower = name.lower()
    search_name = name_lower.replace(' ','%20')
    stateCourt = 'https://www.statecourts.gov.sg/Pages/BasicSearchResult.aspx?k='+ search_name
    page = urllib.request.urlopen(stateCourt)
    soup = BeautifulSoup(page, 'html.parser')
    
    table = html.find('table')
    contents = table.text.lower()
    
    if contents.find(name_lower)!= -1:
        return name + ' FOUND in State Court Records'
    
    
    return name + ' NOT FOUND in State Court Records'


# In[80]:

### Test
'''
print(getStateCourtResults('kang CHI LOONG'))
print(getStateCourtResults('PANG CHI KANG'))
'''


# In[ ]:



