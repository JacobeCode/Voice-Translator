# Voice_Translator
This repository contains project created for Speech Technology classes.

translator_easynmt.py file contains implementation of translation models,as well as function for direct translation in chosen languages and directions.

EasyNMT package allow us to use multiple, pre-trained models for neural machine translation.The list below shows directions of translations,with models used for them:

pl->en  model: opus-mt-pl-en

en->pl  model: mbrat50_en2m

pl->es  model: opus-mt-pl-es

es->pl  model: opus-mt-es-pl

es->en  model: opus-mt-es-en

en->es  model: opus-mt-en-es

Additional function translate() handles exception of using different model for en->pl and return translated sentence.
