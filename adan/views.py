from django.shortcuts import render

# Create your views here.
import requests

def home(request):
    country = request.GET.get('country')
    month = request.GET.get('month')
    year = request.GET.get('year')
    
    url = f'https://api.aladhan.com/v1/calendarByAddress?address={country}&month={month}&year={year}'
    response = requests.get(url)
    data = response.json()
        
    data = data['data']
    
        
   
    
    
    context = {
        'data' : data
    }
    
    return render(request,'adan-api/home.html', context)