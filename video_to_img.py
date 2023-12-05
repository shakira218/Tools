# -*- coding: UTF-8 -*-
import os
import cv2
import skimage.io as io


# 视频文件夹名,保存的图片文件夹名
def avi_to_png(video_folder, png_folder, video_name, video_type):
    path = video_folder + video_name + video_type  # 视频路径
    video = cv2.VideoCapture(path)  # 获取视频
    ret = True  # 设置ret初始值
    i = 0
    png_path = png_folder + "/" + video_name
    file_exists = os.path.isdir(png_path)
    if not file_exists:
        os.makedirs(png_path)

    while ret:  # 当ret为True时(没读到末尾),继续读取
        ret, frame = video.read()  # videoCapture.read()按帧读取视频
        # ret, frame是获cap.read()方法的两个返回值。   # 其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。
        # 其中frame是每一帧的图像，是个BGR三维矩阵。
        if ret:  # 当读取到图像时
            #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # RGB格式
            # img_introduce("读取的值", img)  # 该数据是值为0~ 255 的 (480, 640) 型 2 维 多值 矩阵,元素类型为: uint8
            # io.imsave(png_path + "/" + video_name + "_{:05d}.png".format(i), img)
            cv2.imwrite(png_path + "/" + video_name + "_{:05d}.png".format(i), frame)
            i += 1


def avi_to_png2(video_folder, png_path, video_name, video_type):
    path = video_folder + video_name + video_type  # 视频路径
    video = cv2.VideoCapture(path)  # 获取视频
    ret = True  # 设置ret初始值

    # png_path = png_path + "/" + video_name
    print(png_path)
    file_exists = os.path.isdir(png_path)
    if not file_exists:
        os.makedirs(png_path)

    i = 0
    while ret:  # 当ret为True时(没读到末尾),继续读取
        ret, frame = video.read()
        print(ret)
        if ret:  # 当读取到图像时
            # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # RGB格式
            cv2.imwrite(png_path + "/" + video_name + "_{:05d}.png".format(i), frame)
            i += 1
        if i == 15:
            break


if __name__ == "__main__":
    videos_folder = "./"
    pngs_folder = "./"
    videos_type = ".avi"
    videos_names = os.listdir(videos_folder)  # 获取当前路径下的文件名，返回List
    for n in range(len(videos_names)):
        if ".avi" in videos_names[n]:
            print("videos_names[n]", videos_names[n])
            video_name_n = videos_names[n][:-4]
            print(n, "正在执行{}视频转png".format(video_name_n))
            avi_to_png(videos_folder, pngs_folder, video_name_n, videos_type)

    path = "./"
    videos_names = os.listdir(path)
    for videos_name in videos_names:
        print(videos_name)

    # path = "./"
    # file_names = os.listdir(path)
    # for video_name in file_names:
    #     if "avi" in video_name:
    #         video_name = video_name[:-4]
    #         png_folder = "./" + video_name + "/"
    #         # os.makedirs(png_folder)
    #         avi_to_png2(path, png_folder, video_name, ".avi")
