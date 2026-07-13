import datetime
from NapCat_Server import Send_Class

cat = Send_Class()

while True:
    now= str(datetime.datetime.now().time()).split(".")
    if now[0] =="00:00:00" and now[1]>400000:
        cat.send_group_sign(437291467)