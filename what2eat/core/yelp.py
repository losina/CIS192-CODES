import requests
import json
import random
YOURKEYHERE = "dddd"
api_key = YOURKEYHERE
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'Bearer %s' % api_key}

# class that defines parameters for yelp api search 
class YelpAPIManager():
    params = {'location':'Philadelphia','sort_by':'rating', 'categories': 'restaurants'}
    def __init__(self, term, limit):
        self.params['term'] = term
        self.params['limit'] = limit
    def get(self):
        result = requests.get(url, params=self.params, headers=headers)
        if result.status_code == 200:
            return json.loads(result.text)
        else:
            return {}

# get Yelp search result based on the keyword
def search(keyword) :
    api = YelpAPIManager(keyword, 9)
    result = api.get()

    if len(result) != 0:
        final = []
        for r in result['businesses']:
            a = r["location"]
            c = [c['alias'] for c in r['categories']]
            categories = c if len(c) < 3 else c[:3]
            address = " ".join([a["address1"], a['city']])
            final.append({'id': r['id'], 'name': r['name'], 'rating': r['rating'], 'categories': categories, 'url':r['url'], 'address': address})
        return sorted(final, key=lambda x: x['rating'], reverse=True)
    else:
        return []
    
# get few extra recommendations at the end of selection mode
# remove any search result that is already in the list
def recommend(categories, result):
    if len(categories) < 3:
        categories = random.choices(categories, k=3)

    final = []
    final_names = []
    for cat in categories:
        api = YelpAPIManager(cat, 2)
        api_result = api.get()
 
        if len(api_result) != 0:
            
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

