#Parts of the following code have been taken from user850498 
#https://stackoverflow.com/questions/9623398/text-files-in-a-dir-and-store-the-file-names-in-a-list-python
from bottle import route,run
import json
import socket
import getpass

#array to store photos in
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
    for item in os.listdir(path):
        full_path = os.path.join(path,item)
        if os.path.isfile(full_path):
            editFiles_photos.append(full_path)
    return editFiles_photos



#Reply Functions
@route('/photos')
def photos_request_all():
    return {"photo_name" : get_photos_files()}



#Run the server
run(reloader=True,host=get_my_ip(), port=12345)
