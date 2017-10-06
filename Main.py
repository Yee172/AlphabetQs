#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/9/26'


from Func import *
MODE = 'SEARCH'
RANDOM_LETTER = 'all'


print('Initail mode is SEARCH mode!')
while 1:
    if MODE.lower() == 'search':
        print()
        content = input('Your word or num: ')
        if content.lower() in ['q', 'quit', 'exit']:
            break
        if content.lower() in ['r', 'rand', 'random']:
            clear_screen()
            print('You are in RANDOM mode now!')
            MODE = 'RANDOM'
            continue
        try:
            content = int(content)
        except:
            pass
        word = find_word(content)
        if word is None:
            continue
        print('\nYour word:       %s' % word.word)
        definition_q(word)
    if MODE.lower() == 'random':
        print()
        content = input('Your random letter: ')
        if content.lower() in ['q', 'quit', 'exit']:
            break
        if content.lower() in ['s', 'sear', 'search']:
            clear_screen()
            print('You are in SEARCH mode now!')
            MODE = 'SEARCH'
            continue
        try:
            word = random_word(content)
            if word is None:
                print('Word not available! Rolling back!')
                raise
            RANDOM_LETTER = content
        except:
            word = random_word(RANDOM_LETTER)
        print('        #      : %d' % word.num)
        print('Your word      : %s' % word.word)
        definition_q(word)
