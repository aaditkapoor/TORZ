"""torz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^push-brain/$','torz.views.populateBrain'),
    url(r'^$','torz.views.home'),
    url(r'^ask/','torz.views.ask'),
    url(r'^about/$','torz.views.about'),
    url(r'^best-torrents/$','torz.views.best_torrents'),
    url(r'^working/$','torz.views.working'),
    url(r'^click-counter/','torz.views.click_counter'),
    url(r'^torz-brain/$','torz.views.brain'),
    url(r'^search/','torz.views.search'),
    url(r'^add-knowledge/(?P<info>\w+.*)/','torz.views.add_knowledge'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)