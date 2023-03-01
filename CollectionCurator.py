import os
import glob
import numpy as np
import cv2
from PIL import Image
from mtcnn import MTCNN
import shutil
from thumb_gen.worker import Generator
import torch
import gc


#from pathlib import Path

#Collection Curator is a "closeups" filter. It is a humble franken-script to filter pictures/videos without faces, helping the curation process of collections.

detector = MTCNN()
os.system('cls')

#Input from user, here you tell where to look for pictures. You can drag and drop folders.
source_input = input("Please drag & drop the directory containing images: ")
source_dir = (source_input)
source_dir = source_dir.strip('"')
source_dir2 = source_dir.replace('[', 'o[o')
source_dir2 = source_dir2.replace(']', 'o]o')
source_dir2 = source_dir2.replace('o[o', '[[]')
source_dir2 = source_dir2.replace('o]o', '[]]')
source_dirclean = source_dir2.replace('#', '[#]')
dest_dir = "E:\\Perfil\\Downloads\\FILTRADAS" + '\\' # <-- ***USER INPUT REQUIRED*** This will be your output folder, change it to your liking.

#Checks for output folder existence in dest_dir.
def nooutput():
     if os.path.exists(dest_dir):
        nofiles()
     else:
        os.mkdir(dest_dir)
        nofiles()

#Checks if you are trying to run the script without input files.
def nofiles():
     if os.listdir(source_dir):
        folders_eachfile(source_dir, source_dirclean)
     else:
        print('Input folder is empty, champ ;)')

#Checks the files inside input folder and filters non-image files.
def folders_eachfile(source_dir, source_dirclean):
    for imagefile in glob.iglob(source_dirclean + '/**/*.*', recursive=True):
     if imagefile.endswith(('jpg', 'JPG', 'png', 'PNG', 'jpeg', 'JPEG', 'bmp', 'BMP', 'mp4', 'MP4', 'mkv', 'MKV', 'm4v', 'M4V', 'webm', 'WEBM', 'avi', 'AVI', 'wmv', 'WMV', 'mov', 'MOV', 'ts', 'TS')):
        filename = os.path.basename(imagefile)
        path = os.path.dirname(imagefile)
        global path2
        path2 = ((path.split(os.path.sep, 3)[-1] + '\\'))
        do_each_file(source_dir, imagefile, path2, filename )

#Makes sure the output folders of galleries are made or exists. 
def do_each_file(source_dir, imagefile, path2, filename ):
     if os.path.exists(dest_dir + path2):
        outputfile = (dest_dir + path2 + filename)
        detect_face(imagefile, outputfile)
     else:
        os.makedirs(dest_dir + path2)
        outputfile = (dest_dir + path2 + filename)
        detect_face(imagefile, outputfile)
        return

#Main script, detects faces in images and outputs only the images with faces detected.
def detect_face( imagefile, outputfile ):
    if imagefile.endswith(('jpg', 'JPG', 'png', 'PNG', 'jpeg', 'JPEG', 'bmp', 'BMP')):
        img = cv2.cvtColor(cv2.imread(imagefile), cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(img)
        torch.cuda.empty_cache()
        if len(faces) != 0:
            print(os.path.basename(imagefile) + '   OK ●')
            shutil.move(imagefile, outputfile)
            remove_metadata(outputfile, imagefile)
        else:
            print(os.path.basename(imagefile) + '   NO ○')
    else:
        if imagefile.endswith(('mp4', 'MP4', 'mkv', 'MKV', 'm4v', 'M4V', 'webm', 'WEBM', 'avi', 'AVI', 'wmv', 'WMV', 'mov', 'MOV', 'ts', 'TS')):
            videoprocess(imagefile, outputfile)

#Processes the videos detected in the source folder
def videoprocess(imagefile, outputfile):
    app = Generator(imagefile, imgCount=30, custom_text=False, font_size=1, bg_colour='blue', font_colour='red')
    app.run()
    thumbs = os.path.splitext(imagefile)[0]+'.jpg'
    img = cv2.cvtColor(cv2.imread(thumbs), cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(img)
    if len(faces) != 0:
        shutil.move(imagefile, outputfile)
        print('GOOD! SAVING VIDEO')
        os.remove(thumbs)
        torch.cuda.empty_cache()
    else:
        print('NO FACE DETECTED IN VIDEO')
        os.remove(thumbs)
        torch.cuda.empty_cache()

#Removes metadata from output pictures
def remove_metadata(outputfile, imagefile):
    global path2
    try:
        image = Image.open(outputfile)
        image_data = list(image.getdata())
        new_image = Image.new(image.mode, image.size)
        new_image.putdata(image_data)
        if os.path.isfile(dest_dir + path2 + 'folder.jpg'):
            new_image.save(outputfile)
            return
        else: 
            new_path = (dest_dir + path2)
            new_name = (new_path + 'folder.jpg')
            os.rename(outputfile, new_name)
            return
    except Exception as err:
        print(err)
        return False

gc.collect()
nooutput()