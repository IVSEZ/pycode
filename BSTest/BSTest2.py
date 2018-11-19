import urllib
import urllib.request
from imdbpie import Imdb


imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests

import json


filenameT = 'IMDB-Titles.txt'

# sometext = imdb.search_for_title("Banshee")
# sometext2 = sometext[0]
# id = sometext2['imdb_id']
# title = imdb.get_title_by_id(id)
# episode = imdb.get_episodes(id)
# print(title.title)
# print(episode)
# print()

f = open(filenameT, mode='r')

import csv

# outputFile = open('imdb.csv','w',newline='')
# outputWriter = csv.writer(outputFile)

with open('imdb.csv', 'w', newline='') as csvfile:
    field_names = ['imdb_id', 'imdb_name','imdb_year','imdb_rating','imdb_outline']
    csvwriter = csv.writer(csvfile, delimiter=',')
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    csvwriter.writerow(['imdb_id', 'imdb_name','imdb_year','imdb_rating','imdb_outline'])

    for line in f:
        # get all results
        fullresult = imdb.search_for_title(line)
        # print(fullresult)

        # get first search result
        firstresult = fullresult[0]

        # load all details in variables
        imdb_id = firstresult['imdb_id']
        imdb_title = firstresult['title']
        imdb_year = firstresult['year']



        # Get title by title id
        title = imdb.get_title_by_id(imdb_id)
        imdb_rating = title.rating
        imdb_outline = title.plot_outline

        print(imdb_title + " : " + imdb_id + " : " + str(imdb_rating) + " : " + imdb_outline)
        # outputWriter.writerow[imdb_id,imdb_title,imdb_year,imdb_rating,imdb_outline]
        csvwriter.writerow([imdb_id,imdb_title,imdb_year,imdb_rating,imdb_outline])


csvwriter.close()