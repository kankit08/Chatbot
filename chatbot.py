#!/usr/bin/python3.8
#Descrition: A cahtbot in python
#library to install
#pip3 install nltk

from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)',['hi %1']],
    ['(hi |hello |hey| holla| hola)',['hey there']]
    ]
chat = Chat(pairs, reflections)
print("Here is the chatbot: ")
input("Press Enter to start")
print(chat.converse())