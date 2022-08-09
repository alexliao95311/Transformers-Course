from transformers import pipeline
print('Welcome to the English to Chinese Translator\n')
flag = True
while flag:
    translator = pipeline('translation', model = 'Helsinki-NLP/opus-mt-en-zh')
    user_input = str(input('Input text to translate: '))
    res = translator(user_input)
    print(res)
    cont = str(input('Do you want to translate more text? (y/n): '))
    if cont == 'n':
        flag = False
print('Program exited')
