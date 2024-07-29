import googletrans
from googletrans import Translator
file = "testfile.txt"

translatedtext = 'de'
filetranslator = Translator()
detectlang = filetranslator.detect(file).lang.lower()
destlang = translatedtext.lower()

with open(file, 'r') as file:
    #file.write("Hello, this is a test file.")
    test = file.read()

newfile = "testfile" + destlang + ".txt"

translation = filetranslator.translate(test, src=detectlang, dest=destlang)
with open(newfile, 'w') as f:
    f.write(translation.text)

#print(test)
#print(f"file '{file}' was created.")
print(f"file '{newfile}' was created.")