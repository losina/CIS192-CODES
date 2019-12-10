import requests
import json
import random

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
            c = [c['alias'] for c in r['categories']]
            categories = c if len(c) < 3 else c[:3]
            address = " ".join([a["address1"], a['city']])
            sorted.append({'id': r['id'], 'name': r['name'], 'rating': r['rating'], 'categories': categories, 'url':r['url'], 'address': address})
        return sorted
    else:
        return []
def recommend(categories, result):
    if len(categories) < 3:
        categories = random.choices(categories, k=3)
    print(result)
    final = []
    final_names = []
    for cat in categories:
        params2 = {'term': cat,'location':'Philadelphia','sort_by':'rating', 'limit':2, 'categories': 'restaurants'}
        req=requests.get(url, params=params2, headers=headers)
        if req.status_code == 200:
            api_result = json.loads(req.text)
            for r in api_result['businesses']:
                name = r['name']
                print("-----", final, result)
                if name in result or name in final_names:
                    continue
                a = r["location"]
                c = [c['alias'] for c in r['categories']]
                categories = c if len(c) < 3 else c[:3]
                address = " ".join([a["address1"], a['city']])
                final_names.append(name)
                final.append({'id': r['id'], 'name': name, 'rating': r['rating'], 'categories': categories, 'url':r['url'], 'address': address})
    return sorted(final, key=lambda x: x['rating'], reverse=True)

