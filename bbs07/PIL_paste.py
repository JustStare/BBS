from PIL import Image
from AI_img_api import AI_img2nobg
import time
### 新生成的图片是 "output + 当前时间 + 原来图片名称.png"
def composite_picture(base_pic, fill_pic,fill_pic_x,fill_pic_y,fill_pic_width,fill_pic_high):
    # 加载底图
    base_img = Image.open(base_pic)
    base_img = base_img.convert("RGBA")   ## 转化成为RGBA
    ### 图片格式都是 RGBA 在paste 时候就可以 兼容！！
    box = (fill_pic_x,fill_pic_y,fill_pic_width,fill_pic_high)  # 底图上需要P掉的区域  长,高,长,高

    # 加载需要P上去的图片
    tmp_img = Image.open(fill_pic)
    tmp_img= tmp_img.convert("RGBA")
    region = tmp_img  # 或者使用整张图片 # region = tmp_img.crop((0,0,100,100)) # 选择一块区域

    # 使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
    # 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。
    # 如果需要保留透明度，则使用RGMA mode
    # 提前将图片进行缩放，以适应box区域大小
    # region = region.rotate(180) # 对图片进行旋转

    region = region.resize((box[2] - box[0], box[3] - box[1]))
    r, g, b, a = region.split()
    base_img.paste(region, box,mask=a)

    # base_img.show()  # 查看合成的图片
    dt = time.strftime("%Y年%m月%d日%X")
    print(dt)

    nt = dt.replace(":","时",1)
    nt = nt.replace(":", "分", 1)
    nt = nt+"秒"
    print(nt)
    new_pic ="output"+nt+fill_pic[5:]
    base_img.save(new_pic)  # 保存图片
    print(f"合成图片成功，新图片：{new_pic}")
    return new_pic