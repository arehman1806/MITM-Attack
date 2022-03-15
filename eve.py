import sys
import os
import time
from common import *
from const import *

BREAK_HEART = '--break-heart'
CUSTOM = '--custom'
RELAY = '--relay'

dialog = Dialog('print')

if len(sys.argv) != 2:
    print('Incorrect Number of command line arguments. Exiting the program')
    exit(-1)
flag = sys.argv[1]
print(flag)

os.rename('/tmp/s1829279/buffer', '/tmp/s1829279/buffer1')

player_b = 'bob'
print(player_b)
socket_b, aes_b = setup(player_b, BUFFER_DIR, BUFFER_FILE_NAME + str(1))

player_a = 'alice'
socket_a, aes_a = setup(player_a, BUFFER_DIR, BUFFER_FILE_NAME)

if flag == RELAY:
    received_from_bob = receive_and_decrypt(aes_a, socket_a)
    encrypt_and_send(received_from_bob, aes_b, socket_b)
    received_from_alice = receive_and_decrypt(aes_b, socket_b)
    encrypt_and_send(received_from_alice, aes_a, socket_a)

elif flag == BREAK_HEART:
    received_from_bob = receive_and_decrypt(aes_a, socket_a)
    break_heart_msg = BAD_MSG[player_b]
    encrypt_and_send(break_heart_msg, aes_b, socket_b)
    received_from_alice = receive_and_decrypt(aes_b, socket_b)
    encrypt_and_send(received_from_alice, aes_a, socket_a)

elif flag == CUSTOM:
    received_from_bob = receive_and_decrypt(aes_a, socket_a)
    dialog.prompt('Enter your custom message')
    user_input = input()
    encrypt_and_send(user_input, aes_b, socket_b)
    received_from_alice = receive_and_decrypt(aes_b, socket_b)
    dialog.prompt('Enter your custom message')
    user_input = input()
    encrypt_and_send(user_input, aes_a, socket_a)

else:
    print('Invalid flag. Exiting now')
    exit(-1)








