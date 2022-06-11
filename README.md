# NSFW Collection Curator script
A python (over windows) script to filter pictures and videos without faces in them using face detection from MTCNN.

### Why?
I collect NSFW multimedia and I HATE closeups, "c_ntshots", headless or bad angles where the performer's face cannot be seen. The increased randomness in quality of onlyfans content (and alikes) and the availability of large "packs" makes curation a time consuming process.
I searched hi and low for a script to only filter the images/videos with detected faces but couldn't find any. No other script that I found would separate images/videos with faces from those without them so I had to make one for myself.

![til](https://github.com/masterofobzene/CollectionCurator-script/blob/main/realtime.gif)

### What does this do?

* Filters pictures and videos with faces by saving them in a preconfigured folder. (you can change the folder)
* It removes metadata from output pictures automatically after face detection.
* Renames the first image to 'folder.jpg' to make a folder image (Win 10)

### What does it NOT do?

* It doesn't send any info over internet.
* It doesn't DELETE ANYTHING.
* It doesn't recognize the faces (no tagging done)

# Pre-requisites:

### Please download the whole files from repo: 
https://github.com/masterofobzene/CollectionCurator-script/archive/refs/heads/main.zip
Decompress on the folder you want it to remain.


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
* shutil ```pip install shutil```
* OpenCV ```pip install opencv```

This script uses Thumbnail Generator from https://github.com/truethari/thumb-gen
..and to be honest, a lot more pieces of code from many scripts. To the respective owners, thank you.

# Usage:

## __First mandatory step:__ 
Change the *dest_dir* path (watch for ***USER INPUT REQUIRED***) to the path you want your __output__ files to go.

## __Optional (but highly recommended) step:__
Download ['mtcnn.py'](https://fs-01.cyberdrop.to/mtcnn-mrSOkzKU.zip) and replace your 'mtcnn.py' in (C:\Users\yourusername\AppData\Local\Programs\Python\Python38\Lib\site-packages\mtcnn\mtcnn.py).
Don't worry, the file is vainilla it just has my parameters to end with less false positives.
Then the use is simple. Just open the script, drag & drop the desired folder to be curated, hit 'enter' then wait.

---------------------------------------------------------------
### Here are a couple of tips/warnings/FAQ/did you know's?:
* Check the *input folders* before deleting them. The script is far from perfection and some pictures you might like might be missed.
* The script doesn't like paths with double quotes, so I made the script remove them automatically if it finds them in your source path.
* Removal of metadata is done to the output files only.
* I didn't make the "dest_dir" input to be requested by the script since most people will have to configure this path just one time.
* Video detection depends on how many pics are inside the thumbnails generated. You can change how many from the script, search for this (no quotes) "imgCount=" the value next to it is how many pics will be generated. Less = faster,worse detection; more= slower,better detection.
* Are you a pro? want to give advise/fix or upgrade the script? use the issues section and be humble.
* Renaming one .jpg picture inside a folder as "folder.jpg" makes it a "folder image" AKA "folder thumbnail"; very useful on Windows 10. (stupid MS removed them in 11).
* Windows 11 is a beta for a real next gen Windows. Skip it, trust me. They always do the same.
* I made this script to meet my own demands, don't get mad if you feel something is missing.
* Speed on a 3080 RTX is 2 seconds per photo (3744 x 5616 pixels) aprox. This is variable according to picture sizes.
* I'm not responsible in any way of the use you give to this script.
* This is a "Franken-script". You are free to use the code for your own projects as well.
* Metadata is used by filehostings (among many, many others) to "search & destroy" the files.
* I discovered that by doing a "thumbnail list" of the videos and then scanning that file with MTCNN is way faster than detecting frame by frame for face presence in videos. It has a downside: it will be less acuarate because we are taking small samples of the videos instead of scanning all the video, but I resolved that the tradeoff is bearable.
* Pictures and Videos are moved to output dir. This is to reduce impact on HDD space while doing the filtering process and I found its easier to check and compare the "leftovers".
* You may notice that output pictures have a reduced filesize than originals, this is due to metadata removal.

 
