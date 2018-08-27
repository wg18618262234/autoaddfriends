import itchat, time
from itchat.content import TEXT
#name = ' '
roomslist = []

itchat.auto_login(enableCmdQR = False)

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

def getroom_message(n):
    #获取群的username，对群成员进行分析需要用到
    itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    RoomList =  itchat.search_chatrooms(name=n)

    print(itchat.dump_login_status())

    if RoomList is None:
        print("%s group is not found!" % (name))
    else:
        return RoomList[0]['UserName']

def getchatrooms():
    #获取群聊列表
    roomslist = itchat.get_chatrooms()
    #print(roomslist)
    return roomslist



for i in getchatrooms():
    #print(i['NickName'])
    roomslist.append(i['NickName'])

with open('群用户名.txt', 'a', encoding='utf-8')as f:
    for n in roomslist:
        ChatRoom = itchat.update_chatroom(getroom_message(n), detailedMember=True)
        for i in ChatRoom['MemberList']:
            #print (i['Province']+":",i['NickName'])
            f.write(i['Province']+":"+i['NickName']+'\n')
            print('正在写入           '+i['Province']+":",i['NickName'])
    f.close()

if __name__ == '__main__':\
    # itchat.auto_login(hotReload=True)
    itchat.auto_login()
    itchat.run()