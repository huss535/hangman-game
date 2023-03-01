def make_player_guess(word_list):
    new_list = []
    for i in range(len(word_list)):
        new_list.append("-")
    return new_list



def letter_instances(index_list, letter, player_guess, word_list):
    for i in range(len(word_list)):
        if letter.lower() == word_list[i].lower():
            index_list.append(i)
            player_guess[i] = word_list[i]


def player_state(attempts, player_list, word_list):
    if  attempts <= 0:
        return True
    else:
        return False

def game_outcome(player_guess):
    if "-" in player_guess:
        print("Sorry you lose!")

    else:
        print("Congratulations, you won !")

def check_player_input(attempts,player_input,player_guess,index_list,word):
    if player_input.isspace():
        print("It's empty bro!")
        return attempts      
    elif len(player_input.strip()) > 1:
        print("You can't enter more than one letter")
        return attempts
    elif len(player_input.strip()) == 1 and not(player_input.isalpha()):
        print("Not a letter !")
        return attempts
    if player_input in word and ( player_input not in player_guess) :

            letter_instances(index_list, player_input, player_guess, word)
            print("Hey good guess\n")

    elif player_input in word and ( player_input  in player_guess):
        print("You already guessed this !?!\n")

    else:
        attempts -= 1
        print("No luck I'm afraid 😔\n")
    return attempts
