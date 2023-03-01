# This is a sample Python script.
import sys
import certifi
import pymongo
from pymongo import MongoClient
from word_generator import get_random_word,fill_database,clear_database
from game_functions import make_player_guess,check_player_input,  player_state, game_outcome
def run_game():
    print("Welcome to the game !\n")
    index_list = []  # will be used to get locate letters which the player guesses correctly
    game_over = False
    attempts = 7
    word = list(get_random_word())
    player_guess = make_player_guess(word)
    while game_over == False:
        print(word)
        print(player_guess)
        print()
        player_input = input("Your play: ", )
        attempts = check_player_input(attempts,player_input,player_guess,index_list,word)
        game_over = player_state(attempts, player_guess, word)
    game_outcome(player_guess)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #fill_database('words.txt') #FIlls the db with words from a text file, only runs when needed.
    run_game()

