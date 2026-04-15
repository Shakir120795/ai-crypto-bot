# 🚀 AI Crypto Prediction Bot

An AI-powered trading assistant that predicts next candle direction using RSI and probability logic.

## 🔥 Features
- RSI-based prediction system
- Basic accuracy tracking
- Expandable architecture
- Beginner-friendly

## 🧠 Tech Stack
- Python
- Pandas, NumPy

## ⚙️ How it Works
- Calculates RSI from price data
- Uses thresholds:
  - RSI < 30 → UP (oversold)
  - RSI > 70 → DOWN (overbought)
- Tracks prediction accuracy

## ⚙️ Run
pip install -r requirements.txt  
python main.py

## 📊 Output Example
Prediction 1: UP | Actual: DOWN  
Prediction 2: DOWN | Actual: DOWN  

Accuracy: 55%

## 📌 Future Plans
- Integrate Binance API (real data)
- Add VWAP & divergence
- Telegram alerts
- Polymarket integration

## 🤝 Open Source
Open for contributions and improvements.
