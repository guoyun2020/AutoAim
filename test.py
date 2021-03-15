import paddlex as pdx
import numpy as np
from PIL import ImageGrab
from time import *
import pyautogui
import cv2


model = pdx.load_model('model')
BOX=(0,0,1920,1080)

#左上角坐标和右下角坐标
#调整box的值即可改变截取区域

while True:
    screen = np.array(ImageGrab.grab(bbox=BOX))
    begin_time = time()
    result = model.predict(screen)
    predict_end_time = time()
    predict_run_time = predict_end_time - begin_time
    print('predict_run_time:',predict_run_time)
    for i in result:
        if float(i['score']) > 0.5 and i['category'] == 'CT':
            print('Found target!')
            point_x = i['bbox'][0] + 0.5 * i['bbox'][2]
            point_y = i['bbox'][1] + 0.4 * i['bbox'][3]
            print('Locking target!')
            pyautogui.moveTo(point_x, point_y)
            pyautogui.moveTo(960, 540)
            for num in range(5):
                print('shot!')
                pyautogui.click()
        else:
            continue
    # vis = pdx.det.visualize(screen, result, threshold=0.5,save_dir=None)
    # vis_resize=cv2.resize(vis,(800,500))
    visulize_end_time = time()
    visulize_run_time = visulize_end_time - predict_end_time
    # cv2.imshow("window", cv2.cvtColor(vis_resize,cv2.COLOR_BGR2RGB))
    # cv2.waitKey(10)

