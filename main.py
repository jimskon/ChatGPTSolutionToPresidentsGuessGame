import random
# Jim Skon
# Collection of sentences from inaugural speeches
# Collection of sentences from inaugural speeches
speeches = {
  "George Washington": [
    "The preservation of the sacred fire of liberty...",
    "The propitious smiles of Heaven can never be expected...",
    "The foundations of our national policy...",
  ],
  "Abraham Lincoln": [
    "Fellow-citizens of the United States...",
    "With malice toward none, with charity for all...",
    "It is rather for us to be here dedicated...",
  ],
  "John F. Kennedy": [
    "Ask not what your country can do for you...",
    "Let both sides seek to invoke...",
    "And so, my fellow Americans...",
  ],
  # Add more presidents and their speeches here
}


def select_random_sentence():
  # Randomly select a president and a sentence from their speeches
  president = random.choice(list(speeches.keys()))
  sentence = random.choice(speeches[president])
  return president, sentence


def create_options(correct_option, presidents):
  # Create a list of options with the correct option and two random incorrect options
  options = [correct_option]
  while len(options) < 3:
    random_option = random.choice(presidents)
    if random_option not in options:
      options.append(random_option)
  random.shuffle(options)
  return options


def display_question(question_number, sentence, options):
  # Display the question with the sentence and options
  print(f"Question #{question_number}:")
  print(sentence)
  for i, option in enumerate(options):
    print(f"{chr(65 + i)}. {option}")
  print()


def get_user_answer():
  # Prompt the user for their answer and validate it
  while True:
    user_input = input("Your answer (A, B, or C): ").strip().upper()
    if user_input in ["A", "B", "C"]:
      return user_input


def check_answer(user_answer, correct_option):
  # Compare the user's answer with the correct option and provide feedback
  if user_answer == correct_option:
    print("Correct answer!")
    return True
  else:
    print("Incorrect answer!")
    print(f"The correct answer is: {correct_option}")
    return False


def play_game():
  presidents = list(speeches.keys())
  score = 0

  # Game loop
  while True:
    president, sentence = select_random_sentence()
    options = create_options(president, presidents)
    display_question(score + 1, sentence, options)
    user_answer = get_user_answer()
    is_correct = check_answer(user_answer, options.index(president) + 1)

    if is_correct:
      score += 1

    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
      break

  print(f"Your final score is: {score}")


# Start the game
print("Welcome to the Presidents' Inaugural Speeches Game!")
play_game()
