# NSFW Collection Curator script
A python (over windows) script to filter pictures and videos without faces in them using face detection from MTCNN.

### Why?
I collect NSFW multimedia and I HATE closeups, "c_ntshots", headless or bad angles where the performer's face cannot be seen. The increased randomness in quality of onlyfans content (and alikes) and the availability of large "packs" makes curation a time consuming process.
I searched hi and low for a script to only filter the images/videos with detected faces but couldn't find any. No other script that I found would separate images/videos with faces from those without them so I had to make one for myself.


### What does this do?

* Filters pictures and videos with faces by saving them in a preconfigured folder. (you can change the folder)
* It removes metadata from output pictures automatically after face detection.
* Renames the first image to 'folder.jpg' to make a folder image (Win 10)

### What does it NOT do?

* It doesn't send any info over internet.
* It doesn't DELETE ANYTHING.
* It doesn't recognize the faces (no tagging done)

# Pre-requisites:

### RESTRICTIVE REQUIREMENTS (requires free registration on nvidia site):
* [NVIDIA CUDA Toolkit](https://anonfiles.com/b2n7Mbbayc/cuda_11.6.0_511.23_windows.exe_7z)
* [NVIDIA Deep Neural Network library (cuDNN)](https://anonfiles.com/53ZfLcb5yc/cudnn-windows-x86_64-8.4.0.27_cuda11.6-archive_zip)

A word here; to get those install files from above you need to register with a special dev account at nvidia's site.
Since that is a loss of time and I don't give a fuck about nvidia's restrictive approach, I've uploaded the files for you
so you don't have to go like me through all the senseless and privacy mining process.
Updated versions of these files will require you to do this though, sadly.

-----------------------------------------
### Easy to install Requirements:
* Python 3 __(Please check installation steps on their website)__
* Tensorflow  ```pip install tensorflow```  __(Please check additional requirements/installation steps on their website)__
* Numpy  ```pip install numpy```
* PIL ```pip install pil```
* MTCNN ```pip install mtcnn```



# SCRIPT:
```python
import os
import glob
import time
import numpy as np
import cv2
from PIL import Image
from mtcnn import MTCNN
import shutil
from thumb_gen.__init__ import Generator

#Collection Curator is a "closeups" picture remover. It is a humble and newbie-made script to filter pictures without faces, helping the curation process of picture collections. This was thought with NSFW use in mind but you can use it for other purposes.
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
dest_dir = "E:\\Perfil\\Downloads\\CUNTSHOT FILTER OUTPUT\\" # <-- ***USER INPUT REQUIRED*** This will be your output folder, change it to your liking. Use double backlashes or it will error. MUST end with double backlashes too.




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
     if imagefile.endswith(('jpg', 'png', 'jpeg', 'bmp', 'mp4', 'mkv', 'm4a', 'webm', 'avi', 'wmv')):
        print(imagefile)
        filename = os.path.basename(imagefile)
        path = os.path.dirname(imagefile)
        global path2 
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
    if imagefile.endswith(('jpg', 'png', 'jpeg', 'bmp')):
        img = cv2.cvtColor(cv2.imread(imagefile), cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(img)
        if len(faces) != 0:
            cv2.imwrite(outputfile, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
            remove_metadata(outputfile, imagefile)
    else:
        if imagefile.endswith(('mp4', 'mkv', 'm4a', 'webm', 'avi', 'wmv')):
            videoprocess(imagefile, outputfile)

def videoprocess(imagefile, outputfile):
    app = Generator(imagefile,
    columns=3,
    rows=3,
    custom_text=False,
    font_size=1,
    bg_colour='blue',
    font_colour='red')
    app.run()
    thumbs = os.path.splitext(imagefile)[0]+'.jpg'
    img = cv2.cvtColor(cv2.imread(thumbs), cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(img)
    if len(faces) != 0:
        shutil.move(imagefile, outputfile)
        print('Good one! Saving')
        os.remove(thumbs)
    else:
        print('No face detected, cleaning thumbnails')
        os.remove(thumbs)

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


nooutput()
```

This script uses Thumbnail Generator from https://github.com/truethari/thumb-gen
..and to be honest, a lot more pieces of code from many scripts. To the respective owners, thank you.

# Usage:

## __First mandatory step:__ 
Change the *dest_dir* path (watch for ***USER INPUT REQUIRED***) to the path you want your __output__ files to go. __Use double backlashes.__ 

## __Optional (but highly recommended) step:__
Download 'mtcnn.py' and replace your 'mtcnn.py' in (C:\Users\yourusername\AppData\Local\Programs\Python\Python38\Lib\site-packages\mtcnn\mtcnn.py).
Don't worry, the file is vainilla it just has my parameters to end with less false positives.
Then the use is simple. Just open the script, drag & drop the desired folder to be curated, hit 'enter' then wait.

---------------------------------------------------------------
### Here are a couple of tips/warnings/FAQ/did you know's?:
* Check the *input folders* before deleting them. The script is far from perfection and some pictures you might like might be missed.
* The script doesn't like paths with double quotes, so I made the script remove them automatically if it finds them in your source path.
* Removal of metadata is done to the output files only.
* Your source files are left untouched. Delete them when you are sure you have all you want.
* I didn't make the "dest_dir" input to be requested by the script since most people will have to configure this path just one time.
* Are you a pro? want to give advise/fix or upgrade the script? use the issues section and be humble.
* Renaming one .jpg picture inside a folder as "folder.jpg" makes it a "folder image" AKA "folder thumbnail"; very useful on Windows 10. (stupid MS removed them in 11).
* Windows 11 is a beta for a real next gen Windows. Skip it, trust me. They always do the same.
* I made this script to meet my own demands, don't get mad if you feel something is lacking.
* Speed on a 3080 RTX is 2 seconds per photo (3744 x 5616 pixels) aprox. This is variable according to picture sizes.
* I'm not responsible in any way of the use you give to this script.
* This is a "Franken-python" script. You are free to use the code for your own projects as well.
* Feeling kind-hearted? share your NSFW sources on the Issues section. Use the [NSFW SOURCES] tag please. I might add them in the Wiki section for everyone to check out.
* Metadata is used by filehostings (among many, many others) to "search & destroy" the files.
* I discovered that by doing a "thumbnail list" of the videos and then scanning that file with MTCNN is way faster than detecting frame by frame for face presence in videos. It has a downside: it will be less acuarate because we are taking small samples of the videos instead of scanning all the video, but I resolved that the tradeoff is bearable.
* Pictures are COPIED to output dir while videos are MOVED. This is to reduce impact on HDD space while doing the filtering process.
* You may notice that output pictures have reduced filesize than originals, this is due to metadata removal.

 
