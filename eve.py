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

player_b = 'bob'
print(player_b)
socket_b, aes_b = setup(player_b, BUFFER_DIR, BUFFER_FILE_NAME + str(1))



player_a = 'alice'
socket_a, aes_a = setup(player_a, BUFFER_DIR, BUFFER_FILE_NAME)

received = receive_and_decrypt(aes_a, socket_a)
print('bob said: ' + received)

heart_break = 'I hate you!'
encrypt_and_send(heart_break, aes_b, socket_b)

received_from_alice = receive_and_decrypt(aes_b, socket_b)

encrypt_and_send(received_from_alice, aes_a, socket_a)


