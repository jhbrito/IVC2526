# IVC2526

# CONDA
## Create conda environment
conda create -n IVC2526P311Env -python=3.11

or

conda create -p PATH python=3.11

# Install packages
conda install jupyter
conda install pillow
conda install scikit-image
conda install tk
pip install opencv-contrib-python

## Export conda environment
conda env export > environment.yml

## Import conda environment
conda env create -n Project_Environment_Name --file environment.yml

# PIP

## Import pip environment
pip install -r requirements.txt

## Export pip environment
pip freeze > requirements.txt

## Unofficial Windows Binaries for Python Extension Packages
<https://www.lfd.uci.edu/~gohlke/pythonlibs/>

# Fix YOLO for GPU
pip uninstall torch torchvision torchaudio

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
