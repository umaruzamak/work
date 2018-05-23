from translate import Translator


def translateForMe(fromLang, toLang, text):
    secret = '75a648040ae949f594acc7b25221a622'
    translator = Translator(provider='microsoft', from_lang=fromLang,
                            to_lang=toLang, secret_access_key=secret)
    translation = translator.translate(text)
    return translation


print(translateForMe('th', 'en', 'ไก่จิกเด็กตายบนปากโอ่ง'))
