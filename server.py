from eve import Eve
from eve.auth import TokenAuth
from flask import redirect, request, Response
from settings import posts, users
import json
import random
import string

class RolesAuth(TokenAuth):
    def check_auth(self, token,  allowed_roles, resource, method):
    # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        lookup = {'token': token}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account

def add_token(documents):
    for document in documents:
        document["token"] = (''.join(random.choice(string.ascii_uppercase)
                                    for x in range(10)))

def get_full_relateds(item, key):
    if key in item and item[key]:
        headers = dict(request.headers)
        tc = app.test_client()
        all_relateds =  ",".join(map(lambda x: '"' + str(x) + '"',item[key]))
        resp = tc.get('posts?where={"_id":{"$in":[' + all_relateds + ']}}', headers=headers)
        resp_data = json.loads(resp.data)
        item[key] = resp_data['_items']
    return item

def before_returning_posts(response):
    related = request.args.get('related')
    if related == 'full':
        items = response['_items']
        all_related = ''
        for item in items:
            item = get_full_relateds(item, 'relateds')
    return response

def before_returning_choices(response):
    for item in response['_items']:
        item = get_full_relateds(item, 'choices')
    return response

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

#app = Eve(auth=RolesAuth)
app = Eve()
app.on_replace_article += lambda item, original: remove_extra_fields(item)
app.on_insert_article += lambda items: remove_extra_fields(items[0])
app.on_insert_accounts += add_token
app.on_fetched_resource_posts += before_returning_posts
app.on_fetched_resource_choices += before_returning_choices

@app.route("/sections-latest", methods=['GET'])
def get_sections_latest():
    response = { "_items": {}, 
                 "_links": { 
                            "self": { "href":"sections-latest", "title": "sections latest"}, 
                            "parent":{ "parend": "/", "title": "Home" } } }
    headers = dict(request.headers)
    tc = app.test_client()
    resp = tc.get('/sections', headers=headers)
    resp_header = dict(resp.headers)
    del headers['Content-Length']
    resp_data = json.loads(resp.data)
    if ("_error" not in resp_data and "_items" in resp_data):
        for item in resp_data["_items"]:
            sec_resp = tc.get('/posts?where={"sections":"' + item['_id'] + '"}&max_results=5', headers=headers)
            sec_items = json.loads(sec_resp.data)
            if '_error' not in sec_items and "_items" in sec_items:
                #response[item['name']] = sec_items['_items']
                response['_items'][item['name']] = sec_items['_items']
    return Response(json.dumps(response), headers=resp_header)        
        

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
