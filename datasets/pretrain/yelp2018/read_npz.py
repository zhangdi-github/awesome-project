import numpy as np

# 使用绝对路径来指定文件位置
file_path = 'C:/Users/Dell/Desktop/KG+AT/datasets/pretrain/yelp2018/mf.npz'

# 加载 npz 文件
archive = np.load(file_path)

# 查看存档中的所有数组名称
print("Arrays in archive:", archive.files)

# 遍历存档中的数组，并打印数组的形状和数据类型
for key in archive.files:
    array = archive[key]
    print(f"Array '{key}' shape:", array.shape)
    print(f"Array '{key}' dtype:", array.dtype)
    print(f"Array '{key}' data:")
    print(array)
    print()



