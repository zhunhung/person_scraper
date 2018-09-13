import urllib.request
import json

def checkCSL(name, folder):
    urlname = name.replace(' ', '%20')
    url = 'https://api.trade.gov/consolidated_screening_list/search?api_key=AWsbLvhl2q_-vqIz1V00QX-o&name=%s&type=Individual' %(urlname)
    contents = urllib.request.urlopen(url).read()
    results = json.loads(contents)["results"]
    fileName = folder + '/' + name.replace(' ', '_') + '_CSL.json'
    with open(fileName, 'w') as outfile:
        json.dump(results, outfile)
    print("Found " + str(len(results)) + " matches in CSL")