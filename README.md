# Voice_Translator
## This repository contains project created for Speech Technology classes with use of Techmo TSS.

This branch contains work-in-progress, WSL2-free TTS implementation with proper instalation instructions and working YAML file for installing packages needed to run program. 

## Work in progress changes:

# 1. Currently updated:
- README.md file
- YAML file change name to "ST_Project" for naming clarity:
    - added conda-forge and anaconda channels
    - added pip dependencies for installing TTS requirements (deleted requirements.txt - now it is useless)
- commented main.py file
- splitted main.py into UI instance (first version) and code instance (second version)
- set Records/test.wav as default
- updated .gitignore

UI works on PyQt5 library with design from QT Designer app.

### Work in progress - content:

## Content

## Installation


------
This branch contains working Techmo TTS module applied to main.py file.
To try it out use `main.py` file. Simply insert your desired input in `synthesize` function.

This is default version which returns at the moment only Polish phrases.
Files in .wav format should be overwritten by new input.

NOTE: pyqt5 install is required through Windows WSL sunbsystem to avoid errors.

sudo apt-get install -y libxcb-util-dev
ON cmd :
pip install --upgrade google-api-python-client
ON |Ubuntu:
$ apt install -y protobuf-compiler