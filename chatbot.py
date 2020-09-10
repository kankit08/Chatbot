#!/usr/bin/python3.8
#Descrition: A cahtbot in python
#library to install
#pip3 install nltk

from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)',['hi %1']],
    ['(hi |hello |hey| holla| hola)',['hey there']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed a fun']],
    ['(.*) (location|city) ?', 'New Delhi, India'],
    ['(.*) created you  ?', ['Ankit did using NLTK']]
    ['how is the weather  in (.*)',['the weather in %1 is amazing like always']]
    ]
chat = Chat(pairs, reflections)
print("Here is the chatbot: ")
input("Press Enter to start")
print(chat.converse())