import os
import shutil
db='C:\\Users\\alana\\Aigo\\VOCdevkit\\VOC2007\\YOLO' #預複製檔的位置
dst_db = 'C:\\Users\\alana\\Aigo\\FIsh\\labels\\train'   #要放複製檔的位置
#E:\\魚類標記\\0818_test\\alllabelled
files = os.listdir(db)

arr = None  #目錄，類似之前yolo v4的train.txt那樣，裡面寫上檔案位置
with open("C:\\Users\\alana\\Aigo\\yolov5_val.txt", 'r') as f:
    arr = f.read().split('\n')

    for data in files:     #跟db資料夾的檔案做比對，有符合的就會複製一份到dst_db那裏
        if data in arr:
            src = os.path.join(db, data)
            dst=os.path.join(dst_db, data)
            shutil.copyfile(src, dst)