from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests

#imdb.search_for_title("The Dark Knight")
imdb.search_for_title("Titanic")

#[{'title': "The Dark Knight", 'year':  "2008", 'imdb_id': "tt0468569"},{'title' : "Batman Unmasked", ...}]
#print(imdb)

#print(imdb.__str__())

# imdb.title_exists('tt1327801')

print(imdb.api_keytitle)