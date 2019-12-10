import requests
import json

api_key='-4s2dP9Rl9T0e30DOmljIoReMpCfCx4UWxAGPJBkXFEuJy-dzf-iwClrVnPk0s1Mb63a9pFAC75GC6xrX4dvlT0GL6_SIrbt90dwA-X38IodBSxUj79ZtdNpfN3uXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'
params = {'term':'input','location':'Philadelphia','sort_by':'rating', 'limit':9, 'categories': 'restaurants'}


def search(keyword) :
    params['term'] = keyword
    req=requests.get(url, params=params, headers=headers)

    if req.status_code == 200:
        result = json.loads(req.text)
        sorted = []
        for r in result['businesses']:
            a = r["location"]
            c = r['categories']
            categories = c if len(c) < 3 else c[:3]
            address = " ".join([a["address1"], a['city']])
            sorted.append({'id': r['id'], 'name': r['name'], 'rating': r['rating'], 'categories': categories, 'url':r['url'], 'address': address})
        return sorted
    else:
        return []

