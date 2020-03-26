from django.shortcuts import render, redirect
from .models import Stock
from .form import StockForm
from django.contrib import messages

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

def add_stock(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been saved."))
            return redirect('add_stock')

    else:
        quote = Stock.objects.all()
        output = []
        for quoteItem in quote:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+str(quoteItem)+"/quote?token=pk_c8e987d2696e45c4abcfd5f44b8d24c0")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

        return render(request, 'add_stock.html', {'quote' : quote,
        'output' : output,
        })

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted successfully!"))
    return redirect('deleteStock')


def deleteStock(request):
    quote = Stock.objects.all()
    return render(request, 'deleteStock.html', {'quote' : quote})
