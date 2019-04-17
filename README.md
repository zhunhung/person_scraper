# Person Scraper

Given a name of a person, the scraper will cross check against the following databases:

- [X] OFAC SDN
- [X] The Panama Papers
- [X] UN Sanctions
- [X] US Sanctions
- [X] MAS Sanctions and Freezing of assets
- [X] PEP databases
- [X] CIA Database
- [ ] Credit bureaus
- [X] Facebook
- [ ] LinkedIn
- [X] Twitter
- [ ] Criminal Records
- [X] Court Records
- [X] Google
- [ ] FATF
- [X] Reddit



### Prerequisites

The code runs on Python 3.X and these are the packages you need:

```
pandas
beautifulsoup4
urllib
python-linkedin
```

### Installing

Install the following packages if you have not:

```
pip install pandas
pip install urllib
pip install beautifulsoup4
pip install python-linkedin
```


### Running the scrapper

Here's an example if you want to scrape on "Osama Bin Laden"

```
python scraper.py -n "Osama Bin Laden"
```

And the output will be something like this:
```
Checking for Osama Bin Laden...
CSL check:
Found 1 matches in CSL
Panama Papers check:
Found 0 matches in Panama Papers
```

The search results can be found in the results/name folder
```
person-scraper/
|-- scrapers/
|   |-- CSL.py
|   |-- panama.py
|
|-- results/
|   |-- Osama_Bin_Laden/
|   |   |-- Osama_Bin_Laden_CSL.json
|   |   |-- Osama_Bin_Laden_PanamaPapers.csv
|
|-- scraper.py
|-- README
|-- .gitignore
