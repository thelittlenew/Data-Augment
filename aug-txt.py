import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import re

dirpath = "F:/Pitayatext/jpg/"  #jpg dir
dir_path = "F:/Pitayatext/txt/"  #txt dir
dir__list = os.listdir(dir_path)

def coordinates2yolo(xmin,ymin,xmax,ymax,img_w,img_h):
    # 保留6位小数
    x = round((xmin+xmax)/(2.0*img_w),6)
    y = round((ymin+ymax)/(2.0*img_h),6)
    w1 = round((xmax-xmin)/(1.0*img_w),6)
    h1 = round((ymax-ymin)/(1.0*img_h),6)
    #print( x,y,w1,h1)
    return x,y,w1,h1

def yolo2coordinates(x,y,w1,h1,img_w,img_h):
    xmin = round(img_w*(x-w1/2.0))
    xmax = round(img_w*(x+w1/2.0))
    ymin = round(img_h*(y-h1/2.0))
    ymax = round(img_h*(y+h1/2.0))
    #print(xmin,ymin, xmax, ymax)
    return xmin, ymin, xmax,ymax


for i in dir__list:
    if i.endswith('.txt'):
        file_name = i.replace('.txt','')
       # print(file_name)
        image = plt.imread(dirpath + file_name +'.JPG' )
        datas = []
        count = 0
        with open(dir_path + file_name + '.txt', 'r', encoding='utf-8') as f:
            for data in f.readlines():
                #print(data)
                data = data.strip('\n')
                data = data.split()
                #print(data[0],data[1],data[4])
                data[1],data[2],data[3],data[4] = yolo2coordinates( float(data[1]),float(data[2]),float(data[3]),float(data[4]),image.shape[1],image.shape[0])
                
                datas.append(data)
                count = count + 1
       # print(datas)
       # print(image.shape)    #shape[0]是高   shape[1]是宽
        if count == 1:
            bbs = BoundingBoxesOnImage([
                BoundingBox(x1= datas[0][1] , y1= datas[0][2] , x2= datas[0][3] , 
                            y2= datas[0][4] ,label=datas[0][0])
            ], shape=image.shape)

        if count == 2:
            bbs = BoundingBoxesOnImage([
                BoundingBox(x1= datas[0][1] , y1= datas[0][2] , x2= datas[0][3] , 
                            y2= datas[0][4] ,label=datas[0][0]),
                BoundingBox(x1= datas[1][1] , y1= datas[1][2] , x2= datas[1][3] , 
                            y2= datas[1][4] ,label=datas[1][0])
            ], shape=image.shape)

        if count == 3:
            bbs = BoundingBoxesOnImage([
                BoundingBox(x1= datas[0][1] , y1= datas[0][2] , x2= datas[0][3] , 
                            y2= datas[0][4] ,label=datas[0][0]),
                BoundingBox(x1= datas[1][1] , y1= datas[1][2] , x2= datas[1][3] , 
                            y2= datas[1][4] ,label=datas[1][0]),
                BoundingBox(x1= datas[2][1] , y1= datas[2][2] , x2= datas[2][3] , 
                            y2= datas[2][4] ,label=datas[2][0])
            ], shape=image.shape)

        if count == 4:
            bbs = BoundingBoxesOnImage([
                BoundingBox(x1= datas[0][1] , y1= datas[0][2] , x2= datas[0][3] , 
                            y2= datas[0][4] ,label=datas[0][0]),
                BoundingBox(x1= datas[1][1] , y1= datas[1][2] , x2= datas[1][3] , 
                            y2= datas[1][4] ,label=datas[1][0]),
                BoundingBox(x1= datas[2][1] , y1= datas[2][2] , x2= datas[2][3] , 
                            y2= datas[2][4] ,label=datas[2][0]),
                BoundingBox(x1= datas[3][1] , y1= datas[3][2] , x2= datas[3][3] , 
                            y2= datas[3][4] ,label=datas[3][0])
            ], shape=image.shape)

        if count == 5:
            bbs = BoundingBoxesOnImage([
                BoundingBox(x1= datas[0][1] , y1= datas[0][2] , x2= datas[0][3] , 
                            y2= datas[0][4] ,label=datas[0][0]),
                BoundingBox(x1= datas[1][1] , y1= datas[1][2] , x2= datas[1][3] , 
                            y2= datas[1][4] ,label=datas[1][0]),
                BoundingBox(x1= datas[2][1] , y1= datas[2][2] , x2= datas[2][3] , 
                            y2= datas[2][4] ,label=datas[2][0]),
                BoundingBox(x1= datas[3][1] , y1= datas[3][2] , x2= datas[3][3] , 
                            y2= datas[3][4] ,label=datas[3][0]),
                BoundingBox(x1= datas[4][1] , y1= datas[4][2] , x2= datas[4][3] , 
                            y2= datas[4][4] ,label=datas[4][0])
            ], shape=image.shape)



        seq = iaa.SomeOf(2,[  
        #iaa.Multiply((1.2, 1.5)), # 改变亮度
        iaa.AdditiveGaussianNoise(scale=0.001*255), #高斯噪音
        #iaa.Fliplr(1), #水平翻转 概率50%
        iaa.Flipud(1), #垂直翻转 概率50%
        iaa.Affine(scale=(0.5, 0.7)),  #缩放图像为其原始大小的50%至70%
        iaa.Affine(rotate=(90))
      #  translate_px={"x": 40, "y": 60}, #独立地在x轴和y轴上将图像平移40与60像素
      #  rotate=(-45, 45), #将图像旋转45到45度
      #  shear=(-16, 16), #剪切图像-16至16度            
        ])
        # Augment BBs and images.
        image_aug, bbs_aug = seq(image=image, bounding_boxes=bbs)

        
        for k in range(len(bbs.bounding_boxes)):
            
            #before = bbs.bounding_boxes[i]
            after = bbs_aug.bounding_boxes[k]
          #  print(after)
            datas[k][0] = np.int32(after.label)
            datas[k][1],datas[k][2],datas[k][3],datas[k][4] = coordinates2yolo( after.x1, after.y1, after.x2, after.y2, image.shape[1], image.shape[0])
            
        #print(datas)

        f.close()
        
        with open(dir_path + 'aug/' +'aug_' + file_name + '.txt','w', encoding='utf-8') as w:
           for a in range(count):
               for b in range(5):
                   w.write(str(datas[a][b])+' ')
               w.write('\n')
        w.close()
        plt.imshow(image_aug)
        plt.axis('off')        
        plt.savefig(dirpath + 'aug/' +'aug_'+ file_name + '.jpg',dpi=258.25 , bbox_inches = 'tight',pad_inches = 0)
        print (file_name)

    else:
        continue