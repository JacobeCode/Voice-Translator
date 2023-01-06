# UPDATE README !

# Voice_Translator

## This repository contains project created for Speech Technology classes with use of Techmo TSS and EasyNMT.

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
- sorted main files and directiories
- separated UI main and side window

UI works on PyQt5 library with design from QT Designer app.

Due to use of fasttext==0.9.2 installation of Visual Build Tools 2022 is needed.

### Description from EasyNMT branch :

translator_easynmt.py file contains implementation of translation models,as well as function for direct translation in chosen languages and directions.

EasyNMT package allow us to use multiple, pre-trained models for neural machine translation.The list below shows directions of translations,with models used for them:

pl->en  model: opus-mt-pl-en

en->pl  model: mbrat50_en2m

pl->es  model: opus-mt-pl-es

es->pl  model: opus-mt-es-pl

es->en  model: opus-mt-es-en

en->es  model: opus-mt-en-es

Additional function translate() handles exception of using different model for en->pl and return translated sentence.

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
