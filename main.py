import pymongo
from bson.json_util import dumps

con = pymongo.MongoClient('mongodb+srv://danyl:danyl@test.pexza.mongodb.net/test')


mflix = con['sample_mflix']

print(mflix.list_collection_names())

movies = mflix.movies

print(movies.count_documents({}))
countries = ['Russia', 'Japan']
countries = ['Kosovo']


def get_films(movies, countries):
    # print(movies.collection)
    result = []
    for country in countries:
        result = result + list(movies.find({'countries': country}, {'title': 1}))
    # print(result)
    #result = list(movies.find({'countries': countries}, {'title': 1}))
    print(result)
    return len(result)
    #return dumps(movies.find({'countries': countries}, {'title': 1}))
    #return list(movie.find({'country': {$all: countries}}))


print(get_films(movies, countries))
#get_films(movies, countries)

#print(dumps(movies.find({'countries': ['Kosovo']}, {'title': 1}), indent=2))
