import os

def process_unity3d_files(directory):
    # 遍历指定目录及其所有子目录
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".unity3d"):
                file_path = os.path.join(root, filename)
                # 打开文件，读取内容
                with open(file_path, 'rb') as file:
                    content = file.read()
                
                # 检查文件是否至少有7个字节
                if len(content) >= 7:
                    # 删除前7个字节
                    modified_content = content[8:]
                    
                    # 将修改后的内容写回文件
                    with open(file_path, 'wb') as file:
                        file.write(modified_content)
                    print(f"Processed {file_path}")
                else:
                    print(f"File {file_path} is too short to remove 7 bytes.")

# 指定要处理的目录
directory_path = "D:\新建文件夹\Bundles\skins\新建文件夹"  # 替换为你的目录路径

# 调用函数处理文件
process_unity3d_files(directory_path)