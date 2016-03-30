""" A system to fetch all torrent links for a query from only popular torrent sites """

from bs4 import BeautifulSoup
import requests 
import random
#from torz.models import TrendingStuff

hdr = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}


complete_url = {

    "kickass":"http://kickasstorrentseu.com",
    "piratesbay":"https://thepiratebay.se",
    'torlock':"http://www.torlock.com",
    "onethreex":"https://1337x.to",
}

    

class TorrentClass():
    def __init__(self,query):
        self.query = query
        self.torrents = []
        self.torrents_bay = []
        self.torrents_kickass = []
        self.torrents_onethreex = []
        self.torrents_torlock = []
        self.final_torrents = []

        self.response_piratesbay = ""
        self.response_kickass = ""
        self.response_onethreex = ""
        self.response_torlock = ""

    def build_response(self):
        try:

            self.response_piratesbay = requests.get("https://thepiratebay.se/search/%s/0/99/0" % self.query)
            self.response_piratesbay = self.response_piratesbay.content
            self.response_kickass = requests.get("https://kat.cr/usearch/%s/" % self.query)
            self.response_kickass = self.response_kickass.content
            self.response_onethreex = requests.get("https://1337x.to/search/%s/1/" % self.query)
            self.response_onethreex = self.response_onethreex.content
            self.response_torlock = requests.get("http://www.torlock.com/all/torrents/%s.html" % self.query)
            self.response_torlock = self.response_torlock.content
        except:
            pass

    def fetch_piratesbay(self):
        soup = BeautifulSoup(self.response_piratesbay)
        for s in soup.findAll("a", attrs={"class":"detLink"}):
            self.torrents_bay.append(complete_url['piratesbay']+s.get("href"))

    def fetch_kickass(self):
        soup = BeautifulSoup(self.response_kickass)

        for s in soup.findAll("a",attrs={"class":"cellMainLink"}):
            self.torrents_kickass.append(complete_url['kickass']+s.get("href"))

    
    def fetch_onethreex(self):
        soup = BeautifulSoup(self.response_onethreex)
        for i in soup.findAll("ul",attrs={"class":"clearfix"}):
            for j in i.findAll("li"):
                    self.torrents_onethreex.append(complete_url['onethreex'] + j.find("div",attrs={"class":"coll-1"}).find("strong").find("a").get("href"))
        
    def fetch_torlock(self):
        soup = BeautifulSoup(self.response_torlock)
        i=2
        while(i <= len(soup.findAll("tr"))-1):
            self.torrents_torlock.append (complete_url['torlock'] + soup.findAll("tr")[i].find("a").get("href"))
            i+=1
        
    def grab_one(self, auto=False):
        if auto:
            self.fetch_piratesbay()
            self.fetch_kickass()
            self.fetch_onethreex()
            self.fetch_torlock()
        bay = self.torrents_bay[random.randint(0,10)]
        kickass = self.torrents_kickass[random.randint(0,10)]
        onethreex = self.torrents_onethreex[random.randint(0,10)]
        torlock = self.torrents_torlock[random.randint(0,10)]

        new = bay + " " + kickass + " "  + onethreex + " "  + torlock

        return new.split()

    def return_torrents(self):

        self.fetch_piratesbay()
        self.fetch_kickass()
        self.fetch_onethreex()
        self.fetch_torlock()

        self.final_torrents = self.torrents_torlock + self.torrents_onethreex  + self.torrents_bay + self.torrents_kickass
        
        return (self.final_torrents)

def createClusterOfTorrents():
    a = TrendingStuff.objects.all()
    first = a[0].movie
    second = a[1].movie
    third = a[2].movie
    fourth = a[3].movie

    main = []

    t1 = TorrentClass(first)
    t1.build_response()
    t1.fetch_piratesbay()
    t1.fetch_torlock()
    t1.fetch_kickass()
    t1.fetch_onethreex()

    t2 = TorrentClass(second)
    t2.build_response()
    t2.fetch_piratesbay()
    t2.fetch_torlock()
    t2.fetch_kickass()
    t2.fetch_onethreex()
    
    t3 = TorrentClass(third)
    t3.build_response()
    t3.fetch_piratesbay()
    t3.fetch_torlock()
    t3.fetch_kickass()
    t3.fetch_onethreex()
    
    t4 = TorrentClass(fourth)
    t4.build_response()
    t4.fetch_piratesbay()
    t4.fetch_torlock()
    t4.fetch_kickass()
    t4.fetch_onethreex()
    

    main = t1.grab_one() + t2.grab_one() + t3.grab_one() + t4.grab_one()


    return main


    

