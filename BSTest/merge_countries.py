import requests
import pandas as pd
from bs4 import BeautifulSoup


# ===================================================
urlindia = 'https://en.wikipedia.org/wiki/Visa_requirements_for_Indian_citizens'
fileindia = 'C:\\_out\\india_countries.csv'
vnrindia = 'C:\\_out\\vnr_india_countries.csv'
evisaindia = 'C:\\_out\\evisa_india_countries.csv'
onarrivalindia = 'C:\\_out\\onarrival_india_countries.csv'

urlbrazil = 'https://en.wikipedia.org/wiki/Visa_requirements_for_Brazilian_citizens'
filebrazil = 'C:\\_out\\brazil_countries.csv'
vnrbrazil = 'C:\\_out\\vnr_brazil_countries.csv'
evisabrazil = 'C:\\_out\\evisa_brazil_countries.csv'
onarrivalbrazil = 'C:\\_out\\onarrival_brazil_countries.csv'

vnrtext = "VISA NOT REQUIRED|FREE"
evisatext = "ELECTRONIC|EVISA|E-VISA"
onarrtext = "ON ARRIVAL"
colfilter = "VISA REQUIREMENT"
colmerge = "COUNTRY"
# ===================================================
# MERGE FILES
allboth = 'C:\\_out\\all_both_countries.csv'

vnrboth = 'C:\\_out\\vnr_both_countries.csv'
evisaboth = 'C:\\_out\\evisa_both_countries.csv'
onarrivalboth = 'C:\\_out\\onarrival_both_countries.csv'

dfallindia = pd.read_csv(fileindia, encoding='latin-1')
dfallbrazil = pd.read_csv(filebrazil, encoding='latin-1')
allmerged = dfallindia.merge(dfallbrazil, on=colmerge)
allmerged.to_csv(allboth,index=None, header=True)

dfvnrindia = pd.read_csv(vnrindia, encoding='latin-1')
dfvnrbrazil = pd.read_csv(vnrbrazil, encoding='latin-1')
vnrmerged = dfvnrindia.merge(dfvnrbrazil, on=colmerge)
vnrmerged.to_csv(vnrboth,index=None, header=True)

dfevisaindia = pd.read_csv(evisaindia, encoding='latin-1')
dfevisabrazil = pd.read_csv(evisabrazil, encoding='latin-1')
evisamerged = dfevisaindia.merge(dfevisabrazil, on=colmerge)
evisamerged.to_csv(evisaboth,index=None, header=True)

dfonarrivalindia = pd.read_csv(onarrivalindia, encoding='latin-1')
dfonarrivalbrazil = pd.read_csv(onarrivalbrazil, encoding='latin-1')
onarrivalmerged = dfonarrivalindia.merge(dfonarrivalbrazil, on=colmerge)
onarrivalmerged.to_csv(onarrivalboth,index=None, header=True)