# trans_labelme_to_yolo.py

import cv2
import os
import json
import shutil
import numpy as np
from pathlib import Path
from glob import glob
 
id2cls = {1: '1'}
cls2id = {'1': 1}
 
#支持中文路径
def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),flags=cv2.IMREAD_COLOR)
    return cv_img
 
def labelme2yolo_single(img_path,label_file):
    anno= json.load(open(label_file, "r", encoding="utf-8"))
    shapes = anno['shapes']
    w0, h0 = anno['imageWidth'], anno['imageHeight']
    image_path = os.path.basename(img_path + anno['imagePath'])
    labels = []
    for s in shapes:
        pts = s['points']
        x1, y1 = pts[0]
        x2, y2 = pts[1]
        x = (x1 + x2) / 2 / w0 
        y = (y1 + y2) / 2 / h0
        w  = abs(x2 - x1) / w0
        h  = abs(y2 - y1) / h0
        cid = cls2id[s['label']]        
        labels.append([cid, x, y, w, h])
    return np.array(labels), image_path
 
def labelme2yolo(img_path,labelme_label_dir, save_dir='res/'):
    labelme_label_dir = str(Path(labelme_label_dir)) + '/'
    save_dir = str(Path(save_dir))
    yolo_label_dir = save_dir + '/'
    """ yolo_image_dir = save_dir + 'images/'
    if not os.path.exists(yolo_image_dir):
        os.makedirs(yolo_image_dir) """
    if not os.path.exists(yolo_label_dir):
        os.makedirs(yolo_label_dir)
 
    json_files = glob(labelme_label_dir + '*.json')
    for ijf, jf in enumerate(json_files):
        print(ijf+1, '/', len(json_files), jf)
        filename = os.path.basename(jf).rsplit('.', 1)[0]
        labels, image_path = labelme2yolo_single(img_path,jf)
        if len(labels) > 0:
            np.savetxt(yolo_label_dir + filename + '.txt', labels)
            # shutil.copy(labelme_label_dir + image_path, yolo_image_dir + image_path)
    print('Completed!')
    
if __name__ == '__main__':
    img_path = 'D:/ultralytics-8.1.0/vision_work/train_img/'    # 数据集图片的路径
    json_dir = 'D:/ultralytics-8.1.0/vision_work/result_json/'    # json标签的路径
    save_dir = 'D:/ultralytics-8.1.0/vision_work/result_yolo/'     # 保存的txt标签的路径
    labelme2yolo(img_path,json_dir, save_dir)
