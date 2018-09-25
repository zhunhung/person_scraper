import argparse
import os
from scrapers import CSL, panama, twitter_scraper, google, cia_gov, reddit, MAS, UN_Sanctions, PepScraper

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
    print("CIA Gov check:")
    cia_gov.checkCIA(name, newFolder)
    print("Twitter check:")
    twitter_scraper.checkTwitter(name, newFolder)
    print("Google check:")
    google.checkGoogle(name, newFolder)
    print("Reddit check:")
    reddit.checkReddit(name, newFolder)
    print("MAS check:")
    MAS.getMASResults(name, newFolder)
    print("UN Sanctions check:")
    UN_Sanctions.getUnResults(name, newFolder)
    print("PEP Database check:")
    PepScraper.getPepResults(name, newFolder)
scrape(args.name)