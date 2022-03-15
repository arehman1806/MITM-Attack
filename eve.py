import sys
import os
import time
from common import *
from const import *

dialog = Dialog('print')
# while(True):
#     f = open(BUFFER_DIR+BUFFER_FILE_NAME, "r")
#     print(f.read())
#     f.close()
#     time.sleep(0.1)
os.rename('/tmp/s1829279/buffer', '/tmp/s1829279/buffer1')
player = 'alice'
print(player)
socket, aes = setup(player, BUFFER_DIR, BUFFER_FILE_NAME)
received = receive_and_decrypt(aes, socket)
print('bob said: ' + received)
received = receive_and_decrypt(aes, socket)
print('bob said: ' + received)

