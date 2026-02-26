#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片批量处理脚本

功能：
1. 把所有图片分辨率缩放到 1024×1024（保持宽高比，不拉伸）
2. 把 PNG 格式转换成 JPG 格式，质量设为 80%
3. 处理后的图片保存到新文件夹，不覆盖原图

使用方法：
1. 安装依赖：pip install Pillow
2. 修改脚本中的 input_dir 和 output_dir 变量为实际路径
3. 运行脚本：python image_processor.py
"""

import os
from PIL import Image

# 输入文件夹路径
input_dir = r"d:\GodotProjects\new"
# 输出文件夹路径
output_dir = r"d:\GodotProjects\new\processed_images"

# 确保输出文件夹存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"创建输出文件夹: {output_dir}")

# 支持的图片格式
supported_formats = ['.png', '.jpg', '.jpeg']

# 目标尺寸
target_size = (1024, 1024)

# 处理图片的函数
def process_image(input_path, output_path):
    """处理单个图片"""
    try:
        # 打开图片
        img = Image.open(input_path)
        print(f"处理图片: {os.path.basename(input_path)}")
        
        # 计算缩放后的尺寸（保持宽高比）
        img.thumbnail(target_size, Image.Resampling.LANCZOS)
        
        # 创建一个1024x1024的白色背景
        new_img = Image.new('RGB', target_size, (255, 255, 255))
        
        # 计算图片在背景中的位置（居中）
        paste_x = (target_size[0] - img.width) // 2
        paste_y = (target_size[1] - img.height) // 2
        
        # 将缩放后的图片粘贴到背景上
        new_img.paste(img, (paste_x, paste_y))
        
        # 保存为JPG格式，质量80%
        new_img.save(output_path, 'JPEG', quality=80)
        print(f"保存处理后的图片: {os.path.basename(output_path)}")
        
    except Exception as e:
        print(f"处理图片 {os.path.basename(input_path)} 时出错: {e}")

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_dir):
    # 获取文件扩展名
    ext = os.path.splitext(filename)[1].lower()
    
    # 检查是否是支持的图片格式
    if ext in supported_formats:
        # 输入文件路径
        input_path = os.path.join(input_dir, filename)
        
        # 输出文件路径（改为jpg格式）
        output_filename = os.path.splitext(filename)[0] + '.jpg'
        output_path = os.path.join(output_dir, output_filename)
        
        # 处理图片
        process_image(input_path, output_path)

print("\n图片处理完成！")
print(f"处理后的图片保存在: {output_dir}")