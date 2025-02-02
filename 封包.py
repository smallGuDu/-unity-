import os

def process_unity3d_files(directory):
    # 遍历指定目录及其所有子目录
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".unity3d"):#如果是asset文件的话可以改成asset
                file_path = os.path.join(root, filename)
                # 打开文件，读取内容
                with open(file_path, 'rb') as file:
                    content = file.read()
                
                # 在内容前面添加8个空字节
                modified_content = b"\x00" * 8 + content
                
                # 将修改后的内容写回文件
                with open(file_path, 'wb') as file:
                    file.write(modified_content)
                print(f"Processed {file_path}")

# 指定要处理的目录
directory_path = "D:\新建文件夹\Bundles\skins\新建文件夹"  # 替换为你的目录路径

# 调用函数处理文件
process_unity3d_files(directory_path)
