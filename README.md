# Collection Curator script
A python (over windows) script to filter pictures and videos without faces in them using face detection from MTCNN.

![til](https://github.com/masterofobzene/CollectionCurator-script/blob/main/realtime.gif)

### What does this do?

* Filters pictures and videos with faces by moving them in a preconfigured folder. (you can change the folder)
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
* [NVIDIA CUDA Toolkit]
* [NVIDIA Deep Neural Network library (cuDNN)]


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

 
