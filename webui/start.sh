#!/bin/bash
# 量化投资策略Web UI启动脚本

echo "========================================="
echo "   量化投资策略Web UI"
echo "   Python实用宝典"
echo "========================================="
echo ""

# 检查是否在正确的目录
if [ ! -f "app.py" ]; then
    echo "错误: 请在webui目录下运行此脚本"
    exit 1
fi

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3"
    exit 1
fi

# 检查依赖是否安装
echo "检查依赖..."
python3 -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "正在安装依赖..."
    pip install -r requirements.txt
fi

echo ""
echo "启动Web服务器..."
echo "访问地址: http://localhost:5000"
echo "按 Ctrl+C 停止服务器"
echo ""

# 启动Flask应用
python3 app.py
