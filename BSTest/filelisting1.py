import os
import requests
import urllib3
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from imdbpie import Imdb
from io import StringIO
import textwrap

imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests

pathname = 'D:\Eyes\Eng'

def GetCleanName(shortname):
    shortname = shortname.replace('480P', '')
    shortname = shortname.replace('720P', '')
    shortname = shortname.replace('1080P', '')
    shortname = shortname.replace('X264', '')
    shortname = shortname.replace('YIFY', '')
    shortname = shortname.replace('BRRIP', '')
    shortname = shortname.replace('AAC', '')
    shortname = shortname.replace('ETRG', '')
    shortname = shortname.replace('BLURAY', '')
    shortname = shortname.replace('YTS AG', '')
    shortname = shortname.replace('[YTS.AG]', '')
    shortname = shortname.replace('AC3', '')
    shortname = shortname.replace('WEB DL', '')
    shortname = shortname.replace('DOWNLOADHUB', '')
    shortname = shortname.replace('EXTENDED', '')
    shortname = shortname.replace('BITLOKS', '')
    shortname = shortname.replace('MKVCAGE', '')
    shortname = shortname.replace('H264', '')
    shortname = shortname.replace('MP4', '')
    shortname = shortname.replace('( X265 10BIT JOY)', '')
    shortname = shortname.replace('DVDSCR', '')
    shortname = shortname.replace('450MB', '')
    shortname = shortname.replace('750MB', '')
    shortname = shortname.replace('900MB', '')
    shortname = shortname.replace('SUJAIDR', '')
    shortname = shortname.replace('ENG SUBS', '')
    shortname = shortname.replace('ESUBS', '')
    shortname = shortname.replace('264', '')
    shortname = shortname.replace('4K REMASTERED', '')
    shortname = shortname.replace('6CH FARDADOWNLOAD', '')
    shortname = shortname.replace('FIRST TRY', '')
    shortname = shortname.replace('4K REMASTERED', '')
    shortname = shortname.replace('RARBG', '')
    shortname = shortname.replace('WEBRIP', '')
    shortname = shortname.replace('HDRIP', '')
    shortname = shortname.replace('HC   850 MB   IEXTV', '')
    shortname = shortname.replace('BLU RAY  DDS 5 1 SUB  DDR', '')
    shortname = shortname.replace('CPUL', '')
    shortname = shortname.replace('X265 HAXXOR', '')
    shortname = shortname.replace('HC   850 MB   IEXTV', '')
    shortname = shortname.replace('HD TS   CPG', '')
    shortname = shortname.replace('FUM ETTV', '')
    shortname = shortname.replace('DD5 1  FGT ETHD', '')
    shortname = shortname.replace('EVO ETHD', '')
    shortname = shortname.replace('DD5 1  FGT', '')
    shortname = shortname.replace('M2G PRIME', '')
    shortname = shortname.replace('HDTV', '')
    shortname = shortname.replace('VPPV', '')
    shortname = shortname.replace('_2', '')
    shortname = shortname.replace('VYTO', '')
    shortname = shortname.replace('RK   DUAL AUDIO + LEGENDA', '')
    shortname = shortname.replace('M HD    HINDI  TELUGU  BHATTI87', '')
    shortname = shortname.replace('OZLEM  BIA2MOVIES', '')
    shortname = shortname.replace('EXYU SUBS HC', '')
    shortname = shortname.replace('JYK', '')
    shortname = shortname.replace('BLU RAY      5 1CH         1 2GB  TEAM JAFFA', '')
    shortname = shortname.replace('BOKUTOX', '')
    shortname = shortname.replace('DC M', '')
    shortname = shortname.replace('MUXED', '')
    shortname = shortname.replace('6CH 2 9GB', '')
    shortname = shortname.replace('X265 10BIT JOY', '')
    shortname = shortname.replace('BR 1 35GB  COM', '')
    shortname = shortname.replace('ULTIMATE EDITION     T2E', '')

    shortname = shortname.strip()
    return shortname

for root, directories, filenames in os.walk(pathname):
    # for directory in directories:
        # print(os.path.join(root, directory))
    for filename in filenames:
        # print(os.path.join(root,filename))
        (shortname, extension) = os.path.splitext(filename)
        # print(extension)
        shortname = shortname.upper()
        if extension == '.mp4' or extension == '.mkv':
            # print(shortname)
            for char in ' .-[]_()':
                shortname = shortname.replace(char,' ')

            shortname = GetCleanName(shortname)

            print(shortname)
            try:
                fullresult = imdb.search_for_title(shortname)
                # print(len(fullresult))

                if len(fullresult) > 0:
                    # get first search result
                    firstresult = fullresult[0]
                    print(firstresult)

                    # load all details in variables
                    imdb_id = firstresult['imdb_id']
                    imdb_title = firstresult['title']
                    imdb_year = firstresult['year']

                    # Get title by title id
                    title = imdb.get_title_by_id(imdb_id)
                    imdb_rating = title.rating
                    imdb_outline = title.plot_outline
                    print(imdb_outline)

                    im = Image.new('RGBA', (800, 800), 'white')
                    draw = ImageDraw.Draw(im)
                    # draw.text((20, 150), 'Hello', fill='purple')
                    fontsFolder = 'C:\Windows\Fonts'  # e.g. 'Library/Fonts'
                    arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'verdana.ttf'), 10)
                    draw.text((80, 80), str(imdb_title), fill='gray', font=arialFont)
                    draw.text((80, 100), str(imdb_year), fill='gray', font=arialFont)
                    draw.text((80, 120), str(imdb_rating), fill='gray', font=arialFont)
                    if imdb_outline != None:
                        draw.text((80, 140), textwrap.wrap(imdb_outline,width=50), fill='gray', font=arialFont)
                    im.save(root + '\\text.png')




            # except urllib3.exceptions:
            #     print("not working")
            except Exception as ex:
                print("Didnt Work")
                print(ex)

