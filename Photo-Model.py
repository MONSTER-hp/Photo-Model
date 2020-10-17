# __  __  ___  _   _ ____ _____ _____ ____      _   _    _    ____ _  __ 
#|  \/  |/ _ \| \ | / ___|_   _| ____|  _ \    | | | |  / \  / ___| |/ / 
#| |\/| | | | |  \| \___ \ | | |  _| | |_) |   | |_| | / _ \| |   | ' /  
#| |  | | |_| | |\  |___) || | | |___|  _ <    |  _  |/ ___ \ |___| . \  
#|_|  |_|\___/|_| \_|____/ |_| |_____|_| \_\___|_| |_/_/   \_\____|_|\_\ 
#                                         |_____|                        
#      >>> GitHub : https://github.com/MONSTER-hp/MONSTER_HACK <<<
#        >>> Telegram Chanell : https://t.me/MONSTER_SECURIT <<<
#          >>> Web Sayte : www.Monster-Security.blogfa.com <<<
#                         </> MONSTER_hp </>

from os import popen
from exif import Image
print (" ____  _           _              __  __           _      _")
print ("|  _ \| |__   ___ | |_ ___       |  \/  | ___   __| | ___| |")
print ("| |_) | '_ \ / _ \| __/ _ \ _____| |\/| |/ _ \ / _` |/ _ \ |")
print ("|  __/| | | | (_) | || (_) |_____| |  | | (_) | (_| |  __/ |")
print ("|_|   |_| |_|\___/ \__\___/      |_|  |_|\___/ \__,_|\___|_|")
print('')
print(" >>> GitHub : https://github.com/MONSTER-hp/MONSTER_HACK <<<")
print('')
print("   >>> Telegram Chanell : https://T.me/MONSTER_SECURIT <<<")
print('')
print("     >>> Web Sayte : www.Monster-Security.blogfa.com <<<")
print ('')
print('')
pic = input ("Photo Address : ")
img = Image(open(pic,"rb"))
try:
    model = img.model
except:
    exit()
print("Model : {}".format(model))
command = "google https://www.google.com/search?q=\"{}\"".format(model)
popen(command)

#HACKER BY MONSTER_HP