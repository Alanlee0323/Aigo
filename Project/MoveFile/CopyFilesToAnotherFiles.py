#若舊資料夾裡文件內容的標籤編號在白名單內 則複製該文件到新資料夾

import shutil
import os
import numpy as np
import CopyFilesToAnotherFiles_def as df

db='E:\\魚類標記\\尚未加入train\\P4_0600' #舊資料夾
dst_db='E:\\魚類標記\\尚未加入train\\P4_0600_select' #新資料夾
white_list=[0,1,2,3]
classes = np.zeros(7)
for fname in os.listdir(db):
    with open(os.path.join(db, fname), 'r',encoding="utf-8") as f:
        
        if fname=='classes.txt': continue
        txt=f.read().split('\n')[:-1]
        
        if df.isExsisted(txt, white_list): #若編號在白名單內
            arr = [int(s.split(' ')[0]) for s in txt]
            classes[arr]+=1
            src=os.path.join(db, fname)
            dst=os.path.join(dst_db, fname)
            shutil.copyfile(src, dst) #複製檔案到指定資料夾

print(np.argwhere(classes>0))