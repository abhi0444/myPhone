#Parts of the following code have been taken from user850498 
#https://stackoverflow.com/questions/9623398/text-files-in-a-dir-and-store-the-file-names-in-a-list-python
from bottle import route,run
import json
import socket
import getpass
import cv2
def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(1)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
def get_photos_files():
    import os
    path = "/home/"+str(getpass.getuser())+"/Pictures"
    dirListing = os.listdir(path)
    image_data = []
    for img in dirListing:
        img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_COLOR) #reads images present in folder
        image_data.append(img_array)    #insert the each array of image in imade_data list
    return image_data
#Reply Functions
@route('/photos')
def photos_request():
    return {"myFiles" : get_photos_files()}
#Run the server
run(host=get_my_ip(), port=12345)
