import os
import Catchnumber_def as Ch



black_list = []
white_list = [0,1,3,4]

for fname in os.listdir(Ch.db):  # os.listdir() 用於返回指定文件夾的文件或文件夾的名字的方法列表。
    with open(os.path.join(Ch.db, fname), 'r') as f:  # os.path.join() 連接兩個或更多的路徑名組件
        if fname == 'classes.txt':
            continue
        if Ch.isExsisted(f, white_list):
            print(os.path.join(Ch.db, fname))

# 石斑:19,20,21,22,65 >> 0
# 笛鯛:54,55,77 >> 1
# 蝶魚:4~13,73,78 >> 2  
# 鸚哥魚:14~18 >> 3 
# 老鼠斑: 70 >> 4
# 非目標魚種: >> 5
# 霓虹雀鯛: >> 6
# 燕尾光鰓雀鯛: >> 7