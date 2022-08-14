from transformers import pipeline
from tkinter import *
import tkinter.font as font

#Button Command
def translate():
    btn.configure(text='Translated')
    text = txtfld.get()
    translator = pipeline('translation', model = 'Helsinki-NLP/opus-mt-en-zh')
    result = translator(text)[0]['translation_text']
    res.insert(END, result)
    
#Initialize Window
window = Tk()
window.title('English to Chinese Translator')
window.geometry('600x400+10+10')

#Title Text
maintext = Label(window, text = "English to Chinese Translator", fg = 'blue', font = ('arial', 24))
maintext.place(x = 100, y = 30)

#Note Text
notetext = Label(window, text = 'Note: please wait patiently while we translate!', fg = 'red', font = ('arial', 14))
notetext.place(x = 130, y = 70)

#User Input
input_text = Label(window, text = 'Input Text:', fg = 'blue', font = ('arial', 14))
input_text.place(x=240, y = 120)
txtfld = Entry(window, text = None, bd = 10, font = 20)
txtfld.place(x = 175, y = 150)

#Translate Button
btn = Button(window, text = 'Translate Text', fg = 'blue', command = translate)
btn['font'] = font.Font(size=16)
btn.config(width=20)
btn.place(x = 130, y = 210)

#Result
restext = Label(window, text = 'Result', fg = 'blue', font = ('arial', 14))
restext.place(x=260, y=290)
res = Entry(window, text = 'Result', bd = 10, font = 20)
res.place(x = 175, y = 320)

#Mainloop
window.mainloop()

