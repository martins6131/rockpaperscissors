import random

def play_round(player_selection, computer_selection):
    if player_selection == computer_selection:
        return "It's a tie!"
    
    if player_selection == 'rock':
        if computer_selection == 'paper':
            return """You lose! 
            Paper beats rock."""
        else:
            return """You win! 
            Rock beats scissors."""
    
    if player_selection == 'paper':
        if computer_selection == 'scissors':
            return """You lose! 
            Scissors beat paper."""
        else:
            return "You win! Paper beats rock."
    
    if player_selection == 'scissors':
        if computer_selection == 'rock':
            return """You lose! 
            Rock beats scissors."""
        else:
            return """You win!
             Scissors beat paper."""

def computer_play():
    randomNumber = random.randint(0, 2)
    
    if randomNumber == 0:
        return 'rock'
    elif randomNumber == 1:
        return 'paper'
    elif randomNumber == 2:
        return 'scissors'

def game():
    player_score = 0
    computer_score = 0
    
    for i in range(5):
        player_selection = input('Rock, paper, or scissors? ').lower()
        computer_selection = computer_play()
        
        round_result = play_round(player_selection, computer_selection)
        print(round_result)
        
        if 'win' in round_result:
            player_score += 1
        elif 'lose' in round_result:
            computer_score += 1
    
    print("Player score: {player_score}")
    print("Computer score: {computer_score}")
    
    if player_score > computer_score:
        print("You win the game!")
    elif computer_score > player_score:
        print("You lose the game!")
    else:
        print("The game is tied!")

game()
