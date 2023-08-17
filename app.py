#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import cv2
import numpy as np
import pyautogui as pag


def main():
    # 保存するファイル名
    timestr = time.strftime("%Y%m%d-%H%M%S")
    img_dir_name = "./formovie"+timestr

    # 画像保存用ファイルを作成
    os.makedirs(img_dir_name, exist_ok=True)

    # 動画用の画像（スクリーンショット）を用意
    # 画像を格納するリスト
    img_list = []
    img_No = 0
    # 動画のフレームレイト
    FPS = 5
    # 録画したい時間
    movie_time = 10
    # 上記フレームレイトと録画時間を満たす繰り返し数
    photo_no = FPS*movie_time

    # デスクトップ画面の縦横の大きさを取得
    img = pag.screenshot()
    img = np.asarray(img)
    img_height, img_width, channels = img.shape

    # 繰り返しスクリーンショットを撮り、ファイルに保存
    for i in range(0, photo_no, 1):
        img_No = img_No + 1
        img = pag.screenshot()
        img = np.asarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img_output = '{}/{:010d}.png'.format(img_dir_name, img_No)
        cv2.imwrite(img_output, img)
        img_list.append(img_output)

    # 保存された画像を繋げて動画作成
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter('desktop_capture.mp4', fourcc,
                            FPS, (img_width, img_height))
    for s in img_list:
        img = cv2.imread(s)
        video.write(img)

    video.release()


if __name__ == '__main__':
    main()
