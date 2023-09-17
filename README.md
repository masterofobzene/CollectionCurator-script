# Collection Curator script
A python (over windows) script to filter pictures and videos without faces in them using face detection from MTCNN.

![til](https://github.com/masterofobzene/CollectionCurator-script/blob/main/real.gif)

### What does this do?

* Filters pictures and videos with faces by moving them in a preconfigured folder. (you __must__ change the folder on first use)

### What does it NOT do?

* It doesn't send any info over internet.
* It doesn't DELETE ANYTHING.
* It doesn't recognize the faces (no tagging done)

# Pre-requisites:
### RESTRICTIVE REQUIREMENTS (requires free registration on nvidia site):
* [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive)
* [NVIDIA Deep Neural Network library (cuDNN)](https://developer.nvidia.com/cudnn)


-----------------------------------------
### Install:
1- Install pre-requisites above
2- Download latest release
3- Unzip
4- Execute "install.bat"
5- Change your output folder by opening "CollectionCurator.py" with notepad. (line 31)

# Usage:
Double click "CollectionCurator.py" and when prompted, drag and drop your folder full of pictures/videos to be filtered and press {enter}.

---------------------------------------------------------------

 
This script uses Thumbnail Generator from https://github.com/truethari/thumb-gen
..and to be honest, a lot more pieces of code from many scripts. To the respective owners, thank you.
