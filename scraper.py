import argparse
import os
from scrapers import CSL, panama, twitter_scraper

parser = argparse.ArgumentParser(description='Person Scrapper')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('--name','-n', required=True, type=str, help='Example -n Osama')

args = parser.parse_args()

def scrape(name):
    folderName = name.replace(' ', '_')
    cwd = os.getcwd()
    newFolder = os.path.join(os.path.join(cwd,'results'),folderName)
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)
    print("Checking for " + name + "...")
    print("CSL check:")
    CSL.checkCSL(name, newFolder)
    print("Panama Papers check:")
    panama.checkPanama(name, newFolder)
    print("Twitter check:")
    twitter_scraper.checkTwitter(name, newFolder)

scrape(args.name)