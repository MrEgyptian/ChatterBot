from spellchecker import SpellChecker
def fix_spelling(sentence):
 spell = SpellChecker()
 u=sentence.text.lower().split(' ')
 corrected=[]
 for i in u:
  corrected+=[spell.correction(i)]
 sentence.text=' '.join(u)
# print(sentence.text)
 return sentence
