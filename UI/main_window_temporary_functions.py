import time
import wave
import pyaudio

from TTSTechmo.synthesize import synthesize
from TTSTechmo.settings import setup
from EasyNMT.translator_easynmt import translate
from PyQt5 import QtCore, QtGui, QtWidgets

    settings = setup()
    def RecordInput(self):
        pass
    def PlaySynthesis(self):
        chunk=1024
        file = wave.open("test.wav","rb") 
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(file.getsampwidth()),  
                channels = file.getnchannels(),  
                rate = file.getframerate(),  
                output = True)
        data = file.readframes(chunk)
        while data:  
            stream.write(data)  
            data = file.readframes(chunk)   
        stream.stop_stream()  
        stream.close()      
        p.terminate()  
    def SetInputText(self):
        self.settings.text_to_translate = self.input_text_line_edit.toPlainText()  
    def SetInputLanguage(self):
        if self.source_language_box.currentText() == "English":
            self.settings.language_source = 'en'
        elif self.source_language_box.currentText() == "Polish":
            self.settings.language_source = 'pl'
        elif self.source_language_box.currentText() == "Spanish":
            self.settings.language_source = 'es'
    def SetTranslationLanguage(self):
        if self.translation_language_box.currentText() == "English":
            self.settings.language = 'en'
            self.settings.tts_lang = 'tts-en'
        elif self.translation_language_box.currentText() == "Polish":
            self.settings.language = 'pl'
            self.settings.tts_lang = 'tts-pl'
        elif self.translation_language_box.currentText() == "Spanish":
            self.settings.language = 'es'
    def Translate(self):
        t = time.time()
        self.settings.text = translate(self.settings.text_to_translate, self.settings.language_source, self.settings.language)
        self.output_text_edit.setText(self.settings.text)
        elapsed = time.time() - t
        self.data_box.setText("Elapsed time of operation : " + str(elapsed))
    def TranslateAndSynthesize(self):
        t = time.time()
        self.settings.text = translate(self.settings.text_to_translate, self.settings.language_source, self.settings.language)
        self.output_text_edit.setText(self.settings.text)
        tsynt = time.time()
        synthesize(self.settings)
        elapsed = time.time() - t
        elapsedsynt = time.time() - tsynt
        self.data_box.setText("Elapsed time of operation : " + str(elapsed) + "/nSynthesis elapsed time : " + str(elapsedsynt) + "/nTranslation elapsed time : " + str(elapsed - elapsedsynt))
    def ReplaceLanguages(self):
        source_lang = self.source_language_box.currentIndex()
        self.source_language_box.setCurrentIndex(self.translation_language_box.currentIndex())
        self.translation_language_box.setCurrentIndex(source_lang)
        self.SetInputLanguage()
        self.SetTranslationLanguage()