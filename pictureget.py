import requests
import os
url = "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E8%B1%9A%E9%BC%A0&step_word=&hs=0&pn=16&spn=0&di=97415323060&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=4208957780%2C359279349&os=3436446991%2C124686831&simid=3218857814%2C281235818&adpicid=0&lpn=0&ln=1859&fr=&fmq=1539092725926_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimage14.m1905.cn%2Fuploadfile%2F2016%2F0804%2F20160804102329894456.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B8lac_z%26e3Bv54AzdH3FgjofAzdH3Fda8maba9AzdH3F8acclcl_z%26e3Bfip4s%3Fu6%3Dooofpw6_gjof_x2xo_m_da898a80&gsm=0&rpstart=0&rpnum=0&islist=&querylist="
root = "D://pictureget//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb+') as f:
            f.write(r.content)
            f.close()

    else:
        print("true")
except:
    print("wrong")