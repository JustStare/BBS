import os
import paddlehub as hub
import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 获取需要抠图的图像文件地址
# 图像文件目录地址
path = r'./img/'
# 遍历获取每张图像的地址
files = [path + i for i in os.listdir(path)]

# 显示所有原图像
# 保存图像数据列表
img = []
# 创建画布  定义大小
plt.figure(figsize=(8, 6))
# 遍历获取每张图像数据
for i, img_fine in enumerate(files):
    # 通过opencv获取图像数据并添加到列表
    img.append(cv2.imread(img_fine))
    # 由于opencv打开的图像格式为BGR 所以需要转换为RGB格式
    img[i] = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
    # 显示图像大小
    # print(img[i].shape)
    # 创建子视图
    plt.subplot(2, len(files), i + 1)
    # 显示图像
    plt.imshow(img[i])
    plt.title("原图")


# 调用飞浆的deeplabv3p_xception65_humanseg模型 该模型能够用于人像抠图
module = hub.Module(name="deeplabv3p_xception65_humanseg")
# 图像地址 （固定格式，不要更改）
input_dict = {"image": files}
# 训练模型并预测模型，打印结果（获取到抠图人像）
results = module.segmentation(data=input_dict)

# 列表存储抠图人像（方便保存数据，也可下载图像）
newimgs = []
for i in range(len(files)):
    # 提取抠图人像数据
    prediction = results[i]["data"]
    # 显示抠图后的轮廓图像
    # plt.imshow(prediction)
    # 根据图像成像还原数据（具体原理我也不知道）
    newimg = np.zeros(img[i].shape)
    newimg[:, :, 0] = img[i][:, :, 0] * (prediction > 0)
    newimg[:, :, 1] = img[i][:, :, 1] * (prediction > 0)
    newimg[:, :, 2] = img[i][:, :, 2] * (prediction > 0)

    # 添加到列表 newimg.astype(np.uint8)修改数据类型为uint8
    newimgs.append(newimg.astype(np.uint8))
    # 显示图像
    plt.subplot(2, len(files), i + 1 + len(files))
    plt.imshow(newimgs[i])
    plt.xlabel("抠图后图像")

# 总图像显示（少了这个就没图像了，千万别少了）
plt.show()
