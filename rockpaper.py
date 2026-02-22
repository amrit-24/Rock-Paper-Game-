import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def show_choices(user, computer):
    emojis = {
        "rock": "🪨",
        "paper": "📄",
        "scissors": "✂️"
    }
    print(f"\nYou chose: {user} {emojis[user]}")
    print(f"Computer chose: {computer} {emojis[computer]}")

def main():
    user_score = 0
    computer_score = 0
    round_no = 1

    print("🎮 Welcome to Rock Paper Scissors Game 🎮")

    while True:
        print(f"\n--- Round {round_no} ---")
        print("Choose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            break

        if choice not in ["1", "2", "3"]:
            print("❌ Invalid choice. Try again.")
            continue

        user_choice = ["rock", "paper", "scissors"][int(choice) - 1]
        computer_choice = get_computer_choice()

        show_choices(user_choice, computer_choice)

        result = decide_winner(user_choice, computer_choice)

        if result == "user":
            print("🎉 You WIN this round!")
            user_score += 1
        elif result == "computer":
            print("💻 Computer WINS this round!")
            computer_score += 1
        else:
            print("🤝 It's a TIE!")

        print(f"📊 Score → You: {user_score} | Computer: {computer_score}")
        round_no += 1

    print("\n🏁 Game Over")
    print(f"Final Score → You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("🏆 Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("😢 Computer wins overall. Better luck next time!")
    else:
        print("🤝 Match Draw!")

    print("Thanks for playing 😊")

main()