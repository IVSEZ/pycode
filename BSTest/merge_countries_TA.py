import pandas as pd
allboth = 'C:\\_out\\all_both_countries.csv'
vnrboth = 'C:\\_out\\vnr_both_countries.csv'
evisaboth = 'C:\\_out\\evisa_both_countries.csv'
onarrivalboth = 'C:\\_out\\onarrival_both_countries.csv'
fileTA = 'C:\\_out\\TA_countries.csv'

allTAboth = 'C:\\_out\\allTA_both_countries.csv'
vnrTAboth = 'C:\\_out\\vnrTA_both_countries.csv'
evisaTAboth = 'C:\\_out\\evisaTA_both_countries.csv'
onarrivalTAboth = 'C:\\_out\\onarrivalTA_both_countries.csv'

dfTA = pd.read_csv(fileTA, encoding='latin-1')

dfallboth = pd.read_csv(allboth, encoding='latin-1')
allmerged = dfallboth.merge(dfTA,left_on='COUNTRY', right_on='ADVISORY', how='left')
allmerged.to_csv(allTAboth,index=None, header=True)
# print(vnrmerged)

dfvnrboth = pd.read_csv(vnrboth, encoding='latin-1')
vnrmerged = dfvnrboth.merge(dfTA,left_on='COUNTRY', right_on='ADVISORY', how='left')
vnrmerged.to_csv(vnrTAboth,index=None, header=True)
# print(vnrmerged)

dfevisaboth = pd.read_csv(evisaboth, encoding='latin-1')
evisamerged = dfevisaboth.merge(dfTA,left_on='COUNTRY', right_on='ADVISORY', how='left')
evisamerged.to_csv(evisaTAboth,index=None, header=True)

dfonarrivalboth = pd.read_csv(onarrivalboth, encoding='latin-1')
onarrivalmerged = dfonarrivalboth.merge(dfTA,left_on='COUNTRY', right_on='ADVISORY', how='left')
onarrivalmerged.to_csv(onarrivalTAboth,index=None, header=True)
