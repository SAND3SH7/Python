import matplotlib.pyplot as plt
import numpy as np

try:
    op = input("Enter operation (log/sin/cos/tan): ")
    num = float(input("Enter value: "))

    if op == "log":
        if num > 0:  # yo exception handling log ko lagi!!
            print(np.log(num))
        else:
            print("Log is only defined for positive numbers")

    elif op == "sin":
        print(np.sin(num))

    elif op == "cos":
        print(np.cos(num))

    elif op == "tan":
        print(np.tan(num))

    else:
        print("Invalid operation")

except Exception as e:
    print("Error:", e)


import pandas as pd

info = {
    "Name": ["Sandesh", "Ram", "Sita"],  # yesma afno data rakhnu yesai gari
    "Age": [20, 22, 21],
    "Education": ["Bachelor", "Bachelor", "Master"]
}

list = pd.DataFrame(info)
# yo list ko index ko lagi matra ho nagarda pani farak pardaina
list.index = range(1, len(list) + 1)

print(list)


def f(x):
    return x**2


# first ko two parameter initial value range ra last parameter kati ota dot print garne
x = np.linspace(-10, 10, 100)
y = f(x)
plt.plot(x, y)
plt.title("Graph of y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
