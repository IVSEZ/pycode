import urllib
import urllib.request
from imdbpie import Imdb


imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests

import json


# filenameT = 'EPG-Titles1.txt'
#filenameT = 'EPG-Titles2.txt'
filenameT = 'EPG-Titles3.txt'

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

def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)

with open('imdb_epg3-1.csv', 'w', newline='') as csvfile:
    field_names = ['orig_name','imdb_id', 'imdb_name','imdb_year','imdb_rating','imdb_genre','imdb_cert','imdb_runtime','imdb_tagline','imdb_director','imdb_cast','imdb_outline']
    csvwriter = csv.writer(csvfile, delimiter=',')
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    csvwriter.writerow(['orig_name','imdb_id', 'imdb_name','imdb_year','imdb_rating','imdb_genre','imdb_cert','imdb_runtime','imdb_tagline','imdb_director','imdb_cast','imdb_outline'])

    for line in f:
        print(line)
        orig_name=line
        # get all results
        fullresult = imdb.search_for_title(orig_name)
        #ctr = 0
        #for eachresult in fullresult:
        print(fullresult)
        if fullresult != None:
            # print(fullresult)

            # get first search result
            firstresult = fullresult[0]
            #ctr=ctr+1
            # load all details in variables
            imdb_id = firstresult['imdb_id']
            imdb_title = firstresult['title']
            imdb_year = firstresult['year']



            # Get title by title id
            title = imdb.get_title_by_id(imdb_id)
            imdb_rating = title.rating
            imdb_outline = title.plot_outline
            imdb_director = ''
            imdb_cast = ''
            imdb_genre = ''
            imdb_tagline = title.tagline
            imdb_cert = title.certification
            imdb_runtime = 0
            if title.runtime != None:
                imdb_runtime = humanize_time(title.runtime)

            i=1
            if title.directors_summary != None:
                for imdbdir in title.directors_summary:
                    print(imdbdir.name)
                    if i==1:
                        imdb_director += imdbdir.name
                        i+=i
                    else:
                        imdb_director += ', ' + imdbdir.name
                        i+=i

            i=1
            if title.cast_summary != None:
                for imdbcast in title.cast_summary:
                    print(imdbcast.name)
                    #imdb_cast += ", " + imdbcast.name
                    if i==1:
                        imdb_cast += imdbcast.name
                        i+=i
                    else:
                        imdb_cast += ', ' + imdbcast.name
                        i+=i

            i=1
            if title.genres !=None:
                for imdbgenre in title.genres:
                    print(imdbgenre)
                    #imdb_genre += ", " + imdbgenre
                    if i==1:
                        imdb_genre += imdbgenre
                        i+=i
                    else:
                        imdb_genre += ', ' + imdbgenre
                        i+=i

            # for person in title.credits:
            #     print(person.token)
            #     if person.token == 'directors':
            #         imdb_director = person.name
            #     else if person.token == 'cast':
            #         imdb_cast = person.name
            #         print(person.name + ' is ')


            # imdb_director = title.directors_summary

            #print(imdb_title + " : " + imdb_id + " : " + imdb_year + " : " + str(imdb_rating) + " : " + str(imdb_genre) + " : " + str(imdb_cast) + " : " + imdb_outline)
            #print(imdb_title + " : " + imdb_id + " : " + str(imdb_rating) + " : " + str(imdb_cast))
                  #+ " : " + str(imdb_director) + " : " + imdb_outline)

            # outputWriter.writerow[imdb_id,imdb_title,imdb_year,imdb_rating,imdb_outline]
            csvwriter.writerow([orig_name,imdb_id,imdb_title,imdb_year,imdb_rating,imdb_genre,imdb_cert,imdb_runtime,imdb_tagline,imdb_director,imdb_cast,imdb_outline])



# csvwriter.close()