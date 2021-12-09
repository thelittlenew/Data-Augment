import cv2
import numpy as np
import os, shutil
 
def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))
 
# 遍历某文件夹下所有文件名，包括子文件夹下的文件名
def rotate_imagine(raw_img_path, save_img_path, angle):
    now_file_path = raw_img_path
    for dirpath, dirnames, filenames in os.walk(now_file_path):
        for filename in filenames:
            file_path = now_file_path + filename
            img = cv2.imread(file_path)
            if(img.shape[0]>img.shape[1]):
                img_rotate = rotate_bound(img, angle)
                save_file_path = save_img_path + filename
                cv2.imwrite(save_file_path, img_rotate)
 

angle = 90
raw_img_path = "F:/Pitaya/shuju/jpg/"
save_img_path = "F:/Pitaya/shuju/after/"
if(os.path.exists(save_img_path)):
    shutil.rmtree(save_img_path)
os.mkdir(save_img_path)
rotate_imagine(raw_img_path, save_img_path, angle)
 
 
 
 
 
 
 
 
