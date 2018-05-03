import facebook
import requests
from backmt import *

token = getmytoken()
graph = facebook.GraphAPI(access_token = token)

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"



@app.route('/asr')
def asr():
    x = request.args.get('x')
    x =  str(x).split(',')

    for result in x[:3]:

        keywords = {
        			0	:['เรา', 'โพส'],
                    1	:['เรา', 'เช็ค', 'อิน'],
                    3	:['ล่าสุด', 'ถูกใจ'],
                    4	:['ล่าสุด', 'แชร์'],
                    5	:['ล่าสุด', 'ความ', 'คิด', 'เห็น'],
                    6	:['ขอ', 'เพื่อน', 'เรา'],
                    7	:[ 'เล่น', 'เฟซ'],
                    8	:['เพื่อน', 'ของ', 'เพื่อน'],
                    9	:['หนัง', 'สือ'],
                    10	:['เพื่อน', 'โพส'],
                    11	:['เพื่อน', 'เช็ค', 'อิน'],
                    12	:['เพื่อน', 'เพจ'],
                    13	:['ถูกใจ', 'เพจ'],
                    14	:['เพจ', 'โพส'],
                    15	:['เพจ', 'เรา', 'ชอบ']
                    }

        ret = dict()
        ret['type'] = -1

        if chk(keywords[0], result):
            ret = getMyPost(graph)
            ret['type'] = 1
            script = 'โพสต์ล่าสุดของคุณ คือ ' + ret['data'][0]['message']
            ret['script'] = script
            ret['sentence'] = 'เราโพสต์อะไร'


        elif chk(keywords[1], result):
            ret = getMyLocation(graph)
            ret['type'] = 1
            script = 'คุณเช็คอินล่าสุด ที่ ' + ret['data'][0]['message']
            ret['script'] = script
            ret['sentence'] = 'เราเช็คอินที่ไหน'

        elif chk(keywords[3], result):
            ret = getMyPostLike(graph)
            ret['type'] = 2
            script = 'โพสต์ล่าสุดของคุณมีคนถูกใจ ' + str(ret['data'][0]['count']) + ' คน'
            ret['script'] = script
            ret['sentence'] = 'โพสต์ล่าสุดมีคนถูกใจกี่คน'

        elif chk(keywords[7], result):
            ret = getFriendDevice(graph)
            ret['type'] = 5
            script = ""
            for x in ret['data']:
                try:
                    stmp = x['name'] + ' ใช้ ' + str(x['count'])
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'เพื่อนใช้อะไรเล่นเฟซ'

        elif chk(keywords[4], result):
            ret = getMyPostShare(graph) #['ล่าสุด', 'แชร์']
            ret['type'] = 2
            script = 'โพสต์ล่าสุดของคุณมีคนแชร์ ' + str(ret['data'][0]['count']) + ' คน'
            ret['script'] = script
            ret['sentence'] = 'โพสต์ล่าสุดมีคนแชร์กี่คน'

        elif chk(keywords[5], result):
            ret = getMyPostComment(graph) #['ล่าสุด', 'ความคิดเห็น']
            ret['type'] = 3
            script = ""
            for x in ret['data']:
                try:
                    tmp = ' ' + x['name'] + 'แสดงความคิดเห็นว่า ' + x['message']
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'โพสต์ล่าสุดมีความคิดเห็นอะไร'

        elif chk(keywords[6], result):
            ret = getFriend(graph)
            ret['type'] = 4
            script = "เพื่อนของคุณ ได้แก่"
            for x in ret['data']:
                try:
                    tmp = ' ' + x['name']
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'ขอดูเพื่อนของเราหน่อย'



        elif chk(keywords[8], result):
            ret = getFriendFriend(graph)
            ret['type'] = 6
            script = "เพื่อนของ " + ret['data'][0]['name'] + ' ได้แก่ '
            for x in ret['data'][0]['data']:
                try:
                    tmp = x['name'] + ' '
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'ขอดูเพื่อนของเพื่อน'

        elif chk(keywords[9], result):
            ret = getFriendBook(graph)
            ret['type'] = 6
            script = ''
            for x in ret['data']:
                try:
                    tmp = x['name'] + ' มีหนังสือที่ชอบคือ ' + x['data'][0]['name'] + ' '
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'ขอหนังสือที่เพื่อนชอบ'

        elif chk(keywords[10], result):
            ret = getFriendPost(graph)
            ret['type'] = 7
            script = ''
            for x in ret['data']:
                try:
                    tmp =  x['name'] + ' โพสต์ว่า ' + x['data'][0]['message'] + ' '
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'เพื่อนโพสต์อะไร'

        elif chk(keywords[11], result):
            ret = getFriendLocation(graph)
            ret['type'] = 7
            script = ''
            for x in ret['data']:
                try:
                    tmp = x['name'] + ' เช็คอินที่ ' + x['data'][0]['message'] + ' '
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'เพื่อนเช็คอินที่ไหน'

        elif chk(keywords[12], result):
            ret = getFriendLike(graph)
            ret['type'] = 6
            script = ''
            for x in ret['data']:
                try:
                    tmp = x['name'] + ' ชอบเพจ ' + x['data'][0]['name'] + ' '
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'เพื่อนชอบเพจอะไร'

        elif chk(keywords[13], result):
            ret = getMyPageLike(graph)
            ret['type'] = 5
            script = ''
            for x in ret['data']:
                try:
                    tmp = 'เพจ ' + x['name'] + ' มีคนถูกใจ ' + str(x['data'][0]['count']) + ' คน '
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'ขอจำนวนถูกใจของเพจ'

        # elif chk(keywords[14], result):
        #     ret = getMyPagePost(graph)
        #     ret['type'] = 7
        #     script = ''
        #     for x in ret['data']:
        #         try:
        #             tmp = 'เพจ ' + x['name'] + ' โพสต์ว่า ' + x['data'][0]['message'] + ' '
        #             script = script + tmp
        #         except:
        #             script = script
        #     ret['script'] = script
        #     ret['sentence'] = 'เพจโพสต์อะไร'

        elif chk(keywords[15], result):
            ret = getMyPage(graph)
            ret['type'] = 4
            script = 'เพจที่คุณชอบ ได้แก่ '
            for x in ret['data']:
                try:
                    tmp = 'เพจ ' + x['name'] + ' '
                    script = script + tmp
                except:
                    script = script
            ret['script'] = script
            ret['sentence'] = 'ขอเพจที่เราชอบ'

        if ret['type'] != -1:
            return str(ret)

    ret['data'] = "ขออีกที"
    ret['type'] = 99

    res = str(ret).replace("'",'"')
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0')
