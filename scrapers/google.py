import urllib.request
import json
import config_keys

def checkGoogle(name, folder):
    urlname = name.replace(' ', '%20')
    url = 'https://www.googleapis.com/customsearch/v1?key=%s&cx=008469397288160540229:emgz62cres4&q=%s' % (config_keys.googleAPI, urlname)
    contents = urllib.request.urlopen(url).read()
    results = json.loads(contents)["items"]
    matchCount = json.loads(contents)['searchInformation']['totalResults']
    fileName = folder + '/' + name.replace(' ', '_') + '_GoogleSearch.json'
    # TO-DO process the data dump
    with open(fileName, 'w') as outfile:
        json.dump(results, outfile)
    print("Found " + matchCount + " matches in Google Search")