#The main program coordinating the guess game
#Build a quiz game that presents questions to a player, checks their answers, updates and displays their score progressively, and records completed games in a persistent JSON leaderboard.
from player import Player
import random
from data import question_data
from question_model import Question
from quiz_brain import  QuizBrain
from leaderboard import LeaderBoard

#All questions
questions = [Question(item) for item in question_data]
# print(questions)


still_playing = True
print("Welcome to the quiz game.")
while still_playing:
    option = input("Menu\n1. Play game\n2. Check Leaderboard\n3. Quit\nSelect an option [1,2,3] from the following: ").strip()
    leaderboard = LeaderBoard()
    if option == "1":
        player = Player()
        #Creat or load leader board
        
        

        question_bank = random.sample(questions, 12)
        quiz_brain = QuizBrain(question_bank)
        while quiz_brain.still_questions():
            player_answer, correct_answer = quiz_brain.next_question()
            quiz_brain.check_answer(player_answer,correct_answer)
            print()
        print(f"You scored {quiz_brain.score}/{len(quiz_brain.questions)}\n")
        winner_name = f"{player.name[0]} {player.name[1]}"
        leaderboard.update_leaderboard(winner_name, quiz_brain.score )
        # leaderboard.save_leaderboard()

    elif option == "2":
        leaderboard.display_leaderboard()
    elif option == "3":
        break
    else:
        print("Wrong option selected")  


