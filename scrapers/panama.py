import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re



def getPanamaResults(name):
    
    search_name = name.lower().replace(' ','+')
    initial_page = 'https://offshoreleaks.icij.org/search?cat=1&e=&q='+search_name+'&utf8=%E2%9C%93'

    page = urllib.request.urlopen(initial_page)

    soup = BeautifulSoup(page, 'html.parser')

    results_count = soup.find('div', attrs={'id':'results_wrapper'})

    #Get number of officers/individual count
    officerCategory = str(results_count.find_all('li')[1]).replace('\n', '')
    countpat = r'(?<=\().+?(?=\))'
    resultsCount = int(re.findall(countpat,officerCategory)[0])
    results_table = pd.DataFrame(columns=['Names', 'Node', 'Source'],index=range(resultsCount)) # I know the size 

    #Iterate through the pages and search results
    pageCount = 0
    namepat = r'(?<=\>).+?(?=\<)'
    nodepat = r'(?<=\/).+?(?=\")'
    row_marker = 0
    for i in range((resultsCount//100)+1):
        newpage = 'https://offshoreleaks.icij.org/search?cat=1&e=&from=' + str(pageCount) + '&q='+search_name+'&utf8=%E2%9C%93'
        newpage = urllib.request.urlopen(newpage)
        newsoup = BeautifulSoup(newpage, 'html.parser')
        table_box = newsoup.find('table', attrs={'class':'search_results'})
        names = table_box.find_all('a')
        for row in names:
            str_row = str(row).replace('\n','')
            if 'nodes' in str_row:
                person_name = re.findall(namepat, str_row)[0].strip()
                results_table.iat[row_marker, 0] = person_name
                node = re.findall(nodepat, str_row)[0].split('/')[1]
                results_table.iat[row_marker, 1] = node  
            else:
                source_name = re.findall(namepat, str_row)[0]
                results_table.iat[row_marker, 2] = source_name
                row_marker += 1
        pageCount += 100
    return results_table



#To Compare Names
def nameMatching(testName, dbName, threshold=0.7):
    testName = testName.lower()
    dbName = dbName.lower()
    testList = testName.split(' ')
    dbNameList = dbName.split(' ')
    count = 0
    for name in testList:
        if name in dbNameList:
            count+= 1
    count = count/len(testList)
    if count > threshold:
        return True
    return False


def checkPanama(testName, folder):
    results_table = getPanamaResults(testName)
    filteredNameDb = pd.DataFrame([results_table.iloc[row] for row in results_table.index if nameMatching(testName, results_table.iloc[row]['Names'])])
    filteredNameDb.reset_index(drop=True, inplace=True)
    if len(filteredNameDb) == 0:
        print('No results found in Panama Papers')
    else:
        print('Found ' + str(len(filteredNameDb)) + ' matches in Panama Papers')
        filteredNameDb[['URL']] = 'https://offshoreleaks.icij.org/nodes/' + filteredNameDb[['Node']]
        filteredNameDb.drop(columns=['Node'], inplace=True)
        fileName = folder + '/' + testName.replace(' ', '_') + '_PanamaPapers.csv'
        filteredNameDb.to_csv(fileName,encoding='utf-8',header=True, index=False)
    


