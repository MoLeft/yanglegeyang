import mitmproxy.http
import json
from mitmproxy import ctx
from mitmproxy import flowfilter

class InterceptorUserProfile:

    token = ''

    def __init__(self):
        # 拦截用户信息
        self.filter = flowfilter.parse("~u https://cat-match.easygame2021.com/sheep/v1/game/personal_info")

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flowfilter.match(self.filter, flow):
            print("已拦截到羊了个羊的用户数据：")
            self.token = flow.request.headers['t']

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flowfilter.match(self.filter, flow):  
            user_info = json.loads(flow.response.text)
            print('用户名：' + user_info['data']['nick_name'])
            print('UID：' + str(user_info['data']['uid']))
            print('token：'+self.token)
            print('')
            
            user_info['data']['nick_name'] = 'Crack By MoLeft & 呆瓜'
            flow.response.text = json.dumps(user_info)

# 旧版
class InterceptorStartGame():
    def __init__(self):
        # 拦截闯关
        self.filter = flowfilter.parse("~u https://cat-match.easygame2021.com/sheep/v1/game/map_info\?")

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flowfilter.match(self.filter, flow):
            map_id = flow.request.query['map_id']
            if map_id != '80001':
                flow.request.query['map_id'] = '80001'
                print('已将关卡[%s]修改为[80001]难度降低' % (map_id))
                print('')

# 新版
class InterceptorStartNewGame():
    def __init__(self):
        # 拦截新闯关
        self.filter = flowfilter.parse("~u https://cat-match.easygame2021.com/sheep/v1/game/map_info_ex\?")

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flowfilter.match(self.filter, flow):
            pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flowfilter.match(self.filter, flow):
            game_data = json.loads(flow.response.text)
            if game_data['err_code'] == 0:
                print("已将关卡[%s]修改为[%s]难度降低" % (game_data['data']['map_md5'][1], game_data['data']['map_md5'][0]))
                game_data['data']['map_md5'][1] = game_data['data']['map_md5'][0]
                flow.response.text = json.dumps(game_data)
                print()

addons = [
    InterceptorUserProfile(),
    InterceptorStartGame(),
    InterceptorStartNewGame()
]
