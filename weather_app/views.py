from django.shortcuts import render
import requests


def index(request):
    
    if request.POST.get('cityList') == "None":
        city = "Baghdad"

    city = request.POST.get('cityList')
    
    if  city != "":
        part1 ='q'
        part2 = city

        response = requests.get(
            "http://api.apixu.com/v1/forecast.json?key=7dcb3377f6704b1ca9c85452181010"+'&'+str(part1)+'='+str(part2)
        )

        data        = response.json()
        country     = data['location']['country']
        longtude    = data['location']['lon']
        latitude    = data['location']['lat']
        localtime   = data['location']['localtime']
        temperature = data['current']['temp_c']
        status      = data['current']['condition']['text']
        wind_degree = data['current']['wind_degree']
        humidity    = data['current']['humidity']
        i          = "https:"+data['current']['condition']['icon']
        

        mydict = {
            "city": city, "country": country, 
            "longtude": longtude, "latitude": latitude,
            "localtime": localtime, "temperature": temperature,
            "status": status, "wind_degree": wind_degree,
            "humidity": humidity, "icon": i
        }

        return render(request,"index.html", mydict)

    
def about(request):
    return render(request, "about.html")