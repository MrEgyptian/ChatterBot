import re
import string

def fix_punkt(sentence):
 text=sentence.text
 text = ' '.join(text.split())
 # Remove leading/trailing punctuation
 text = text.strip(string.punctuation)
 # Replace multiple punctuation marks with a single space
 text = re.sub(r'[' + re.escape(string.punctuation) + r']+', ' ', text)
 # Fix spacing around punctuation marks
 text = re.sub(r'\s+([' + re.escape(string.punctuation) + r'])', r'\1', text)
 text = re.sub(r'([' + re.escape(string.punctuation) + r'])\s+', r'\1', text)
 # Fix quotes
 text = text.replace('``', '“').replace("''", '”').replace("`", "'")
 text = text.capitalize()
 sentence.text=text
 exceptions = ['I']
 text = ' '.join(word.lower() if word not in exceptions else word for word in text.split())
 return sentence
