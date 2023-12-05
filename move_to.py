import os
import shutil
import fnmatch


def move(json_file, json_png_file):
    filelist = os.listdir(json_file)# 输入的参数当成目录，取得目录下的所有 json 文件
    # print(filelist)
    for i in range(len(filelist)):
        files = os.listdir(json_file + '/' + filelist[i])
        # print(files)
        for file in files:
            if fnmatch.fnmatch(file, 'label.png'):
                print(file)
                os.rename(json_file + '/' + filelist[i] + '/' + 'label.png', filelist[i][:-5] + '.png')
                shutil.move(filelist[i][:-5] + '.png', json_png_file)

if __name__ == '__main__':
    json_file = './N0114/json_data'
    json_png_file = './N0114/json_png'
    filelist = os.listdir(json_file)
    for i in range(len(filelist)):
        move(json_file, json_png_file)
