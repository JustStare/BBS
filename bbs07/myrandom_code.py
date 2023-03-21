from PIL import  Image,ImageDraw,ImageFont
import  random
def get_random_color():
    # 获取随机的颜色  RGB
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def random_code():
    img_obj = Image.new('RGB', (430, 35),(255,255,255))
    img_draw = ImageDraw.Draw(img_obj)  # 产生一个画笔对象
    img_font = ImageFont.truetype('static/font/222.ttf', 30)  # 字体样式


    random_int_first = str(random.randint(10, 99))
    # 从上面的三个里面随机选择一个

    # 将产生的随机字符串写到图片上
    # '''一个一个去写入'''
    img_draw.text((30, 0),random_int_first, get_random_color(), img_font)
    # 拼接随机字符串
    random_int_second = str(random.randint(10, 99))
    img_draw.text((45+30, 0),"+", get_random_color(), img_font)

    img_draw.text((45*2+30, 0),random_int_second, get_random_color(), img_font)
    img_draw.text((45*3+30,0),"=",get_random_color(),img_font)
    code = str(random_int_first) +"+"+ str(random_int_second)

    # 添加干扰点和线
    width = 320
    height = 35
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        img_draw.line((x1, y1, x2, y2), fill=get_random_color())

    for i in range(55):
        x = random.randint(0, width)
        y = random.randint(0, height)
        img_draw.point((x, y), fill=get_random_color())

    print(code)
    code_sum = print(eval(random_int_first)+eval(random_int_second))
    code_list = []  # 返回的列表
    code_list.append(code)   # 76+23  =  验证码图片中的字符串
    code_list.append(code_sum)   # 99
    code_list.append(img_obj)    # img 对象

    return code_list
