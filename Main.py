#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'


from Func import *


while 1:
    print()
    content = input('Your word or num: ')
    if content in ['q', 'quit', 'exit']:
        break
    try:
        content = int(content)
    except:
        pass
    word = find_word(content)
    if word is None:
        continue
    print('\nYour word:       %s' % word.word)
    definition = input('Your definition: ')
    print()
    print('Your definition: %s' % definition)
    print('Real definition: %s' % word.definition)
    if word.definition.lower() == definition.lower():
        print('Exactly!')
    else:
        print('Not so good!')
    print()
    print('Sample sentence: %s' % word.get_sample())
    print('\n' * 17)

