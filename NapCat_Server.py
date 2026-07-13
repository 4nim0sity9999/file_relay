import time
import requests

white = [1107993188,1574822637,2794561699]
ip = "http://192.168.1.19:3000"

class Send_Class:
    def post(self,addr,data):
        """post再封装"""
        result =requests.post(addr,json = data)
        return result.content

    def send_private_msg(self,user_id,msg):
        """私法消息"""
        jsons ={
        "user_id": str(user_id),
        "message": msg
        }
        self.post(ip+"/send_private_msg",jsons)

    def send_group_msg(self,group_id,msg):
        """群发消息"""
        jsons = {
            "group_id" : str(group_id),
            "message" : msg
        }
        self.post(ip+"/send_group_msg",jsons)

    def send_group_sign(self,group_id):
        """群打卡"""
        jsons = {
            "group_id":group_id
        }
        self.post(ip+"/send_group_sign",jsons)

class Group_Operation:
    def __init__(self,id):
        self.group_id = id
        self.group_members = None
        self.delta = 777600 #限制时间
        self.now = int(time.time())

    def get(self,addr):
        """get再封装"""
        result = requests.get(addr)
        return result
    
    def post(self,addr,data):
        """post再封装"""
        result =requests.post(addr,json = data)
        return result
    
    def get_group_member_list(self,):
        """获取群成员"""
        json = {
            "group_id":self.group_id
        }
        r = self.post(ip+"/get_group_member_list",json).json()['data']
        print(r)
        self.group_members =[{'usr_id':m['user_id'],'last_sent_time':m['last_sent_time']}for m in r]

    def set_group_kick_members(self):
        """剔除无效用户(三个月)"""
        invalid_user = [
            x['usr_id'] for x in self.group_members if x['last_sent_time']+self.delta < self.now and x['usr_id'] not in white
        ]
        json = {
            "group_id":self.group_id,
            "user_id" :[
                x for x in invalid_user
            ],
            "reject_add_reques": False
        }
        self.post(ip+"/set_group_kick_members",json)
