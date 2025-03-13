import random

def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'
    
# Initialize score counters
player_score = 0
computer_score = 0
ties = 0

# Initialize counters for each move
player_wins_by_move = {'rock': 0, 'paper': 0, 'scissors': 0}
computer_wins_by_move = {'rock': 0, 'paper': 0, 'scissors': 0}
ties_by_move = {'rock': 0, 'paper': 0, 'scissors': 0}

print('Welcome to Rock, Paper, Scissors!')

while True:
    # Get player choice
    player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").strip().lower()
    if player_choice == 'quit':
        break
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue
    
    # Get computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer choice: {computer_choice}")
    
    # Determine the result of the round
    result = play_round(player_choice, computer_choice)
    
    if result == 'player':
        player_score += 1
        player_wins_by_move[player_choice] += 1
        print("You win this round!")
    elif result == 'computer':
        computer_score += 1
        computer_wins_by_move[computer_choice] += 1
        print("Computer wins this round!")
    else:
        ties += 1
        ties_by_move[player_choice] += 1
        print("This round is a tie!")
    
    # Print current scores and moves
    print(f"Scores - Player: {player_score}, Computer: {computer_score}, Ties: {ties}")
    print(f"Player Wins by Move: {player_wins_by_move}")
    print(f"Computer Wins by Move: {computer_wins_by_move}")
    print(f"Ties by Move: {ties_by_move}")

# Final Score
print("Thanks for playing!")
print(f"Final Scores - Player: {player_score}, Computer: {computer_score}, Ties: {ties}")
 





