import json
import os

class LeaderBoard:

    def __init__(self):
        self.leaderboard_file =  "leaderboard.json"
        # LOAD OR CREATE LEADERBOARD

        if not os.path.exists(self.leaderboard_file):

            self.leaderboard = {}

            with open(self.leaderboard_file, "w") as file:
                json.dump(self.leaderboard, file, indent=4)

        else:

            with open(self.leaderboard_file, "r") as file:
                self.leaderboard = json.load(file)
        print(self.leaderboard)

    def display_leaderboard(self):
        """
        Displays the current leaderboard.
        """
        print("\n========== LEADERBOARD ==========")

        if not self.leaderboard:
            print("No scores recorded yet.")

        else:
            self.sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda item: item[1], reverse=True )

            for position, (name, score) in enumerate(self.sorted_leaderboard,start=1):
                print(f"{position}. {name} - {score} points")

        print("=================================")

    def save_leaderboard(self):
        with open(self.leaderboard_file, "w") as file:
            json.dump(self.leaderboard, file, indent=4 )



    def update_leaderboard(self, winner_name, score):
        # self.winner_name =  winner_name
        self.score = score
        if winner_name not in self.leaderboard:

            self.leaderboard[winner_name] = score

            print(f"\n{winner_name} has been added to the leaderboard with {self.score} points.")
            self.save_leaderboard()

        elif self.score > self.leaderboard[winner_name]:

            old_score = self.leaderboard[winner_name]

            self.leaderboard[winner_name] = score

            print(f"\nNew best score for {winner_name}!")

            print(f"Previous best: {old_score}")

            print(f"New best: {score}"
            )



