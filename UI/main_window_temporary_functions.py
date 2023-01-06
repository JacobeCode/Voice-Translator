import time

from TTSTechmo.synthesize import synthesize
from TTSTechmo.settings import setup
from EasyNMT.translator_easynmt import translate
from PyQt5 import QtCore, QtGui, QtWidgets

settings = setup()

    def SetInputText(self):
        self.settings.text_to_translate = self.input_text_line_edit.toPlainText()
    def SetInputLanguage(self):
        if self.entry_language_box.currentText() == "English":
            self.settings.language_source = "en"
        elif self.entry_language_box.currentText() == "Polish":
            self.settings.language_source = "pl"
        elif self.entry_language_box.currentText() == "Spanish":
            self.settings.language_source = "es"
    def SetTranslationLanguage(self):
        if self.exit_language_box.currentText() == "English":
            self.settings.language = "en"
            self.settings.tts_lang = "tts-en"
        elif self.exit_language_box.currentText() == "Polish":
            self.settings.language = "pl"
            self.settings.tts_lang = "tts-pl"
        elif self.exit_language_box.currentText() == "Spanish":
            self.settings.language = "es"
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
        source_lang = self.entry_language_box.currentIndex()
        self.entry_language_box.setCurrentIndex(self.exit_language_box.currentIndex())
        self.exit_language_box.setCurrentIndex(source_lang)
        self.SetInputLanguage()
        self.SetTranslationLanguage()
