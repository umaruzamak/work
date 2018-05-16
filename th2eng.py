# from translate import Translator
# to_lang = 'zh'
# secret = '<your secret from Microsoft>'
# translator = Translator(provider='microsoft', to_lang=to_lang, secret_access_key=secret)
# translator.translate('the book is on the table')
# print (translator)


from translate import Translator
translator1= Translator(to_lang="th")
translation = translator1.translate("This is a pen.")
translator2= Translator(to_lang="en")
translation2 = translator2.translate("นี่คือปากกา")
print(translation)
print(translation2)