import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re

def getFBProfiles(name):
    
    subject = name.lower().replace(' ','-')
    links= []
    names= []
  
    url = 'https://www.facebook.com/public/' + subject 
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')    
    text = str(soup)
    result = re.findall('<a class="_32mo"(.*?)/span>',text)    
    
    for r in result:
        link = re.search('href="(.*)">',r)
        name = re.search('><span>(.*)<', r)
        links.append(link.group(1))
        names.append(name.group(1))            
    data = pd.DataFrame({'Name':names, 'Link': links})
    return data

    print(len(links))

        
def checkFB(name,folder):   
    results_table = getFBProfiles(name)
    if len(results_table) == 0:
        print('No results found in www.facebook.com')
    else:
        print('Found ' + str(len(results_table)) + ' matches in www.facebook.com')
        results_table.to_csv("FB.csv" , header = True, index = False )
        fileName = folder + '/' + name.replace(' ', '_') + '_FBResults.csv'
        results_table.to_csv(fileName, encoding='utf-8',header=True, index=False)

#test: 
#checkFB('Daniel Tan')
      