# class Player:

#     def __init__(self, name, total_score = 0):
#         self.name = name
#         self.total_score = total_score
#         self.turn_score = 0


#     def add_to_turn(self, dice):
#         self.turn_score += dice

#     def bank_turn(self):
#         self.total_score += self.turn_score
#         self.turn_score = 0



# abdul = Player("Abdul")

# abdul.total_score = 40
# abdul.turn_score = 17

# abdul.bank_turn()

# print(abdul.total_score)  # 57
# print(abdul.turn_score)   # 0


     

import random
import time

def roll_die():
    return random.randint(1, 6)

def play_pig():
    print("=" * 40)
    print("Welcome to the Pig Dice Game (CLI Version)!")
    print("=" * 40)
    print("Rules: First to 100 points wins.")
    print("Roll a 2-6: Add points to your current turn total.")
    print("Roll a 1: Lose all points accumulated this turn and pass.")
    print("Hold: Bank your current turn total into your global score.\n")

    scores = {"Player": 0, "Computer": 0}
    winning_score = 100

    while scores["Player"] < winning_score and scores["Computer"] < winning_score:
        # --- PLAYER TURN ---
        print(f"\n--- YOUR TURN (Current Global: {scores['Player']} | Computer: {scores['Computer']}) ---")
        turn_score = 0
        while True:
            choice = input("Do you want to (r)oll or (h)old? ").strip().lower()
            if choice == 'r':
                roll = roll_die()
                print(f"🎲 You rolled a {roll}!")
                if roll == 1:
                    print("💥 Pigged out! You lost your points for this turn.")
                    turn_score = 0
                    break
                else:
                    turn_score += roll
                    print(f"Turn total: {turn_score}")
            elif choice == 'h':
                scores["Player"] += turn_score
                print(f"💰 You banked {turn_score} points. New global score: {scores['Player']}")
                break
            else:
                print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")

        if scores["Player"] >= winning_score:
            break

        # --- COMPUTER TURN ---
        print(f"\n--- COMPUTER'S TURN (Current Global: {scores['Computer']} | Player: {scores['Player']}) ---")
        time.sleep(1)
        turn_score = 0
        while True:
            roll = roll_die()
            print(f"🤖 Computer rolled a {roll}...")
            time.sleep(1)
            
            if roll == 1:
                print("💥 Computer pigged out!")
                break
            else:
                turn_score += roll
                # Computer strategy: Hold if turn score >= 20 or if it's enough to win
                if turn_score >= 20 or (scores["Computer"] + turn_score) >= winning_score:
                    scores["Computer"] += turn_score
                    print(f"🤖 Computer decides to hold and banks {turn_score} points.")
                    print(f"Computer global score: {scores['Computer']}")
                    break
                else:
                    print(f"Computer turn total: {turn_score}. Rolling again...")
                    time.sleep(0.5)

    # --- GAME OVER ---
    print("\n" + "=" * 40)
    print("GAME OVER")
    print(f"Final Scores -> Player: {scores['Player']} | Computer: {scores['Computer']}")
    if scores["Player"] >= winning_score:
        print("🎉 Congratulations! You won the game!")
    else:
        print("🤖 The Computer wins. Better luck next time!")
    print("=" * 40)

if __name__ == "__main__":
    play_pig()
