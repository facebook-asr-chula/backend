import facebook
import requests

pic = ',picture.height(720).width(720){url}'
lim = '.limit(5)'
lim1 = '.limit(1)'

def getmytoken():
    file = open('token.txt','r')
    token = ""
    for line in file:
        token = token + line
    #print(token)
    return token


def getMyPost(graph):
    event = graph.request('me?fields=name,posts'+lim1+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for d in event['posts']['data']:
        try:
            data = {
                'message': d['message'],
                'time': d['created_time']
            }
            ret.append(data)
        except:
            ret = ret
    return {'name': name, 'pic': picture, 'data':ret}

def getMyPostLike(graph):
    event = graph.request('me?fields=name,posts'+lim1+'{message,likes}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for d in event['posts']['data']:
        data = {
            'message': d['message'],
            'count':0,
        }
        data['count']+= len(d['likes']['data'])
        try:
            while(true):
                url = d['likes']['paging']['next']
                resp = requests.get(url)
                d['likes'] = resp.json()
                data['count'] += len(d['likes']['data'])
        except:
            data['count']+=0
        ret.append(data)

    return {'name': name, 'pic': picture, 'data':ret}

def getMyPostComment(graph):
    event = graph.request('me?fields=name,posts'+lim1+'{message,comments'+lim+'{message,from{name'+pic+'}}}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for d in event['posts']['data']:
        data = {
            'message': d['message'],
            'data': [],
        }
        for dd in d['comments']['data']:
            data['data'].append({'name':dd['from']['name'], 'pic': dd['from']['picture']['data']['url'], 'message':dd['message']})

        ret.append(data)

    return {'name': name, 'pic': picture, 'data':ret}

def getMyPostShare(graph):
    event = graph.request('me?fields=name,posts'+lim1+'{message,shares}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for d in event['posts']['data']:
        data = {
            'message': d['message'],
            'count':d['shares']['count']
        }
        ret.append(data)

    return {'name': name, 'pic': picture, 'data':ret}

def getMyLocation(graph):
    event = graph.request('me?fields=name,tagged_places'+lim1+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for d in event['tagged_places']['data']:
        data = {
            'message': d['place']['name'],
            'time': d['created_time']
        }
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

def getMyPage(graph):
    event = graph.request('me?fields=name,likes'+lim+'{name'+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for d in event['likes']['data']:
        data = {
            'name': d['name'],
            'pic': d['picture']['data']['url']
        }
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

def getMyPageLike(graph):
    event = graph.request('me?fields=name,likes'+lim+'{name,fan_count'+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for d in event['likes']['data']:
        data = {
            'name': d['name'],
            'pic': d['picture']['data']['url'],
            'count': d['fan_count']
        }
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

def getMyPagePost(graph):
    event = graph.request('me?fields=name,likes'+lim+'{name,posts'+lim1+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for d in event['likes']['data']:
        posts = []
        for p in d['posts']['data']:
            try:
                data = {
                    'message': p['message'],
                    'time': p['created_time']
                }
                posts.append(data)
            except:
                posts = posts
        data = {
            'name': d['name'],
            'pic': d['picture']['data']['url'],
            'message': posts
        }
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

#me?fields=friends{picture.height(720).width(720){url}}
#name, pic
def getFriend(graph):
    event = graph.request('me'+'?fields=name,friends'+lim+'{name'+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for friend in event['friends']['data']:
        data = {
            'name': friend['name'],
            'pic': friend['picture']['data']['url']
        }
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

#name, pic, device
def getFriendDevice(graph):
    event = graph.request('me'+'?fields=name,friends'+lim+'{name,devices.limit(1)'+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for friend in event['friends']['data']:
        data = {
            'name': friend['name'],
            'pic': friend['picture']['data']['url'],
        }
        try:
            data['count']=friend['devices'][:1][0]['os']
        except:
            data['count']="อะไรไม่รู้ เขาไม่บอก"
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

#name, pic, post{msg, time, pic(ถ้ามี)}
def getFriendPost(graph):
    event = graph.request('me?fields=name,friends'+lim+'{name,posts'+lim1+''+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    #print(event['friends']['data'][0]['posts'])
    for friend in event['friends']['data']:
        data = {
            'name': friend['name'],
            'pic': friend['picture']['data']['url'],
            'data' : []
        }
        try:
            for post in friend['posts']['data']:
                try:
                    a = {'message':post['message'], 'time':post['created_time']}
                    data['data'].append(a)
                except:
                    data = data
        except:
            ret = ret
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

#name, pic, book{name,pic}
def getFriendBook(graph):
    event = graph.request('me?fields=name,friends'+lim+'{name,books'+lim1+'{name'+pic+'}'+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for friend in event['friends']['data']:
        data = {
            'name': friend['name'],
            'pic': friend['picture']['data']['url'],
            'data' : []
        }
        try:
            for book in friend['books']['data']:
                a = {'name':book['name'], 'pic':book['picture']['data']['url']}
                data['data'].append(a)
        except:
            data = data
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

#name, pic, friend{name,pic}
def getFriendFriend(graph):
    event = graph.request('me?fields=name,friends'+lim1+'{name,friends'+lim+'{name'+pic+'}'+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for friend in event['friends']['data']:
        data = {
            'name': friend['name'],
            'pic': friend['picture']['data']['url'],
            'data' : []
        }
        try:
            for f in friend['friends']['data']:
                a = {'name':f['name'], 'pic':f['picture']['data']['url']}
                data['data'].append(a)
        except:
            data = data
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

def getFriendLocation(graph):
    event = graph.request('me?fields=name,friends'+lim+'{name,tagged_places'+lim1+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    #print(event['friends']['data'][0]['posts'])
    for friend in event['friends']['data']:
        data = {
            'name': friend['name'],
            'pic': friend['picture']['data']['url'],
            'data' : []
        }
        try:
            for post in friend['tagged_places']['data']:
                try:
                    a = {'message':post['place']['name'], 'time':post['created_time']}
                    data['data'].append(a)
                except:
                    data = data
        except:
            ret = ret
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

#name, pic, page{name,pic}
def getFriendLike(graph):
    event = graph.request('me?fields=name,friends'+lim+'{name,likes'+lim1+'{name'+pic+'}'+pic+'}'+pic)
    name = event['name']
    picture = event['picture']['data']['url']
    ret = []
    for friend in event['friends']['data']:
        data = {
            'name': friend['name'],
            'pic': friend['picture']['data']['url'],
            'data' : []
        }
        try:
            for page in friend['likes']['data']:
                a = {'name':page['name'], 'pic':page['picture']['data']['url']}
                data['data'].append(a)
        except:
            data = data
        ret.append(data)
    return {'name': name, 'pic': picture, 'data':ret}

def chk(keyword, result):
    idx = 0
    for word in keyword:
        idx = result.find(word,idx)
        if(idx==-1):
            return False
    return True
