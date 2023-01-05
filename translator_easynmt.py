from easynmt import EasyNMT

opus=EasyNMT('opus-mt')
mbart=EasyNMT('mbart50_en2m', device="cpu")

directions_for_opus=[['pl','en'],['es','pl'],['pl','es'],['es','en'],['en','es']]
for direction in directions_for_opus:
    opus.translate("initialization text",source_lang=direction[0],target_lang=direction[1])
mbart.translate("",source_lang='en',target_lang='pl')


def translate(sentence,source_lang,target_lang):
    if source_lang=='en' and target_lang=='pl':
        translated_sentence=mbart.translate(sentence,source_lang='en',target_lang='pl')
    else:
        translated_sentence=opus.translate(sentence,source_lang=source_lang,target_lang=target_lang)

    return translated_sentence