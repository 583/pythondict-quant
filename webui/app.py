# -*- coding: utf-8 -*-
"""
量化投资策略Web UI
提供可视化界面来查看和运行各种量化投资策略
"""

import os
import sys
import json
import datetime
import subprocess
from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
import io
import base64

# 添加项目根目录到路径
BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pythondict-quant-webui-2025'

# 策略配置
STRATEGIES = {
    '01.begin': {
        'name': '入门教程 - 移动平均线策略',
        'description': 'Backtrader基础使用，基于5日和10日移动平均线的金叉死叉策略',
        'script': '01.begin/cash.py',
        'has_plot': False,
        'stock_file': '01.begin/600519.csv',
        'category': '基础入门'
    },
    '02.easy_macd_strategy': {
        'name': 'MACD策略',
        'description': '基于MACD指标的交易策略，当MACD线上穿信号线时买入，涨跌幅达到10%时卖出',
        'script': '02.easy_macd_strategy/macd.py',
        'has_plot': True,
        'stock_file': '02.easy_macd_strategy/603186.csv',
        'category': '技术指标'
    },
    '03.macd_in_A_market': {
        'name': 'A股MACD批量回测',
        'description': 'MACD策略在A股市场的批量回测，验证策略在真实市场环境中的表现',
        'script': '03.macd_in_A_market/batch_macd.py',
        'has_plot': False,
        'category': 'A股回测'
    },
    '04.kdj_with_macd': {
        'name': 'KDJ策略',
        'description': '基于KDJ随机指标的交易策略，买入基于MACD，卖出基于KDJ',
        'script': '04.kdj_with_macd/kdj_macd.py',
        'has_plot': True,
        'stock_file': '04.kdj_with_macd/002859.csv',
        'category': '技术指标'
    },
    '05.kdj_macd_in_A_market': {
        'name': 'A股KDJ+MACD批量回测',
        'description': 'KDJ和MACD组合策略在A股市场的批量回测',
        'script': '05.kdj_macd_in_A_market/batch_kdj_macd.py',
        'has_plot': False,
        'category': 'A股回测'
    },
    '06.average_profit': {
        'name': '交易平均收益分析',
        'description': '计算和分析交易的平均收益率，评估策略性能',
        'script': '06.average_profit/macd.py',
        'has_plot': True,
        'stock_file': '06.average_profit/603186.csv',
        'category': '策略分析'
    },
    '07.harami': {
        'name': '孕线策略',
        'description': '基于K线形态的孕线策略，识别孕线形态进行交易',
        'script': '07.harami/harami.py',
        'has_plot': True,
        'stock_file': '07.harami/603186.SH.csv',
        'category': 'K线形态'
    },
    '08.harami_in_A_market': {
        'name': 'A股孕线批量回测',
        'description': '孕线策略在A股市场的批量回测验证',
        'script': '08.harami_in_A_market/batch_harami.py',
        'has_plot': False,
        'category': 'A股回测'
    },
    '09.custom_data_source': {
        'name': '自定义MySQL数据源',
        'description': '展示如何从MySQL数据库读取股票数据进行回测',
        'script': '09.custom_data_source/macd.py',
        'has_plot': True,
        'category': '数据源'
    },
    '11.eastmoney_with_prom_grafana': {
        'name': '实时监控系统',
        'description': '基于Prometheus + Grafana的东方财富人气榜实时监控',
        'script': '11.eastmoney_with_prom_grafana/fetch_stock.py',
        'has_plot': False,
        'category': '监控系统'
    },
    '13.alphalens_factor_backtest': {
        'name': 'Alphalens因子回测',
        'description': '使用Alphalens进行单因子回测分析',
        'script': '13.alphalens_factor_backtest/test.py',
        'has_plot': False,
        'category': '因子分析'
    },
    '15.rl_learning': {
        'name': '强化学习自动交易',
        'description': '基于深度强化学习(PPO算法)的自动交易系统',
        'script': '15.rl_learning/main.py',
        'has_plot': False,
        'category': '强化学习',
        'images': [
            '15.rl_learning/img/profits.png',
            '15.rl_learning/img/profits_hist.png'
        ]
    }
}


@app.route('/')
def index():
    """主页 - 显示所有策略"""
    # 按类别分组策略
    categories = {}
    for key, strategy in STRATEGIES.items():
        category = strategy.get('category', '其他')
        if category not in categories:
            categories[category] = []
        categories[category].append({
            'id': key,
            **strategy
        })
    
    return render_template('index.html', categories=categories)


@app.route('/strategy/<strategy_id>')
def strategy_detail(strategy_id):
    """策略详情页"""
    if strategy_id not in STRATEGIES:
        return "策略不存在", 404
    
    strategy = STRATEGIES[strategy_id]
    strategy['id'] = strategy_id
    
    # 检查是否有预览图片
    preview_images = []
    if 'images' in strategy:
        for img_path in strategy['images']:
            full_path = BASE_DIR / img_path
            if full_path.exists():
                preview_images.append(f'/preview_image/{strategy_id}/{os.path.basename(img_path)}')
    
    return render_template('strategy_detail.html', 
                         strategy=strategy, 
                         preview_images=preview_images)


@app.route('/preview_image/<strategy_id>/<image_name>')
def preview_image(strategy_id, image_name):
    """获取策略预览图片"""
    if strategy_id not in STRATEGIES:
        return "策略不存在", 404
    
    strategy = STRATEGIES[strategy_id]
    if 'images' in strategy:
        for img_path in strategy['images']:
            if os.path.basename(img_path) == image_name:
                full_path = BASE_DIR / img_path
                if full_path.exists():
                    return send_file(full_path, mimetype='image/png')
    
    return "图片不存在", 404


@app.route('/api/run_strategy', methods=['POST'])
def run_strategy():
    """运行策略"""
    data = request.json
    strategy_id = data.get('strategy_id')
    
    if strategy_id not in STRATEGIES:
        return jsonify({'error': '策略不存在'}), 404
    
    strategy = STRATEGIES[strategy_id]
    script_path = BASE_DIR / strategy['script']
    
    if not script_path.exists():
        return jsonify({'error': '策略脚本不存在'}), 404
    
    try:
        # 运行策略脚本
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=script_path.parent,
            capture_output=True,
            text=True,
            timeout=300  # 5分钟超时
        )
        
        return jsonify({
            'success': True,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': '策略运行超时'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/strategies')
def api_strategies():
    """获取所有策略列表API"""
    strategies_list = []
    for key, strategy in STRATEGIES.items():
        strategies_list.append({
            'id': key,
            'name': strategy['name'],
            'description': strategy['description'],
            'category': strategy.get('category', '其他'),
            'has_plot': strategy.get('has_plot', False)
        })
    
    return jsonify(strategies_list)


if __name__ == '__main__':
    # 创建必要的目录
    os.makedirs(BASE_DIR / 'webui' / 'templates', exist_ok=True)
    os.makedirs(BASE_DIR / 'webui' / 'static', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
