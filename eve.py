import sys
import os
import time
from common import *
from const import *


dialog = Dialog('print')

flag = sys.argv[0]
print(flag)

os.rename('/tmp/s1829279/buffer', '/tmp/s1829279/buffer1')

player_b = 'bob'
print(player_b)
socket_b, aes_b = setup(player_b, BUFFER_DIR, BUFFER_FILE_NAME + str(1))



player_a = 'alice'
socket_a, aes_a = setup(player_a, BUFFER_DIR, BUFFER_FILE_NAME)

received = receive_and_decrypt(aes_a, socket_a)
heart_break = 'I hate you!'
print('bob said: {}. But i will say: {}. HEHEHEHEHE'.format(received, heart_break))
encrypt_and_send(heart_break, aes_b, socket_b)

received_from_alice = receive_and_decrypt(aes_b, socket_b)

encrypt_and_send(received_from_alice, aes_a, socket_a)


