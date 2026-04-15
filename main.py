import random

def predict():
    return random.choice(["UP", "DOWN"])

if __name__ == "__main__":
    for i in range(10):
        print(f"Prediction {i+1}: {predict()}")
