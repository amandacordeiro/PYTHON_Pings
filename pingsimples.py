
import os

print('#' * 60)

ip_host = input('Digite o Ip ou Host a ser verificado: ')

os.system('ping -n 6 {}'.format(ip_host))
