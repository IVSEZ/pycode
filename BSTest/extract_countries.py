import requests
import pandas as pd
from bs4 import BeautifulSoup

class HTMLTableParser:

    def parse_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return [(table['id'], self.parse_html_table(table)) \
                for table in soup.find_all('table')]

    def parse_html_table(self, table):
        n_columns = 0
        n_rows = 0
        column_names = []

        # Find number of rows and columns
        # we also find the column titles if we can
        for row in table.find_all('tr'):

            # Determine the number of rows in the table
            td_tags = row.find_all('td')
            if len(td_tags) > 0:
                n_rows += 1
                if n_columns == 0:
                    # Set the number of columns for our table
                    n_columns = len(td_tags)

            # Handle column names if we find them
            th_tags = row.find_all('th')
            if len(th_tags) > 0 and len(column_names) == 0:
                for th in th_tags:
                    column_names.append(th.get_text().rstrip().lstrip().upper())

        # Safeguard on Column Titles
        if len(column_names) > 0 and len(column_names) != n_columns:
            raise Exception("Column titles do not match the number of columns")

        columns = column_names if len(column_names) > 0 else range(0, n_columns)
        df = pd.DataFrame(columns=columns,
                          index=range(0, n_rows))
        row_marker = 0
        for row in table.find_all('tr'):
            column_marker = 0
            columns = row.find_all('td')
            for column in columns:
                df.iat[row_marker, column_marker] = column.get_text().rstrip().lstrip().upper()
                column_marker += 1
            if len(columns) > 0:
                row_marker += 1

        # Convert to float if possible
        for col in df:
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                pass

        return df




hp = HTMLTableParser()
# table = hp.parse_url('https://en.wikipedia.org/wiki/Visa_requirements_for_Indian_citizens')[0][1]
# print(table.head())

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

website_url=requests.get(urlindia).text
soup = BeautifulSoup(website_url,'lxml')
my_table = soup.find('table',{'class' : 'sortable wikitable'})
# print(my_table)
table = hp.parse_html_table(my_table)
# print(table.head())
vnrtable = table[table[colfilter].str.contains(vnrtext)]
evisatable = table[table[colfilter].str.contains(evisatext)]
onarrtable = table[table[colfilter].str.contains(onarrtext)]

# print(table[table['Visa requirement'].str.contains("Visa not required")].head())
table.to_csv(fileindia,index=None, header=True)
vnrtable.to_csv(vnrindia,index=None, header=True)
evisatable.to_csv(evisaindia,index=None, header=True)
onarrtable.to_csv(onarrivalindia,index=None, header=True)


# ===================================================


website_url=requests.get(urlbrazil).text
soup = BeautifulSoup(website_url,'lxml')
my_table = soup.find('table',{'class' : 'sortable wikitable'})
# print(my_table)
table = hp.parse_html_table(my_table)
# print(table.head())
vnrtable = table[table[colfilter].str.contains(vnrtext)]
evisatable = table[table[colfilter].str.contains(evisatext)]
onarrtable = table[table[colfilter].str.contains(onarrtext)]

table.to_csv(filebrazil,index=None, header=True)
vnrtable.to_csv(vnrbrazil,index=None, header=True)
evisatable.to_csv(evisabrazil,index=None, header=True)
onarrtable.to_csv(onarrivalbrazil,index=None, header=True)

