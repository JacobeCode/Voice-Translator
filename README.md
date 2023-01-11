# Voice_Translator

## This repository contains project created for Speech Technology classes with use of Techmo TSS and EasyNMT.

This branch contains version 1.0.1 of Techmo TTS, EasyNMT and Whisper implementation in project for Speech Technology classes project with proper instalation instructions and working YAML file for installing packages needed to run program. 

## Installation/Requirements:

- PyTorch with CUDA compute platform (CUDA 11.6) (optional):

To use CUDA computing, it is required to install PyTorch with CUDA module with command:

`conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia`

It can be generated on 'Start locally' page of PyTorch:

[PyTorch]https://pytorch.org/get-started/locally/

It is optional, but recommended solution.

If you don't want to use CUDA as device, it is required to change in EasyNMT/translator - opus device to "cpu".

---

- Microsoft C++ Build Tools:

Because of use of fasttext ver.0.9.2 it is needed to install Microsoft C++ Build Tools (Programming classic applications in C++ load):

[Microsoft C++ Build Tools 2022](https://visualstudio.microsoft.com/pl/visual-cpp-build-tools/)

---

- Packages listed in ST_Project.yml:

To install packages run:

`conda env update -n "env_name" --file ST_project.yml`

Works properly on command-line, Powershell and also on Anaconda Prompt.

---

- ffmpeg package

Due to encountered problems, it is suggested to install independently ffmpeg-python package from conda-forge, as shown below:

`conda install -c conda-forge ffmpeg-python`

[Ffmpeg-python]https://github.com/conda-forge/ffmpeg-python-feedstock

## Content

This branch contains contains version 1.0.0 of Techmo TTS, EasyNMT and Whisper linked togheter to work as translator with synthesise speech output.

Available languages (with abbreviation) for input:
- English (en)
- Polish (pl)
- Spanish (es) (only text output)

Currently in both solutions .wav files are saved to proper folders folders, but it can be also saved and loaded through proper options (in UI solution).
Please, take into consideration that program in both version may take a while to launch.

- Code launch:

To launch translation and synthesis from 'code level' solution, open `main_code_launch.py`.
At the top of the code, you can find settings for program. 
Currently use:
- for input text pass string in `settings.text_to_translate = ""`
- for language from we translate pass language abbreviation in `settings.language_source = ''`
- for target language pass language abbreviation in `settings.language = ''`

Rest of settings to use in code solution are described in TTSTechmo/settings file.

---

- UI launch:

To launch translation and synthesis with UI solution open and run `main_UI_launch.py`.

---

### TTS Techmo

Folder and implementation contains TTS model with added value in form of classes and functions used in manipulating the synthesis.

---

### EasyNMT

Folder and implementation contains EasyNMT model with translator_easynmt.py file. It contains implementation of translation models, as well as function for direct translation in chosen languages and directions.

EasyNMT package allow us to use multiple, pre-trained models for neural machine translation.The list below shows directions of translations, with models used for them:

pl->en  model: opus-mt-pl-en

en->pl  model: mbrat50_en2m

pl->es  model: opus-mt-pl-es

es->pl  model: opus-mt-es-pl

es->en  model: opus-mt-es-en

en->es  model: opus-mt-en-es

Additional function translate() handles exception of using different model for en->pl and return translated sentence.

---

### UI work

UI works on PyQt5 library (ver.5.15.7) and was constructed with QT Designer app.
