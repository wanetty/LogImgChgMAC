#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import ntpath
import shutil
path_img=""
orgiName =""
bckName =""

def doBackup(response):
	if response == "s":
		print("Doing backup ")
		print ("sudo cp  + path_img + orgiName + "  + path_img + bckName )
		os.system(" sudo mv " + path_img + orgiName + " " + path_img + bckName )
		print("Finish backup")
	elif response == "n":
		print("No backup")
	else:
		print ("Aborting")
		exit()
def mvImg(path):
	if path == "" and not os.path.exists(path):
		print ("Aborting")
		exit()
	else:
		print(" sudo cp " + path +  " " + path_img + orgiName )
		os.system(" sudo cp " + path + " " + path_img + orgiName )
		print("Image moved")


if __name__ == "__main__":
	print(chr(27) + "[2J")
	print( " _                _____                _____  _            ___  ___  ___  _____ ")
	print( "| |              |_   _|              /  __  | |           |  \/  | / _ \/  __ \ ")
	print( "| |     ___   __ _ | | _ __ ___   __ _| /  \ | |__   __ _  | .  . |/ /_\ \ /  \/")
	print( "| |    / _ \ / _\` | || |  '_  \`/ _  | |    | '_ \ / _\`  | | |\/| | | |   ")
	print( "| |___| (_) | (_| || || | | | | | (_| | \__/\ | | | (_| |  | |  | || | | | \__/\ ")
	print( "\_____/\___/ \__, \___/_| |_| |_|\__, |\____/_| |_|\__, |  \_|  |_/\_| |_/\____/")
	print( "              __/ |               __/ |             __/ |                      ")
	print( "             |___/               |___/             |___/                       ")
	path_img = "/Library/Desktop\\ Pictures/"
	orgiName= "Mojave_tst.heic"
	bckName = "Mojave_test_old.heic"
	path_new_image= raw_input("Location of new image: ")
	path_new_image = path_new_image.strip()
	backup = raw_input("Do you like a backup of old image? [s/n]")
	doBackup(backup)
	mvImg(path_new_image)
	print("Once you have copied the image, you should follow these steps:\n" +
		"1-> go to System preferences -> Users and groups -> Startup options\n" +
		"2-> Change any parameter and remember the change\n" +
		"3-> Reset\n" +
		"4-> Finally, leave the parameter as it was.\n")
	
	
