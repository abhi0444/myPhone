#Parts of the following code have been taken from user850498 
#https://stackoverflow.com/questions/9623398/text-files-in-a-dir-and-store-the-file-names-in-a-list-python
from bottle import route,run
import json
import socket
import getpass
editFiles_photos = []
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
    for item in dirListing:
        if ".png" in item:
            editFiles_photos.append(item)
        elif ".jpg" in item:
            editFiles_photos.append(item)
        elif ".jpeg" in item:
            editFiles_photos.append(item)
    return editFiles_photos
#Reply Functions
@route('/photos')
def photos_request_all():
    return {"photo_name" : get_photos_files()}
#Run the server
run(reloader=True,host=get_my_ip(), port=12345)
