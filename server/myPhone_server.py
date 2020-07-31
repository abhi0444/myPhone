#Parts of the following code have been taken from user850498 
#https://stackoverflow.com/questions/9623398/text-files-in-a-dir-and-store-the-file-names-in-a-list-python
from bottle import route,run, template, static_file
import json
import socket
import getpass
import os

main_dir = "/home/"+str(getpass.getuser())+"/"
photos_dir = main_dir+"Pictures"

photos_tpl = """
% for file in files:
   	<img src="{{file}}" alt="Snow" width=10% height=10% >
% end
"""

def list_photos():
    photos_list = []
    for item in os.listdir(photos_dir):
        full_path = os.path.join(photos_dir,item)
        if os.path.isfile(full_path):
            photos_list.append(full_path)
    return photos_list

@route("/photos")
def photos():
    return template(photos_tpl, files=list_photos())

@route(photos_dir+"/<filename>")
def wallpapers(filename):
    return static_file(filename, root = photos_dir)

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

#Run the server
run(reloader=True,host=get_my_ip(), port=12345)
