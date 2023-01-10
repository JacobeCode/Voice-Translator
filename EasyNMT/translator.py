from easynmt import EasyNMT

class Translator:

    def __init__(self):
        self.opus=EasyNMT('opus-mt',max_length=512,device='cpu',)
        #self.mbart=EasyNMT('mbart50_en2m',max_length=512,device='cuda')
        self.mbart = EasyNMT('m2m_100_418M', max_length=512, device='cuda')

        directions_for_opus=[['pl','en'],['es','pl'],['pl','es'],['es','en'],['en','es']]
        for direction in directions_for_opus:
            self.opus.translate("initialization text",source_lang=direction[0],target_lang=direction[1])
        self.mbart.translate("",source_lang='en',target_lang='pl')


    def translate(self,sentence,source_lang,target_lang):
        if source_lang=='en' and target_lang=='pl':
            translated_sentence= self.mbart.translate(sentence,source_lang='en',target_lang='pl')
        elif source_lang==target_lang:
            translated_sentence=sentence
        else:
            translated_sentence= self.opus.translate(sentence,source_lang=source_lang,target_lang=target_lang)

        return translated_sentence