import requests
import json

def img_dict_generator(url):
    urls = []
    content = requests.get(url).text
    if 'results' in content:
        json_content = json.loads(content)
        all_results = json_content.get('results')
        for result in all_results:
            urls.append(result['img_src'])
    return urls