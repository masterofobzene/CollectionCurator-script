import os
import glob
import numpy as np
import cv2
from PIL import Image
from mtcnn import MTCNN
#import tensorflow as tf
#tf.compat.v1.disable_eager_execution()

#Collection Curator is a "closeups" picture remover. It is a humble and newbie-made script to filter pictures without faces, helping the curation process of picture collections. This was thought with NSFW use in mind but you can use it for other purposes.

#Input from user, here you tell where to look for pictures. You can drag and drop folders.
source_input = input("Please paste the directory containing images: ")
source_dir = (source_input)
source_dir = source_dir.strip('"')
source_dir2 = source_dir.replace('[', 'o[o')
source_dir2 = source_dir2.replace(']', 'o]o')
source_dir2 = source_dir2.replace('o[o', '[[]')
source_dirclean = source_dir2.replace('o]o', '[]]')
dest_dir = "E:\\xxxxxxx\\xxxxxxxxxx\\xxxxxxxx\\" # <-- ***USER INPUT REQUIRED*** This will be your output folder, change it to your liking. Use double backlashes or it will error. MUST end with double backlashes too.




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
    for imagefile in glob.iglob(source_dirclean + '/**/*', recursive=True):
     if imagefile.endswith(('.jpg', '.png', '.jpeg')):
        print(imagefile)
        filename = os.path.basename(imagefile)
        path = os.path.dirname(imagefile)
        path2 = ((os.path.basename(path)) + '\\')
        do_each_file(source_dir, imagefile, path2, filename )

#Makes sure the output folders of galleries are made or exists. 
def do_each_file(source_dir, imagefile, path2, filename ):
     if os.path.exists(dest_dir + path2):
        outputfile = (dest_dir + path2 + '\\' + filename)
        detect_face(imagefile, outputfile)
     else:
        os.mkdir(dest_dir + path2)   
        outputfile = (dest_dir + path2 + '\\' + filename)
        detect_face(imagefile, outputfile)
        return

#Main script, detects faces in images and outputs only the images with faces detected.
def detect_face( imagefile, outputfile ):
    img = cv2.cvtColor(cv2.imread(imagefile), cv2.COLOR_BGR2RGB)
    detector = MTCNN()
    faces = detector.detect_faces(img)
    if len(faces) == 0:
        return;
    else:
        cv2.imwrite(outputfile, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        remove_metadata(outputfile)
        return;

#Removes exif metadata from output files
def remove_metadata(outputfile):
        try:
            image = Image.open(outputfile)
            image_data = list(image.getdata())
            new_image = Image.new(image.mode, image.size)
            new_image.putdata(image_data)
            new_image.save(outputfile)  
            return True
        except Exception as err:
            print(err)
            return False


nooutput()