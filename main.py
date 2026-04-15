import pandas as pd
import numpy as np
import random

# Dummy price data (replace later with real API)
data = pd.DataFrame({
    "close": np.random.randint(30000, 40000, 100)
})

# RSI function
def calculate_rsi(data, period=14):
    delta = data["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Prediction logic
def predict(data):
    rsi = calculate_rsi(data).iloc[-1]

    if rsi < 30:
        return "UP"
    elif rsi > 70:
        return "DOWN"
    else:
        return random.choice(["UP", "DOWN"])

# Accuracy tracker
def run_bot():
    correct = 0
    total = 20

    for i in range(total):
        pred = predict(data)
        actual = random.choice(["UP", "DOWN"])  # dummy result

        if pred == actual:
            correct += 1

        print(f"Prediction {i+1}: {pred} | Actual: {actual}")

    print(f"\nAccuracy: {round((correct/total)*100, 2)}%")

if __name__ == "__main__":
    run_bot()
