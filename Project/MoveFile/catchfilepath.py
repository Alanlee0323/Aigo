#抓取資料夾裡面的所有檔案路徑

import os

path = "C:\\Users\\alana\\Aigo\\0902test\\新增笛鯛relabel"

dirs = os.listdir(path)
print(dirs)
# for file in dirs:
#     file_path = os.path.join(path, file)
#     print(file_path)
