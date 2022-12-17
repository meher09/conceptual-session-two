from pprint import pprint
from wpFunc import wp_list, slugify
import requests
import base64

api_url = 'https://www.gadgetsnow.com/pwafeeds/gnow/web/show/gadgets/json?uName=Google-Pixel-7&category=mobile'
r = requests.get(api_url)
data = r.json().get('jsonFeed').get('data').get('item').get('specs')
# pprint(data)
product_name = r.json().get('jsonFeed').get('data').get('item').get('productName')
battery = data.get('battery')
title = product_name + ' Specifications and Reviews'
content = wp_list(battery)
slug = slugify(product_name)

user = 'aouwal'
password = 'TiL7 fEs2 Brnu ydcm 3AJG EetU'
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
headers = {'Authorization': f'Basic {token.decode("utf-8")}'}

data = {
    'title': title,
    'content': content,
    'slug': slug
}
api_endpoints = 'https://mysite.local/wp-json/wp/v2/posts'
r = requests.post(api_endpoints, data=data, headers=headers, verify=False)
print(r.status_code)