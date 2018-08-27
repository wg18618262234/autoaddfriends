import itchat
import requests

def get_response(_info):
    print(_info)                                       # 从好友发过来的消息
    api_url = 'http://www.tuling123.com/openapi/api'   # 图灵机器人网址
    data = {
        'key': '86e8ec069d1246c5b7c49407147258ff',     # 如果这个 apiKey 如不能用，那就注册一次
        'info': _info,                                 # 这是我们从好友接收到的消息 然后转发给图灵机器人
        'userid': 'wechat-robot',                      # 这里你想改什么都可以
    }
    r = requests.post(api_url, data=data).json()       # 把data数据发
    print(r.get('text'))                               # 机器人回复给好友的消息
    return r

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return "【我是天才^_^】" + get_response(msg["Text"])["text"]

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)                  # hotReload = True, 保持在线，下次运行代码可自动登录
    itchat.run()