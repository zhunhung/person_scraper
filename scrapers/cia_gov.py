from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re

def getCIAResults(name):    
    subject = name.lower().replace(' ','+')
    url = 'https://www.cia.gov/search?q=' + subject + '&site=CIA&output=xml_no_dtd&client=CIA&myAction=/search&proxystylesheet=CIA&submitMethod=get&ie=UTF-8&ulang=en&ip=137.132.84.43&access=p&sort=date:D:L:d1&entqr=3&entqrm=0&wc=200&wc_mc=1&oe=UTF-8&ud=1&filter=0'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')    
    result_info = soup.find(id="content-core")
    result_info_items = result_info.find_all('b', limit = 4)
    
    info = []    
    for ri in result_info_items:
        info.append(ri.text.strip())
    num_results= int(info.pop(2))
    num_pages = int(num_results/10 + (num_results % 10 > 0))


    counter = 0    
    pages = []
    for i in range(0,num_pages):
        url2 = 'https://www.cia.gov/search?q=' + subject + '&site=CIA&output=xml_no_dtd&client=CIA&myAction=/search&proxystylesheet=CIA&submitMethod=get&ie=UTF-8&ulang=en&ip=137.132.84.43&access=p&sort=date:D:L:d1&entqr=3&entqrm=0&wc=200&wc_mc=1&oe=UTF-8&ud=1&filter=0&start=' + str(counter)
        pages.append(url2)
        counter += 10
    
    link = []
    title = []    
    desc = []
    date = []        
        
    for item in pages:
        pg = urllib.request.urlopen(item)
        soup2 = BeautifulSoup(pg, 'html.parser')
        result_list = soup2.find(id="content-core")
        
        #get link and title

        result_list_items = result_list.find_all('a', ctype = "c")
        for result in result_list_items:
            link.append(result.get('href')) #get links
            title.append(result.text) #get title
            
        result_list_desc = result_list.find_all('td', class_="s")
        for result2 in result_list_desc:
            temp = result2.text.strip() 
            desc.append(temp[:-19])
            date.append(temp[-10:])
    
    data = pd.DataFrame({'title':title, 'date': date, 'description': desc, 'link':link})
    return data


def checkCIA(name, folder):   
    results_table = getCIAResults(name)
    if len(results_table) == 0:
        print('No results found in www.cia.gov')
    else:
        print('Found ' + str(len(results_table)) + ' matches in www.cia.gov')
        fileName = folder + '/' + name.replace(' ', '_') + '_CIAResults.csv'
        results_table.to_csv(fileName, encoding='utf-8',header=True, index=False)





    
    
    

    
    