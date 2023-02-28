# ICMP_Flooding_Demo

These are two demos that simply implement icmp flooding

### Test1.py

This file uses `scapy`, a python library, to implement sending requests.

`inputIPCheck()` implements the function to check the input ip. `fakeSourceIPgenerates()` implements the function to forge the source ip.

#### Usage

```sh
pip install scapy
sudo python test1.py
```

After that, enter the target ip in the LAN.

### Test2.py

It uses hping to implement the icmp flooding attack. Send icmp packet with random source ip address and packet size 1400b to target ip to implement dos attack.

```sh
hping --icmp --rand-source --flood -d 1400 192.168.1.1
```

The script introduces the `ThreadPoolExecutor` to open a pool of threads of size 20 to execute the task of flooding attack.

#### Usage

```sh
sudo python test2.py
```



### Attention

This is for experimentation only, please try it with your own personal device. Do not launch malicious attacks on others.
