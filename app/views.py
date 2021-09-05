from django.http import response
from django.shortcuts import render
from youtubesearchpython import VideosSearch
from django.http.response import HttpResponse


# Create your views here.

def home(request):
    videosSearch = VideosSearch('Machine Gun Kelly ft. blackbear', limit = 20)
    temp = []
    dict_results = {}
    for i in range(len(videosSearch.result()['result'])):

        try:
            for j in videosSearch.result()['result'][i]['descriptionSnippet']:
                temp.append(j['text'])
        except:
            temp.append('Non description')

        dict_results.update(
            {str(i): 
            {'title': videosSearch.result()['result'][i]['title'] , 
            'duration' : videosSearch.result()['result'][i]['duration'],
            'img' :videosSearch.result()['result'][i]['thumbnails'][0]['url'],
            'view' : videosSearch.result()['result'][i]['viewCount']['short'],
            'author' : videosSearch.result()['result'][i]['channel']['name'],
            'link' : videosSearch.result()['result'][i]['link'],
            'description' : ' '.join(temp),
            }})
        temp = []
    data = {
        'data': dict_results
    }
    return render(request,'app/home.html',data)

