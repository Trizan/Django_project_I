from sre_parse import GLOBAL_FLAGS
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
import requests
from PIL import Image
from Engine.form import create_form
from Engine.json_scraper import img_dict_generator



def return_url(request):
    global links
    links = []
    input_string = create_form(request.POST or None)
    context = {
        'input_string': input_string,
    }
    return render(request, 'index.html', context)

def display_img(request):
    links = []
    input_string = create_form(request.POST or None)
    query_string = request.GET.get('search_string')
    for page_no in range(1, 5):
        url = f'https://searx.thegpm.org/?q={query_string}&categories=images&format=json&pageno={page_no}'
        links.extend(img_dict_generator(url))
    input_string = create_form()
    context = {
        'title': query_string,
        'input_string': input_string,
        'source': links,
    }
    return render(request,'display.html', context)


def download_image(request):
    list_of_extensions = ['png', 'jpg', 'jpeg', 'svg']
    if request.method == 'GET' and 'url' in request.GET:
        image_url = request.GET.get('url')
        response = requests.get(image_url)
        if response.status_code == 200:
            file_name = image_url.split('/')[-1]
            file_name_extension = file_name.split('.')[-1]
            if file_name_extension not in list_of_extensions:
                file_name = 'image.jpg'
            response = HttpResponse(response.content, content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename="' + file_name + '"'
            return response
    return HttpResponse(status=400)


def download_img(download_url):
    download_path = f"C:/Users/labuser40/Downloads/img.jpg"
    data = requests.get(download_url).content 
    with open(download_path, 'wb') as f:
        f.write(data)

    img = Image.open(download_path)
    img.show()
