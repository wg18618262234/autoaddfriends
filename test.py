import itchat

itchat.auto_login(hotReload=True)

#itchat.run()

mpsList=itchat.get_chatrooms(update=True)[1:]

total=0
for it in mpsList:
    print(it['NickName'])
    total=total+1

print('群聊的数目是%d'%total)

#显示所有的群聊，包括未保存在通讯录中的，如果去掉则只是显示在通讯录中保存的
itchat.dump_login_status()

if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()