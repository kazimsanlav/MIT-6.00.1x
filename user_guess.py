# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:21:42 2017

@author: kazIm
"""
is_correct = ""
low = 0
high = 100
guess = int((low+high)/2)
print("Please think of a number between 0 and 100!")


while(is_correct != "c"):
    print("Is your secret number", guess, "?")
    is_correct = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while((is_correct in ["h", "l", "c"]) == False):
        print("Sorry, I did not understand your input.")
        print("Is your secret number", guess, "?")
        is_correct = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(is_correct == "h"):
        high = guess
        guess = int((low+high)/2)
    elif(is_correct == "l"):
        low = guess
        guess = int((low+high)/2)
print("Game over. Your secret number was:", guess)