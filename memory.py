import os
import json
import random
import time

def main():
    play = ""
    name = ""
    high_scores = get_data()
    while True:
        print("\nWelcome to the Memory Game!")
        name = input("Please enter your name: ")
        print("\nCurrent High Scores:")
        for player in high_scores:
            print(f"Name: {player['name']}, Score: {player['score']}")
        play = input("Press Enter to start or 'q' to quit: ").lower().strip()
        if play == 'q':
            print("Thanks for playing! Goodbye.")
            break
        num = get_num(3)
        score = play_game(num, name)
        high_scores = update_high_scores(high_scores, score, name)
        save_high_scores(high_scores)
        play_again = input("Would you like to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

def get_data():
    if not os.path.exists("high_scores.json"):
        return []
    with open("high_scores.json", "r") as file:
        return json.load(file)

def get_num(level):
    return [str(random.randint(0, 9)) for _ in range(level)]

def play_game(num, name):
    score = 0
    level = 3
    while True:
        print(f"\nRemember this sequence: {''.join(num)}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_time = time.time()
        guess = input("Enter the sequence you just saw: ").strip()
        response_time = time.time() - start_time
        if guess == ''.join(num):
            print("Correct! Well done!")
            score += int(100 / response_time)
            print(f"Current score: {score}")
            level += 1
            num = get_num(level)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f"Incorrect! The correct sequence was: {''.join(num)}")
            break
    return score

def update_high_scores(high_scores, score, name):
    high_scores.append({"name": name, "score": score})
    high_scores.sort(key=lambda x: x['score'], reverse=True)
    if len(high_scores) > 5:
        high_scores.pop()
    return high_scores

def save_high_scores(high_scores):
    with open("high_scores.json", "w") as file:
        json.dump(high_scores, file, indent=4)

if __name__ == "__main__":
    main()
