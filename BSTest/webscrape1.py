import requests
import csv
from bs4 import BeautifulSoup

with open('yachts-2.csv', 'w', newline='') as csvfile:
    field_names = ['yacht_name', 'yacht_url', 'yacht_builder', 'yacht_length', 'yacht_date', 'yacht_tspeed',
                   'yacht_cspeed', 'yacht_range',
                   'yacht_beam', 'yacht_guests', 'yacht_crew']
    csvwriter = csv.writer(csvfile, delimiter=',')
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    csvwriter.writerow(
        ['yacht_name', 'yacht_url', 'yacht_builder', 'yacht_length', 'yacht_date', 'yacht_tspeed', 'yacht_cspeed',
         'yacht_range',
         'yacht_beam', 'yacht_guests', 'yacht_crew'])

    for i in range(1,21):
        url = "http://www.boatinternational.com/yachts/the-register/top-200-largest-yachts--25027/page-{0}".format(i)
        print(url)
        try:
            r = requests.get(url)
            print(r.status_code)
            soup = BeautifulSoup(r.content,'html.parser')

            con_text = soup.find_all(class_="content-text")
            # table = soup.findAll('div', attrs={"class": "content-text"})



            for x in con_text:
                # print(x.find('p'))
                print("h3:" + str(x.find('h3')))
                a_text = x.find('a')

                if a_text!=None:
                    yacht_name = ''
                    yacht_url = ''
                    yacht_builder = ''
                    yacht_length = ''
                    yacht_date = ''
                    yacht_tspeed = ''
                    yacht_cspeed = ''
                    yacht_range = ''
                    yacht_beam = ''
                    yacht_guests = ''
                    yacht_crew = ''

                    # print(a_text)
                    yacht_name = a_text.get_text()
                    yacht_url = a_text.get('href')
                    print(yacht_name)
                    print(yacht_url)
                    try:

                        r2 = requests.get(yacht_url)
                        # print('r2:' + str(r2.status_code))
                        soup2=BeautifulSoup(r2.content,'html.parser')
                        con_text2=soup2.find_all(class_="yacht-profile-heading yacht-profile-block")
                        # print(soup2.get_text())
                        for y in con_text2:
                            # print(y.find(itemprop='name').get_text())
                            yacht_builder=y.find(itemprop='url').get_text()
                            yacht_length=y.find(itemprop='depth').get_text()
                            yacht_date=y.find(itemprop='releaseDate').get_text()
                            yacht_tspeed = ''
                            yacht_cspeed = ''
                            yacht_range = ''
                            yacht_beam = ''
                            yacht_guests = ''
                            yacht_crew = ''

                            con_text2 = soup2.find_all(class_="yacht-profile-stat-block")
                            # print(soup2.get_text())
                            for y in con_text2:
                                y2=y.find(class_="yacht-profile-stat-block__title")
                                # print(y2.text)



                                if y2.text.strip() == 'Top Speed':
                                    yacht_tspeed = y.find(class_="yacht-profile-stat-block__value").text
                                    # print(yacht_tspeed)

                                if y2.text.strip() == 'Cruise Speed':
                                    yacht_cspeed = y.find(class_="yacht-profile-stat-block__value").text

                                if y2.text.strip() == 'Range':
                                    yacht_range = y.find(class_="yacht-profile-stat-block__value").text

                                if y2.text.strip() == 'Beam':
                                    yacht_beam = y.find(class_="yacht-profile-stat-block__value").text

                                if y2.text.strip() == 'Guests':
                                    yacht_guests = y.find(class_="yacht-profile-stat-block__value").text

                                if y2.text.strip() == 'Crew':
                                    yacht_crew = y.find(class_="yacht-profile-stat-block__value").text

                                # if y2.text == 'Cruise Speed':
                                #     yacht_cspeed = y.find(class_="yacht-profile-stat-block__value").text


                    except requests.exceptions.ConnectionError:
                        r2.status_code = "Connection refused"

                    csvwriter.writerow(
                        [yacht_name, yacht_url, yacht_builder, yacht_length, yacht_date, yacht_tspeed, yacht_cspeed,
                         yacht_range, yacht_beam, yacht_guests, yacht_crew])
        except requests.exceptions.ConnectionError:
            r.status_code = "Connection refused"