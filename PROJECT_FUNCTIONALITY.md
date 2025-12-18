# Project Functionality Documentation

## 📊 Project Overview

This is a **Quantitative Investment Practical Tutorial** project developed and maintained by Python实用宝典 (pythondict.com). The core objective is to teach how to develop, backtest, and verify quantitative investment strategies using Python, helping investors validate various technical analysis strategies through data and code rather than blindly trusting market investment advice.

## 🎯 Main Features

### 1. **Quantitative Trading Strategy Backtesting**
The project provides multiple classic quantitative trading strategy implementations and backtesting frameworks, including:

- **MACD Strategy**: Trading strategy based on Moving Average Convergence Divergence indicator
- **KDJ Strategy**: Trading strategy based on Stochastic indicator
- **MACD + KDJ Combined Strategy**: Multi-indicator combination strategy
- **Moving Average Strategy**: Trading strategy based on golden cross and death cross
- **Harami Strategy**: Trading strategy based on candlestick patterns

### 2. **A-Share Market Batch Backtesting**
Supports batch backtesting of multiple stocks in the A-share market to verify strategy performance in real market environments, including:

- Batch download and processing of A-share historical data
- Batch execution of backtesting strategies
- Statistical analysis of backtesting results
- Calculation of key metrics such as average returns

### 3. **Custom Data Source Support**
Provides custom data source implementation examples, supporting:

- Reading stock data from MySQL database
- Custom data formats and data streams
- Flexible data interface extensions

### 4. **Real-time Monitoring System**
Stock real-time monitoring system based on Prometheus + Grafana:

- Real-time scraping of Eastmoney popularity ranking data
- Data collection using Prometheus
- Visualization through Grafana dashboard

### 5. **Factor Backtesting Analysis**
Single-factor backtesting analysis using Alphalens:

- Quantitative factor effectiveness validation
- Factor return analysis
- Factor Information Coefficient (IC) calculation

### 6. **Reinforcement Learning Quantitative Trading**
Automatic trading system based on deep reinforcement learning:

- Building stock trading environment using OpenAI Gym
- Implementing PPO (Proximal Policy Optimization) algorithm
- Automatically learning buy, sell, and hold strategies
- Optimizing trading decisions through reinforcement learning

### 7. **Convertible Bond Arbitrage Strategy**
Convertible bond investment strategy and arbitrage opportunity analysis

## 🛠 Technology Stack

- **Core Framework**: Backtrader - Python quantitative backtesting framework
- **Data Processing**: Pandas, NumPy
- **Data Visualization**: Matplotlib
- **Data Sources**:
  - baostock - Free open-source securities data platform
  - MySQL database
  - Eastmoney API
- **Monitoring System**: Prometheus + Grafana
- **Factor Analysis**: Alphalens
- **Reinforcement Learning**:
  - OpenAI Gym - Reinforcement learning environment
  - Stable Baselines - Reinforcement learning algorithm library
  - TensorFlow/PyTorch

## 📚 Tutorial Directory Structure

The project contains 15 series of tutorial articles, of which 13 tutorials have corresponding code directories. Each directory corresponds to a specific quantitative investment topic:

| Directory | Topic | Functionality |
|-----------|-------|---------------|
| 01.begin | Beginner Tutorial | Backtrader basics, moving average strategy |
| 02.easy_macd_strategy | MACD Strategy | MACD indicator strategy implementation and backtesting |
| 03.macd_in_A_market | A-Share MACD Backtesting | MACD strategy batch backtesting in A-share market |
| 04.kdj_with_macd | KDJ Strategy | KDJ indicator and MACD combination strategy |
| 05.kdj_macd_in_A_market | A-Share KDJ+MACD Backtesting | Combined strategy batch backtesting in A-share market |
| 06.average_profit | Trading Average Profit | Calculate and analyze average trading returns |
| 07.harami | Harami Strategy | Candlestick pattern-based harami strategy |
| 08.harami_in_A_market | A-Share Harami Backtesting | Harami strategy batch backtesting in A-share market |
| 09.custom_data_source | Custom Data Source | MySQL data source custom implementation |
| 10.converted_bond | Convertible Bond Strategy | Convertible bond investment strategy analysis |
| 11.eastmoney_with_prom_grafana | Real-time Monitoring | Prometheus+Grafana real-time monitoring system |
| 13.alphalens_factor_backtest | Factor Backtesting | Alphalens single-factor backtesting analysis |
| 15.rl_learning | Reinforcement Learning | Deep reinforcement learning automatic trading system |

