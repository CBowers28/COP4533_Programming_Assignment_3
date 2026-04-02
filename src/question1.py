import random
import string
import time
from main import opt, main
import seaborn
from matplotlib import pyplot as plt

def gen_example(length=25):
    str1 = ''.join(random.choices(string.ascii_lowercase, k=length))
    str2 = ''.join(random.choices(string.ascii_lowercase, k=length))
    values = {}
    for char in string.ascii_lowercase:
        values[char] = random.randint(0, 6)
    return (values, str1, str2)

if __name__ == '__main__':
    random.seed(100)
    sizes = [25 * i**2 for i in range(1, 15)]
    examps = [gen_example(size) for size in sizes]
    runtimes = []

    fig, ax = plt.subplots()

    for (i, examp) in enumerate(examps):
        start_time = time.time()
        main(examp)
        runtime = time.time() - start_time
        runtimes.append(runtime)
        print(sizes[i], runtime)

    plot = seaborn.lineplot(x=sizes, y=runtimes)
    ax.set_xlabel("n")
    ax.set_ylabel("Runtime (s)")
    ax.set_title("Runtime for various input string sizes")
    fig.savefig("img/graph.png")