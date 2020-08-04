import os

# 获取当前目录
# print(os.getcwd())

# 修改当前工作目录
os.chdir('/Users/daixin/Desktop/Pictures/')

basePath = os.getcwd()

print(basePath)

print('遍历文件开始....')

for pathdir in os.listdir(basePath):
    # 拼接出文件的绝对路径
    newdir = basePath + pathdir
    if os.path.isfile(pathdir) and os.path.splitext(pathdir)[1] == '.png':
        # print(os.path.splitext(pathdir)[0])
        # print(os.path.splitext(pathdir)[1])
        # print(os.path.splitext(newdir)[0])
        # print(os.path.splitext(newdir)[1])
        os.rename(pathdir, os.path.split(newdir)[1].split('.')[0] + '.jpg')

print('遍历文件结束....')