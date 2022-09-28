import os
import time
import os.path
from pathlib import Path

home = str(Path.home())
imgN = 0
path = home + "/Pictures/wallpapers/mix/"
darkmode = "picture-uri-dark "
savefilePath = home + "/.cache/background/"
savefileName = "background.num"
savefileLoc = savefilePath + savefileName

num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])


if(os.path.isfile(savefileLoc)):
    with open(savefileLoc) as f: imgN = int(f.read())

def setWallpaper():
    global imgN

    if (imgN == num_files):
        imgN = 1
    else:
        imgN += 1

    filename = "img" + str(imgN) + ".*"
    command = "gsettings set org.gnome.desktop.background " + darkmode + path + filename

    os.system(command)

    if not os.path.isdir(savefilePath):
        os.mkdir(savefilePath)

    with open(savefileLoc, "w") as file:
        file.write(str(imgN))

    print(imgN)

while True:
    setWallpaper()
    time.sleep(300)
