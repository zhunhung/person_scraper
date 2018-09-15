# Person Scraper

Given a name of a person, the scraper will cross check against the following databases:

- [X] OFAC SDN
- [X] The Panama Papers
- [ ] UN Sanctions
- [ ] US Sanctions
- [ ] MAS Sanctions and Freezing of assets
- [ ] PEP databases
- [X] CIA Database
- [ ] Credit bureaus
- [ ] Facebook
- [ ] LinkedIn
- [X] Twitter
- [ ] Criminal Records
- [X] Court Records
- [ ] Google
- [ ] FATF



### Prerequisites

The code runs on Python 3.X and these are the packages you need:

```
pandas
beautifulsoup4
urllib
```

### Installing

Install the following packages if you have not:

```
pip install pandas
pip install urllib
pip install beautifulsoup4
```


### Running the scrapper

Here's an example if you want to scrape on "Osama Bin Laden"

```
python scrapper.py -n "Osama Bin Laden"
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
person-scrapper/
|-- scrappers/
|   |-- CSL.py
|   |-- panama.py
|
|-- results/
|   |-- Osama_Bin_Laden/
|   |   |-- Osama_Bin_Laden_CSL.json
|   |   |-- Osama_Bin_Laden_PanamaPapers.csv
|
|-- scrapper.py
|-- README
|-- .gitignore
