import itchat

def get_friends_info():
    friends = itchat.get_friends()
    for i in friends:
        print(i)
if __name__ == '__main__':
    itchat.auto_login(True)
    get_friends_info()
    itchat.run(True)