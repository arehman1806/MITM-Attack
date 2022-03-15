import sys
import os
import time
from common import *
from const import *

dialog = Dialog('print')
while(True):
    f = open(BUFFER_DIR+BUFFER_FILE_NAME, "r")
    print(f.read())
    f.close()
    time.sleep(0.1)
# player = os.path.basename(sys.argv[0]).split('.', 1)[0]
# print(player)
# socket, aes = setup(player, BUFFER_DIR, BUFFER_FILE_NAME)
# os.rename()