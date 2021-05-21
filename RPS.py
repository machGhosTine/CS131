# Assignment 'Rock-Paper-Scissors - RPS.py
# This program is my version of a rock, paper, scissors game in python.
# Hilbert College CS131
# November 1,2020

import random
import tkinter
from tkinter import PhotoImage

game_stats = []

def game_winner(call):
    if random.random() <= (1 / 3):
        rps = 'Rock'
    elif (1 / 3) < random.random() <= (2 / 3):
        rps = 'Scissors'
    else:
        rps = 'Paper'

    if (rps == 'Rock' and call == 'Paper') or (rps == 'Paper' and call == 'Scissors') or (rps == 'Scissors' and call == 'Rock'):
        game_stats.append('WIN')
        game_result = '\nGame Result: Guess what...you won!'
    elif rps == call:
        game_stats.append('DRAW')
        game_result = '\nGame Result: Ehh...it is a draw!'
    else:
        game_stats.append('LOSS')
        game_result = '\nGame Result: Bad news...you lost!'

    output.config(text='The Super-Computer has chosen: ' + rps + '\n' + game_result)
    outfile = open('Rock-Paper-Scissors_Results.txt', 'a')
    print('The Super-Computer has chosen:', rps, game_stats, game_result, file=outfile)

def game_scissors():
    game_winner('Scissors')

def game_rock():
    game_winner('Rock')

def game_paper():
    game_winner('Paper')

window = tkinter.Tk()
window.title('The Rock-Paper-Scissors Game')

rock_img = PhotoImage(file='rock.gif')
scissor_img = PhotoImage(file='scissors.gif')
paper_img = PhotoImage(file='paper.gif')

rock = tkinter.Button(window, image=rock_img, text='Rock', bg="#000000", padx=10, pady=5, command=game_rock, width=155)
scissors = tkinter.Button(window, image=scissor_img, text='Scissors', bg='#000000', padx=10, pady=5, command=game_scissors, width=155)
paper = tkinter.Button(window, image=paper_img, text='Paper', bg='#000000', padx=10, pady=5, command=game_paper, width=155)
output = tkinter.Label(window, width=35, fg='#000000', text='Welcome to the Rock-Paper-Scissors Game!\n\nWhat will you choose?')

rock.pack(side='left')
paper.pack(side='left')
scissors.pack(side='left')
output.pack(side='right')
window.mainloop()

for i in game_stats:
    print(i, end=" ")
if game_stats.count('Loss') > game_stats.count('Win'):
    game_result = "\nBad news...you lost!"
elif game_stats.count('Loss') == game_stats.count('Win'):
    game_result = "\nthe game ended in a draw!"
else:
    game_result = "\nGuess what...you won!"

print(game_result)
