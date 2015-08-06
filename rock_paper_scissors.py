import math
import random

def play_game ():
	number_of_games = 5
	games_to_win = int(math.ceil(number_of_games/2.0))
	player_wins = 0
	computer_wins = 0
	print "Best of %d!" %number_of_games
	while number_of_games:
		choices = ['rock','paper','scissors']
		computer_choice = random.choice(choices)
		player_choice = raw_input("Rock, Paper, or Scissors? ").lower()
		valid_choice = False
		while valid_choice == False:
			if player_choice not in choices:
				player_choice = raw_input("Invalid response, try again: Rock, Paper, or Scissors? ").lower()
			else:
				valid_choice = True
		#print "C: %s P: %s" %(computer_choice, player_choice)
		if computer_choice == 'rock' and player_choice == 'rock':
			print "Tie: %s vs %s" %(computer_choice, player_choice)
		elif computer_choice == 'rock' and player_choice == 'paper':
			print "You win: %s vs %s" %(computer_choice, player_choice)
			player_wins = player_wins + 1
		elif computer_choice == 'rock' and player_choice == 'scissors':
			print "Computer wins: %s vs %s" %(computer_choice, player_choice)
			computer_wins = computer_wins +1
		elif computer_choice == 'paper' and player_choice == 'rock':
			print "Computer wins: %s vs %s" %(computer_choice, player_choice)
			computer_wins = computer_wins +1
		elif computer_choice == 'paper' and player_choice == 'paper':
			print "Tie: %s vs %s" %(computer_choice, player_choice)
		elif computer_choice == 'paper' and player_choice == 'scissors':
			print "You win: %s vs %s" %(computer_choice, player_choice)
			player_wins = player_wins + 1
		elif computer_choice == 'scissors' and player_choice == 'rock':
			print "You win: %s vs %s" %(computer_choice, player_choice)
			player_wins = player_wins +1
		elif computer_choice == 'scissors' and player_choice == 'paper':
			print "Computer wins: %s vs %s" %(computer_choice, player_choice)
			computer_wins = computer_wins +1
		elif computer_choice == 'scissors' and player_choice == 'scissors':
			print "Tie: %s vs %s" %(computer_choice, player_choice)


		number_of_games = number_of_games -1

		print "%d vs %d" %(player_wins,computer_wins)

		if player_wins >= games_to_win:
			print "\nYou are the winner!"
			break
		elif computer_wins >= games_to_win:
			print "\nComputer is the winner!"
			break
		elif number_of_games == 0:
			print "Tiebreaker round!"
			number_of_games = number_of_games + 1
		
			



		

play_game()


