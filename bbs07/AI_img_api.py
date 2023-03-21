import requests
import os
import time
import requests
import base64
import requests
import io
from PIL import Image


# 转化后图片名称是 nobg_ + 原来文件名称.png
# def AI_img2nobg(PIL_name):
    #
    # key = 'c6vLHWNS7fDFAvoMXk3uo4mB'  ##
    # dt = time.strftime("%Y年%m月%d日%X")
    # print(dt)
    #
    # nt = dt.replace(":", "时", 1)
    # nt = nt.replace(":", "分", 1)
    # nt = nt + "秒"
    # print(nt)
    # new_file_name = os.path.join('./static/img/nohuman/nobg_'+nt+PIL_name)
    # with open(PIL_name, 'rb') as f:
    #     response = requests.post(
    #         'https://api.remove.bg/v1.0/removebg',
    #         files={'image_file': f},
    #         data={
    #             'size': "regular",
    #             'bg_color': None
    #         },
    #         headers={'X-Api-Key': key})
    #     with open(new_file_name, 'wb') as removed_bg_file:
    #          removed_bg_file.write(response.content)
    # return new_file_name

    # encoding:utf-8


def AI_img2nobg(img_name):




    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"


    # 二进制方式打开图片文件
    f = open(img_name, 'rb')
    img = base64.b64encode(f.read()) # 使用base64 编码




    params = {"image": img}
    access_token = '[24.2b26d773c2f13dadfcc1b670117aaf8d.2592000.1673771311.282335-29097173]' ## asscee_token
        # 这个是百度 的接口 需要自己获取

    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        res = response.json()
        img = res["foreground"]
        # print(response.json())
        print(img)
        imgdata = base64.b64decode(img)
        image = io.BytesIO(imgdata)
        image = Image.open(image)
        with open("imageToSave.png", "wb") as fh:
            fh.write(imgdata)


############# 这个是获取token的代码
def get_token():
    # encoding:utf-8


    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EoGyIsKLL98l0L5xGxFKvA4x&client_secret=BhfGTVAQkvyhsbThDLtxudMaSL09BBpq&'
    response = requests.get(host)
    if response:
        retxt = response.json()
        print(response.json())

    access_token = retxt["access_token"]
    print(access_token)
    return access_token

if __name__ == '__main__':
    AI_img2nobg(r"E:\code\bbs07\bbs07\weqeqq.png")