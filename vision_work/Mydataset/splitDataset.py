import os
import random

trainval_percent = 0.9
train_percent = 0.9

# 定义文件路径
xmlfilepath = r"D:\ultralytics-8.1.0\vision_work\Mydataset\data\Annotations"
output_base_path = r"D:\ultralytics-8.1.0\vision_work\Mydataset\data\ImageSets"

# 获取所有XML文件
total_xml = os.listdir(xmlfilepath)

# 确保输出目录存在
if not os.path.exists(output_base_path):
    os.makedirs(output_base_path)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# 打开文件进行写入
with open(os.path.join(output_base_path, 'trainval.txt'), 'w') as ftrainval, \
     open(os.path.join(output_base_path, 'test.txt'), 'w') as ftest, \
     open(os.path.join(output_base_path, 'train.txt'), 'w') as ftrain, \
     open(os.path.join(output_base_path, 'val.txt'), 'w') as fval:
  
    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)

print("数据集划分完成！")