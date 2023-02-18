from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests



# Create your views here.


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    
    url = f'https://newsapi.org/v2/everything?q=Apple&apiKey=d0b69496c18e463f888a273cb521ea9f'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    



    context = {
        'articles' : articles
    }

    return render(request, 'base.html', context)

