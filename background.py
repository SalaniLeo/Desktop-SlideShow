import os
import time
import os.path
from pathlib import Path
import json
 
home = str(Path.home())
imgN = 0
path = home + "/Pictures/wallpapers/mix/"
darkmode = "picture-uri-dark "
savefilePath = home + "/.cache/background"
savefileName = "/background.json"
savefileLoc = savefilePath + savefileName
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

#reads json file
if(os.path.isfile(savefileLoc)):
    with open(savefileLoc, 'r') as jsonfile:
        data = jsonfile.read()

    jsoncontent = json.loads(data)

    imgN = jsoncontent['img']

#sets the wallpaper
def setWallpaper():
    global imgN

    ##checks if imgnumber is more than the wallpapers and if so resets to the first
    if (imgN == num_files):
        imgN = 1
    else:
        imgN += 1

    filename = "img" + str(imgN) + ".*"
    command = "gsettings set org.gnome.desktop.background " + darkmode + path + filename

    ##executes the command to set wallpaper
    os.system(command)

    ##writes wallpaper number to json file
    json_data = '{"img": ' + str(imgN) + '}'
    jsonFIle = json.dumps(json_data)
    with open(savefileLoc, "w") as file:
        file.write(str(json_data))

#Creates json folder if not existing
if not os.path.isdir(savefilePath):
    os.mkdir(savefilePath)

#every tot minutes changes background
while True:
    setWallpaper()
    time.sleep(2)
