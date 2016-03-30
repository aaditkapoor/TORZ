"""  A python progam to check for movie name """

import requests
import json



def checkMovie(movie):
    url = "http://www.omdbapi.com/?t=%s&y=&plot=short&r=json" % movie

    res = requests.get(url)
    res = res.content

    x = str(res.decode())
    return bool(json.loads(x)['Response'])
