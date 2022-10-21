import os
import sys
import time
import os.path
from pathlib import Path
import json
import argparse
 
home = str(Path.home())
imgN = 0
darkmode = "picture-uri-dark "
savefilePath = home + "/.cache/background"
savefileName = "/background.json"
savefileLoc = savefilePath + savefileName
imgPath = None
num_files = None

##ARGPARSE
parser = argparse.ArgumentParser(description='App to modify ')
parser.add_argument('--path', help='sets the wallpapers path')
args = parser.parse_args()

imgPath = args.path

#writes data inside json file
def writeData():
    #specify the data to write to file
    data = {"img": imgN, "imgPath": imgPath}
    #writes the data to file
    with open(savefileLoc, 'w') as outfile:
        json.dump(data, outfile,indent=4)

#checks if Json file exists
if(os.path.isfile(savefileLoc)):
    with open(savefileLoc, 'r') as jsonfile:
        data = jsonfile.read()

        jsoncontent = json.loads(data)
        #reads specified content
        imgN = jsoncontent['img']
        if(args.path != None):
            None
        else:
            imgPath = jsoncontent['imgPath']
else:
    #sets imgPath to default if json file doesn't exists
    imgPath = home + "/Pictures"

#sets the wallpaper
def setWallpaper():
    num_files = len([f for f in os.listdir(imgPath) if os.path.isfile(os.path.join(imgPath, f))])
    # print(num_files)
    global imgN

    ##checks if imgnumber is more than the wallpapers and if so resets to the first
    if (imgN >= num_files):
        imgN = 1
    else:
        imgN += 1

    filename = "img" + str(imgN) + ".*"
    command = "gsettings set org.gnome.desktop.background " + darkmode + imgPath + filename

    ##executes the command to set wallpaper
    os.system(command)
    writeData()

#Creates json folder if not existingfsdfsdffds
if not os.path.isdir(savefilePath):
    os.mkdir(savefilePath)


if(args.path != None):
    if os.path.isdir(args.path):
        writeData()
    else:
        print(args.path + " is not a valid path")
else:
    while True:
        setWallpaper()
        time.sleep(1200)