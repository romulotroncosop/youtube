from django.http import response
from django.shortcuts import render
from youtubesearchpython import VideosSearch
from .forms import SearchForm
from .models import Result,Search

# Create your views here.

def home(request):

    
    if request.method == 'POST':
        word_key = SearchForm(data=request.POST)
        if word_key.is_valid():
            word_key.save()


     

    if request.POST.get('name') != 'None':
        videosSearch = VideosSearch(request.POST.get('name'), limit = 20)
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
            
            new_video =Result.objects.create(title = videosSearch.result()['result'][i]['title'],author = videosSearch.result()['result'][i]['channel']['name'],
            description = ' '.join(temp),views = videosSearch.result()['result'][i]['viewCount']['short'],link = videosSearch.result()['result'][i]['link'],
            image = videosSearch.result()['result'][i]['thumbnails'][0]['url'],duration = videosSearch.result()['result'][i]['duration'] )
            new_video.save()

            temp = []
    else:
         dict_results = {}

  
    
    data = {
        'data': dict_results,
        'form': SearchForm(),
    }

    return render(request,'app/home.html',data)

