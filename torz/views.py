from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import random
from .torrentfinder.find import TorrentClass, createClusterOfTorrents
from .models import TrendingStuff, BrainSystem, TorzBrain, URLClicks
from .movie import checkMovie
from .ai.ai import AISystem
from .responder import Responder
import os


def populate():
	t = list(set([i for i in BrainSystem.objects.all()]))
	random.shuffle(t)
	keys = list(set([i.query for i in BrainSystem.objects.all()]))
	return keys


def view_torrents(request):
	q = request.GET.get("query","")

	if q:
		a = BrainSystem.objects.filter(query=q)
		return render_to_response("view.html",{"data":a})



def home(request):
	data = populate()
	return render_to_response("index.html",{"data":data})

def about(request):
	return render_to_response("about.html")

def working(request):
	return render_to_response("working.html")

def add_knowledge(request, info):
	if info:
		TorzBrain.objects.create(brain=info)
		return HttpResponseRedirect('/')
	else:
		return HttpResponse(checkMovie(info))



def click_counter(request):
	count = 0
	url = request.GET.get("url")
	flag = True
	print url

	if url:	
		try:
			 URLClicks.objects.get(url=url)
		except:
			flag = False

		if flag:
			x = URLClicks.objects.get(url=url)
			new = int(x.number) + 1
			URLClicks.objects.update(url=url, number=new)
			return HttpResponseRedirect(url)
		else:
			count+=1
			URLClicks.objects.create(url = url, number=count)
			return HttpResponseRedirect(url)
	else:
		return HttpResponseRedirect('/')

def best_torrents(request):
	a = URLClicks.objects.all()
	return render_to_response("best.html",{"data":a})


def populateBrain2(request):
	a = TorzBrain.objects.all()

	for i in a:
		t = TorrentClass(i)
		t.build_response()
		print("Response made")
		x=0
		for n in t.grab_one(auto=True):
			print ("PUSHED TORRENT URL %d" % x)
			BrainSystem.objects.create(query=i,knowledge=n)
			x+=1

	return HttpResponse("populated!")


def populateBrain(request):
	a = TorzBrain.objects.all()
	c = BrainSystem.objects.all()

	for i in a:
		if (c.filter(query=i).exists()):
			print  "Exists!"
		else:
			t = TorrentClass(i)
			t.build_response()
			print("Response made!!")
			x=1
			for s in t.return_torrents():
				print ("PUSHED TORRENT URL %d" % x)
				BrainSystem.objects.create(query=i,knowledge=s)
				x+=1

	return HttpResponse("POPULATED TORZ'S BRAIN")

def search(request):
	search = request.GET.get("search", "")


	if search:
		t = TorrentClass(search)
		t.build_response()
		data = t.return_torrents()

		return render_to_response("search.html", {"data":data})
	else:
		return HttpResponseRedirect("/")


def brain(request):
	all_knowledge = list(set([i.knowledge for i in BrainSystem.objects.all()]))
	random.shuffle(all_knowledge)
	return render_to_response("brain.html",{"data":all_knowledge})


def ask(request):
	query = request.GET.get("query","").lower()
	list_of_query_on_database = set(list([i.query.lower() for i in BrainSystem.objects.all()]))
	torrents_data = []
	flag = False
	if query:
		for i in list_of_query_on_database:
			if i in query:
				print (i)
				torrents_data = BrainSystem.objects.filter(query=i)
				return render_to_response("ask.html",{"data":torrents_data})
				break
			else:
				flag = False
				continue

		if not flag:
			r = Responder(query)
			data = [r.respond()]
			return render_to_response("ask.html",{"data":data})

	else:
		return render_to_response("ask.html",{"data":["STOP PLAYING ME :("]})

