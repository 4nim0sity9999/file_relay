from NapCat_Server import Send_Class
from MyLib import DictView
import re
from requests import post

black = []
def sender1(dst,num:int,msg,tm):
    global black
    for i in range(num):
        Send_Class().send_private_msg(dst,msg)
    black.append(tm)

def sender2(dst,num:int,msg,tm):
    global black
    for i in range(num):
        Send_Class().send_group_msg(dst,msg)
    black.append(tm)


head = {
    "Authorization": "Bearer 1"
}
dic = {
  "user_id": "1574822637",
  "message_seq": 0,
  "count": 5,
}
url = "http://192.168.1.19:3000/get_friend_msg_history"


def main():
    result = DictView(post(url,headers=head,data=dic).json(),"data.messages").get()[-1]
    x = result["raw_message"].split(" ")  #命令format : Command user\group_send_many /dst /num /content
    time = result["time"]
    if time not in black:
        if x[1] == "user_send_many":
            sender1(x[2],int(x[3]),x[4],time)
        elif x[1] == "group_send_many":
            sender2(x[2],int(x[3]),x[4],time)
    #     print("Done")

    # if x[0] == 'Command' and time not in black:
    #     send_many(x[2],int(x[3]),x[4],time)
    #     print("Done")

if __name__ == "__main__":
    while True:
        main()