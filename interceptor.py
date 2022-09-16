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
            # 修改用户昵称为我想显示的
            user_info['data']['nick_name'] = 'Crack By MoLeft & 呆瓜'
            flow.response.text = json.dumps(user_info)

class InterceptorStartGame():
    def __init__(self):
        # 拦截闯关
        self.filter = flowfilter.parse("~u https://cat-match.easygame2021.com/sheep/v1/game/map_info")

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flowfilter.match(self.filter, flow):
            map_id = flow.request.query['map_id']
            if map_id != '80001':
                flow.request.query['map_id'] = '80001'
                print('已将关卡[%s]修改为[80001]难度降低' % (map_id))
                print('')


addons = [
    InterceptorUserProfile(),
    InterceptorStartGame()
]