**Note**: Tutorial 12 (Lean quantitative trading platform) and Tutorial 14 (Qlib quantitative investment platform) are introductions to external platforms and do not have corresponding code directories in this repository.

## 💡 Core Value

### 1. **Data-Driven Investment Decisions**
The project emphasizes validating investment strategies with data and backtesting results rather than relying on subjective judgment or one-sided market propaganda.

### 2. **Complete Practical Tutorials**
Each module includes:
- Detailed code implementation
- Real stock data
- Runnable backtesting examples
- Supporting tutorial articles

### 3. **Progressive Learning Path**
Starting from basic moving average strategies, gradually advancing to:
- Technical indicator strategies (MACD, KDJ)
- Candlestick pattern strategies (Harami)
- Factor analysis
- Reinforcement learning

### 4. **Real Market Validation**
Not only provides theoretical strategies but also includes:
- Real data backtesting in A-share market
- Statistical analysis of batch stocks
- Quantitative assessment of strategy effectiveness

## 🔍 Use Cases

1. **Quantitative Investment Learning**: Suitable for beginners to systematically learn basic knowledge and practical skills of quantitative investment
2. **Strategy Validation**: Verify the effectiveness of technical analysis indicators and trading strategies
3. **Strategy Development**: Develop and test new trading strategies based on existing code
4. **Research Analysis**: Conduct quantitative investment-related academic research and data analysis
5. **System Monitoring**: Build real-time monitoring and alert systems for stock markets

## 📖 Typical Usage Examples

### Example 1: Run MACD Strategy Backtesting

```python
# Enter MACD strategy directory
cd 02.easy_macd_strategy

# Run backtesting
python macd.py
```

### Example 2: Batch Backtest A-Share Strategies

```python
# Enter A-share batch backtesting directory
cd 03.macd_in_A_market

# Run batch backtesting
python batch_macd.py
```

### Example 3: Start Real-time Monitoring System

```python
# Enter monitoring system directory
cd 11.eastmoney_with_prom_grafana

# Start data collection service
python fetch_stock.py
```

### Example 4: Run Reinforcement Learning Training

```python
# Enter reinforcement learning directory
cd 15.rl_learning

# Get stock data
python get_stock_data.py

# Start training
python main.py
```

## ⚠️ Important Notes

1. **For Learning Only**: All strategies and code in this project are for educational and research purposes only
2. **Not Investment Advice**: Historical backtesting results do not represent future performance; actual investment requires caution
3. **Data Sources**: Stock data used comes from public sources (such as baostock) and may have delays or deviations
4. **Risk Warning**: Stock market involves risks, invest cautiously. Any investment decision should be based on your own independent judgment

## 🔗 Related Resources

- **Project Homepage**: Python实用宝典 (Python Practical Dictionary) - https://pythondict.com
- **Tutorial List**: See complete tutorial links in README.md
- **Core Framework**: Backtrader - https://github.com/mementum/backtrader
- **Data Platform**: baostock - http://baostock.com

## 📝 Summary

This is a comprehensive quantitative investment tutorial project covering everything from basic technical indicator strategies to advanced deep reinforcement learning algorithms. Through 15 series of tutorial articles (including 13 code implementation modules), it helps learners:

- Master basic principles and methods of quantitative investment
- Learn to develop and backtest strategies using Python
- Understand how to validate the effectiveness of trading strategies
- Build complete quantitative trading systems

The greatest value of this project lies in emphasizing **letting data speak**, objectively evaluating strategy effectiveness through backtesting and statistical analysis, avoiding being misled by one-sided market propaganda.
