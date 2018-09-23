from multiprocessing import Process, Manager
from datetime import datetime
from bs4 import BeautifulSoup
import argparse
import requests
import json
import re


def createSoup(url):
    REQUEST_AGENT = 'Mozilla/5.0 Chrome/47.0.2526.106 Safari/537.36'
    return BeautifulSoup(requests.get(url, headers={'User-Agent':REQUEST_AGENT}).text, 'lxml')

def getSearchResults(searchUrl):
    posts = []
    while True:
        resultPage = createSoup(searchUrl)
        posts += resultPage.findAll('div', {'class':'search-result-link'})
        footer = resultPage.findAll('a', {'rel':'nofollow next'})
        if footer:
            searchUrl = footer[-1]['href']
        else:
            return posts

def parsePost(post, results):
    time = post.find('time')['datetime']
    date = datetime.strptime(time[:19], '%Y-%m-%dT%H:%M:%S')
    title = post.find('a', {'class':'search-title'}).text
    score = post.find('span', {'class':'search-score'}).text
    score = int(re.match(r'[+-]?\d+', score).group(0))
    author = post.find('a', {'class':'author'}).text
    subreddit = post.find('a', {'class':'search-subreddit-link'}).text
    commentsTag = post.find('a', {'class':'search-comments'})
    url = commentsTag['href']
    numComments = int(re.match(r'\d+', commentsTag.text).group(0))
    #print("\n" + str(date)[:19] + ":", numComments, score, author, subreddit, title)
    results.append({'title': title, 'url': url, 'date': str(date), 'score': score,
                    'author': author, 'subreddit': subreddit})

def checkReddit(name, folder):
    SITE_URL = 'https://old.reddit.com/'
    searchUrl = SITE_URL + 'search?q="' + name + '"'
    fileName = folder + '/' + name.replace(' ', '_') + '_redditResults.json'
    try:
        product = json.load(open(fileName))
    except FileNotFoundError:
        print('Creating json file')
        product = {}
    print('Search URL:', searchUrl)
    posts = getSearchResults(searchUrl)
    if (len(posts) == 0):
        return "Found 0 matches in Reddit"
    print('Started scraping', len(posts), 'posts.')
    keyword = name.replace(' ', '-')
    product[keyword] = {}
    product[keyword]['subreddit'] = 'all'
    results = []
    i = 0
    for post in posts:
        parsePost(post, results)
        if i == len(posts):
            break
        i += 1
    product[keyword]['posts'] = list(results)
    print('Found', len(product[keyword]['posts']), 'results')
    with open(fileName, 'w', encoding='utf-8') as f:
        json.dump(product, f, indent=4, ensure_ascii=False)