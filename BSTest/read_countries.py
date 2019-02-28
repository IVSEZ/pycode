import pandas as pd

vnrTAboth = 'C:\\_out\\vnrTA_both_countries.csv'
evisaTAboth = 'C:\\_out\\evisaTA_both_countries.csv'
onarrivalTAboth = 'C:\\_out\\onarrivalTA_both_countries.csv'

finalfile = 'C:\\_out\\final_countries.csv'

dfvnrTAboth = pd.read_csv(vnrTAboth, encoding='latin-1')
dfevisaTAboth = pd.read_csv(evisaTAboth, encoding='latin-1')
dfonarrivalTAboth = pd.read_csv(onarrivalTAboth, encoding='latin-1')

dfconcat = pd.concat([dfvnrTAboth, dfevisaTAboth, dfonarrivalTAboth], ignore_index=True)

dfconcat.to_csv(finalfile,index=None, header=True)

# print(dfconcat)


