import os
import time
import os.path
from pathlib import Path
import json
import argparse

home = str(Path.home())

parser = argparse.ArgumentParser(description='Thanks for using wllp :D, help:')
parser.add_argument('--path', help='Select which path to use')
parser.add_argument('--darkmode', help='Choose true, false or both based on your system theme')
args = parser.parse_args()

class SaveConf():
    @staticmethod
    def save_directory(img_path, json_save_loc):
        data = load_config(json_save_loc)
        data["img_path"] = img_path
        SaveConf._save_json(data, json_save_loc)

    @staticmethod
    def save_darkmode(mode, json_save_loc):
        data = load_config(json_save_loc)
        data["dark_mode"] = mode
        SaveConf._save_json(data, json_save_loc)

    @staticmethod
    def save_current_image(image_number, json_save_loc):
        data = load_config(json_save_loc)
        data["image_number"] = image_number
        SaveConf._save_json(data, json_save_loc)

    @staticmethod
    def _save_json(data, json_save_loc):
        with open(json_save_loc, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    def _first_load(image_number, img_path, mode, json_save_loc):
        open(json_save_loc, "w")
        data = {"image_number": image_number, "img_path": img_path, "dark_mode": mode}
        SaveConf._save_json(data, json_save_loc)
        print(data, json_save_loc)

def load_config(json_save_loc):
    if(os.path.isfile(json_save_loc)):
        with open(json_save_loc, 'r') as jsonfile:
            data = jsonfile.read()
            return json.loads(data)


def set_wallpaper(image_number, img_path, images, mode):

    filename = f'{images[image_number]}'
    command = f'gsettings set org.gnome.desktop.background {mode}"{img_path}/{filename}"'

    os.system(command)

def main():

    json_save_path = home + "/.cache/wllp"
    json_save_name = "/wllp.json"

    json_save_loc = json_save_path + json_save_name

    if not os.path.isdir(json_save_path):
        os.mkdir(json_save_path)
        SaveConf._first_load(0, f'{home}/Pictures', False, json_save_loc)

    if args.path != None:
        if os.path.isdir(args.path):
            if len(os.listdir(args.path)) == 0:
                print(f'The path {args.path} does not contain any image')
                return
            SaveConf.save_directory(args.path, json_save_loc)
        else:
            print(f'{args.path} is not a valid path.')

    if args.darkmode != None: SaveConf.save_darkmode(args.darkmode, json_save_loc)

    app_data     = load_config(json_save_loc)
    image_number = app_data['image_number']
    img_path     = app_data['img_path']
    images       = os.listdir(img_path)
    darkmode     = app_data['dark_mode']

    if darkmode:
        mode = "picture-uri-dark "
    else: 
        mode = "picture-uri "

    while True:
        if image_number >= len(images): image_number = 0
        set_wallpaper(image_number, img_path, images, mode)
        SaveConf.save_current_image(image_number, json_save_loc)

        time.sleep(1)

        image_number += 1

if __name__ == "__main__":
    main()