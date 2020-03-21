from django.shortcuts import render


def home(request):
    import requests
    import json

    if request.method == "POST":
        quote = request.POST['quotetosearch']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+quote+"/quote?token=pk_c8e987d2696e45c4abcfd5f44b8d24c0")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api' : api})
    else:
        return render(request, 'home.html', {'quote' : "Enter something above in the Search box..."})


def about(request):
    return render(request, 'about.html', {})
