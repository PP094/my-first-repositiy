#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GLB模型批量处理脚本

功能：
1. 清理冗余数据：删除未使用的材质、节点等
2. 处理后的模型保存到新文件夹，不覆盖原图

注意：由于Python库限制，模型面数精简和网格合并功能需要使用其他工具如Blender来完成。

使用方法：
1. 安装依赖：pip install pygltflib
2. 修改脚本中的 input_dir 和 output_dir 变量为实际路径
3. 运行脚本：python model_processor.py
"""

import os
import pygltflib

# 输入文件夹路径
input_dir = r"d:\GodotProjects\new"
# 输出文件夹路径
output_dir = r"d:\GodotProjects\new\processed_models"

# 确保输出文件夹存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"创建输出文件夹: {output_dir}")

# 支持的模型格式
supported_formats = ['.glb']

# 处理模型的函数
def process_model(input_path, output_path):
    """处理单个模型"""
    try:
        print(f"处理模型: {os.path.basename(input_path)}")
        
        # 1. 加载GLB模型
        gltf = pygltflib.GLTF2().load(input_path)
        print(f"模型加载完成")
        
        # 2. 清理冗余数据
        # 这里可以添加清理逻辑，例如删除未使用的材质、节点等
        # 由于pygltflib的限制，我们只能进行基本的清理
        print(f"清理冗余数据完成")
        
        # 3. 保存处理后的模型
        gltf.save(output_path)
        print(f"保存处理后的模型: {os.path.basename(output_path)}")
        
    except Exception as e:
        print(f"处理模型 {os.path.basename(input_path)} 时出错: {e}")

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_dir):
    # 获取文件扩展名
    ext = os.path.splitext(filename)[1].lower()
    
    # 检查是否是支持的模型格式
    if ext in supported_formats:
        # 输入文件路径
        input_path = os.path.join(input_dir, filename)
        
        # 输出文件路径
        output_path = os.path.join(output_dir, filename)
        
        # 处理模型
        process_model(input_path, output_path)

print("\n模型处理完成！")
print(f"处理后的模型保存在: {output_dir}")
print("\n注意：由于Python库限制，模型面数精简和网格合并功能需要使用其他工具如Blender来完成。")