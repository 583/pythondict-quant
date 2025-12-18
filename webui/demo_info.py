#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成Web UI预览截图的演示脚本
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到路径
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / 'webui'))

from app import app, STRATEGIES

def generate_demo_info():
    """生成演示信息"""
    print("=" * 80)
    print("量化投资策略Web UI - 演示信息")
    print("=" * 80)
    print()
    
    print(f"📊 已配置策略总数: {len(STRATEGIES)}")
    print()
    
    print("策略列表按类别分组:")
    print("-" * 80)
    
    # 按类别分组
    categories = {}
    for key, strategy in STRATEGIES.items():
        category = strategy.get('category', '其他')
        if category not in categories:
            categories[category] = []
        categories[category].append({
            'id': key,
            **strategy
        })
    
    for category, strategies in categories.items():
        print(f"\n【{category}】({len(strategies)}个策略)")
        for strategy in strategies:
            plot_info = "✓ 支持图表" if strategy.get('has_plot') else "✗ 无图表"
            images_info = f" | {len(strategy.get('images', []))}张预览图" if 'images' in strategy else ""
            print(f"  • {strategy['name']}")
            print(f"    {strategy['description']}")
            print(f"    脚本: {strategy['script']} | {plot_info}{images_info}")
    
    print()
    print("=" * 80)
    print("Web UI功能特点:")
    print("=" * 80)
    print("""
✅ 策略浏览 - 卡片式布局展示所有策略
✅ 分类管理 - 按功能类别自动分组
✅ 详情查看 - 点击查看每个策略的详细信息
✅ 图表预览 - 对于强化学习等策略，可直接查看预览图
✅ 一键运行 - 直接在Web界面执行策略并查看结果
✅ 响应式设计 - 支持桌面和移动设备
✅ 美观界面 - 渐变色主题，现代化UI设计
    """)
    
    print("=" * 80)
    print("启动方式:")
    print("=" * 80)
    print("""
方式1: 使用启动脚本
    cd webui
    ./start.sh

方式2: 直接运行Python
    cd webui
    pip install -r requirements.txt
    python app.py

方式3: 使用Flask CLI
    cd webui
    export FLASK_APP=app.py
    flask run
    """)
    
    print("=" * 80)
    print("访问地址: http://localhost:5000")
    print("=" * 80)

if __name__ == '__main__':
    generate_demo_info()
