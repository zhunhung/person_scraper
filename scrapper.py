import argparse
import os
from scrappers import CSL, panama

#Checklist
# OFAC SDN - DONE
#https://developer.trade.gov/consolidated-screening-list.html
# The Panama Papers - Done
# UN Sanctions
# US Sanctions
# MAS Sanctions and Freezing of assets
# PEP databases
# Credit bureaus
# Facebook
# LinkedIn
# Twitters
# Criminal Records
# Court Records
# Google
# FATF


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

scrape(args.name)