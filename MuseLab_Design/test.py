import numpy as np

for i in range(1000):
    R = np.random.choice([0, 1], replace= True, p=[0.3, 0.7])
    # R = random.randint(0, 1)
    print("Random Number:", R)