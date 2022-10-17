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
* Python 3.8.2__(Please check installation steps on their website)__
* Tensorflow  ```pip install tensorflow```  __(Please check additional requirements/installation steps on their website)__
* MTCNN ```pip install mtcnn```
* infomedia ```pip install infomedia```
* Pillow ```pip install pillow```
* pathlib ```pip install pathlib```


This script uses Thumbnail Generator from https://github.com/truethari/thumb-gen
..and to be honest, a lot more pieces of code from many scripts. To the respective owners, thank you.

# Usage:

## __First mandatory step:__ 
Change the *dest_dir* path (watch for ***USER INPUT REQUIRED***) to the path you want your __output__ files to go.


---------------------------------------------------------------

 
