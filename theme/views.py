from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator

# To get as much as I want of pages
def get_smartphones(request):
    if request.method == 'POST':
        button_value = request.POST.get('value')
        print(button_value)
    url = 'https://www.jumia.tn/smartphones/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    smartphones = []
    brands = [] 
    for page in range(0, 1):
        res = requests.get(f"{url}?page={page}", headers=headers)   # the f is a response object returned by the requests module
        soup = BeautifulSoup(res.text, 'html.parser')
        for item in soup.select('.core'):
            name = item['data-name']
            price = item.find('div', {'class': 'prc'}).text
            image = item.find('img')['src']
            brand = item['data-brand']
            category = item['data-category']
            smartphones.append({'name': name, 'price': price, 'brand': brand, 'category': category})
            if brand not in brands:
                brands.append(brand)
    return render(request, 'test.html', {'smartphones': smartphones, 'brands': brands})


def filter(request):
    url = 'https://www.jumia.tn/smartphones/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # Get brand and quantity values from the HTML form
    brand = request.POST.get('brand')
    argent = request.POST.get('argent')
    
    smartphones = []
    brands = []
    
    for page in range(0, 1):
        res = requests.get(f"{url}?page={page}", headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        for item in soup.select('.core'):
            name = item['data-name']
            price = item.find('div', {'class': 'prc'}).text
            image = item.find('img')['src']
            item_brand = item['data-brand']
            category = item['data-category']
            
            if argent:
                argent = int(argent)
            else:
                argent = 0 
            # Check if the brand and quantity filters match
            if item_brand == brand:
                if argent:
                    if float(price[:-4]) < float(argent):
                        smartphones.append({'name': name, 'price': price, 'brand': item_brand, 'category': category})
                else:
                    smartphones.append({'name': name, 'price': price, 'brand': item_brand, 'category': category})
                           
            # Add the brand to the list of brands if it's not already there
            if item_brand not in brands:
                brands.append(item_brand)
    
    return render(request, 'test.html', {'smartphones': smartphones, 'brands': brands})